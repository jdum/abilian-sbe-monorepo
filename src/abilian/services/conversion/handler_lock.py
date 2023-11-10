import functools
import os
from collections.abc import Callable
from pathlib import Path

from filelock import FileLock, Timeout

from .exceptions import ConversionError

LOCK_EXPIRE = 1800  # 30 min, in case many request in //


def acquire_lock(name: str) -> Callable:
    """Ensure the decorated function is alone to run by using a lock file."""
    var_run = Path(os.environ.get("INSTANCE_VAR_RUN", "/var/run"))
    lock = FileLock(var_run / f"{name}.lock", timeout=LOCK_EXPIRE)

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
