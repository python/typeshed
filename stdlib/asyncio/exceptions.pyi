import sys
from typing import Optional

if sys.version_info >= (3, 8):
    class CancelledError(BaseException): ...
    class TimeoutError(Exception): ...
    class InvalidStateError(Exception): ...
    class SendfileNotAvailableError(RuntimeError): ...
    class IncompleteReadError(EOFError):
        expected: int | None
        partial: bytes
        def __init__(self, partial: bytes, expected: int | None) -> None: ...
    class LimitOverrunError(Exception):
        consumed: int
        def __init__(self, message: str, consumed: int) -> None: ...
