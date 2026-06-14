import contextlib
import logging
from _typeshed import Incomplete
from collections.abc import Generator

LOGGER: Incomplete
PROGRESS_LOGGER: Incomplete

class CallbackHandler(logging.Handler):
    emit: Incomplete
    def __init__(self, callback) -> None: ...

@contextlib.contextmanager
def capture_logs(logger: str = "weasyprint", level=None) -> Generator[Incomplete]: ...
