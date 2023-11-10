import functools
from collections.abc import Callable
from pathlib import Path

from filelock import FileLock, Timeout

from .exceptions import ConversionError
from .util import get_tmp_dir

LOCK_EXPIRE = 1800  # 30 min, in case many request in //


def acquire_lock(name: str) -> Callable:
    """Ensure the decorated function is alone to run by using a lock file."""
    lock = FileLock(
        get_tmp_dir() / f"{name}.lock",
        timeout=LOCK_EXPIRE,
    )

    def locked(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                lock.acquire()
                return func(*args, **kwargs)
            except Timeout as e:
                raise ConversionError from e
            finally:
                lock.release()

        return wrapper

    return locked
