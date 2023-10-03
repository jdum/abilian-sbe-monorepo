"""Simple redis extension."""
from __future__ import annotations

import redis
from flask import Flask


class Redis:
    """Redis extension for flask."""

    client = None

    def __init__(self, app: Flask | None = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        uri = app.config.get("REDIS_URI")
        if app.testing:
            return
        if not uri:
            app.logger.warning(
                "Redis extension: REDIS_URI is not defined "
                "in application configuration"
            )
            return
        app.logger.info(f"connection to REDIS_URI {uri}")
        self.client = redis.from_url(uri)
        app.extensions["redis"] = self
