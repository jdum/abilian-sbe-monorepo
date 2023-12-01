"""Celery tasks related to document transformation and preview."""
from __future__ import annotations
from loguru import logger

# import logging
from abilian.logutils.configure import connect_logger
from collections.abc import Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING

from celery import shared_task
from sqlalchemy.orm import Session

from abilian.core.extensions import db
from abilian.services import converter, get_service
from abilian.services.conversion import ConversionError, HandlerNotFound

if TYPE_CHECKING:
    from .models import Document

# logger = logging.getLogger(__package__)
connect_logger(logger)


@contextmanager
def get_document(
    document_id: int, session: Session | None = None
) -> Iterator[tuple[Session, Document | None]]:
    """Context manager that yields (session, document)."""
    from .models import Document

    connect_logger(logger)
    logger.debug(f"get_document() {document_id=} {session=}")

    if session is None:
        doc_session = db.create_scoped_session()
    else:
        doc_session = session

    with doc_session.begin_nested():
        query = doc_session.query(Document)
        document = query.get(document_id)
        yield (doc_session, document)

    # cleanup
    if session is None:
        doc_session.commit()
        doc_session.close()


@shared_task
def process_document(document_id: int) -> None:
    """Run document processing chain."""
    connect_logger(logger)
    logger.debug(f"in process_document() {document_id=}")
    with get_document(document_id) as (session, document):
        if document is None:
            return

        # True = Ok, None means no check performed (no antivirus present)
        is_clean = _run_antivirus(document)
        logger.debug(f"process_document() {document_id=} {is_clean=}")
        if is_clean is False:
            return
    logger.debug(f"out process_document() {document_id=}")
    preview_document.delay(document_id)
    logger.debug(f"before convert process_document() {document_id=}")
    convert_document_content.delay(document_id)
    logger.debug(f"exit process_document() {document_id=}")


def _run_antivirus(document: Document) -> bool | None:
    antivirus = get_service("antivirus")
    if antivirus and antivirus.running:
        is_clean = antivirus.scan(document.content_blob)
        if "antivirus_task" in document.content_blob.meta:
            del document.content_blob.meta["antivirus_task"]
        return is_clean
    return None


@shared_task
def antivirus_scan(document_id):
    """Return antivirus.scan() result."""
    with get_document(document_id) as (session, document):
        if document is None:
            return None
        return _run_antivirus(document)


@shared_task
def preview_document(document_id: int) -> None:
    """Compute the document preview images with its default preview size."""
    connect_logger(logger)
    logger.debug(f"preview_document() {document_id=}")
    with get_document(document_id) as (session, document):
        logger.debug(f"preview_document() {document_id=} {document=}")
        if document is None:
            # deleted after task queued, but before task run
            return

        try:
            converter.to_image(
                document.content_digest,
                document.content,
                document.content_type,
                0,
                document.preview_size,
            )
        except ConversionError as e:
            logger.info(
                "Preview failed: %s", str(e), exc_info=True, extra={"stack": True}
            )
    logger.debug(f"exit preview_document() {document_id=}")


@shared_task
def convert_document_content(document_id: int) -> None:
    """Convert document content."""
    connect_logger(logger)
    logger.debug(f"convert_document_content() {document_id=}")
    with get_document(document_id) as (session, doc):
        if doc is None:
            # deleted after task queued, but before task run
            return

        convert_to_pdf(doc)
        convert_to_text(doc)
        extract_metadata(doc)


def convert_to_pdf(doc: Document) -> None:
    error_kwargs = {"exc_info": True, "extra": {"stack": True}}
    connect_logger(logger)

    if doc.content_type == "application/pdf":
        doc.pdf = doc.content
    else:
        try:
            doc.pdf = converter.to_pdf(
                doc.content_digest, doc.content, doc.content_type
            )
        except HandlerNotFound:
            doc.pdf = b""
        except ConversionError as e:
            doc.pdf = b""
            logger.info(
                "Conversion to PDF failed for document %s: %s",
                doc.name,
                e,
                **error_kwargs,
            )


def convert_to_text(doc: Document) -> None:
    error_kwargs = {"exc_info": True, "extra": {"stack": True}}
    connect_logger(logger)
    try:
        doc.text = converter.to_text(doc.content_digest, doc.content, doc.content_type)
    except ConversionError as e:
        doc.text = ""
        logger.info(
            "Conversion to text failed for document %s: %s", doc.name, e, **error_kwargs
        )


def extract_metadata(doc: Document) -> None:
    error_kwargs = {"exc_info": True, "extra": {"stack": True}}
    connect_logger(logger)
    doc.extra_metadata = {}
    try:
        doc.extra_metadata = converter.get_metadata(
            doc.content_digest, doc.content, doc.content_type
        )
    except ConversionError as e:
        logger.warning(
            "Metadata extraction failed on document %s: %s", doc.name, e, **error_kwargs
        )
    except UnicodeDecodeError as e:
        logger.error("Unicode issue on document %s: %s", doc.name, e, **error_kwargs)
    except Exception as e:
        logger.error("Other issue on document %s: %s", doc.name, e, **error_kwargs)

    if doc.text:
        import langid

        doc.language = langid.classify(doc.text)[0]

    doc.page_num = doc.extra_metadata.get("PDF:Pages", 1)
