import sys

if sys.version_info >= (3, 11):
    __all__ = (
        "BrokenBarrierError",
        "CancelledError",
        "IncompleteReadError",
        "InvalidStateError",
        "LimitOverrunError",
        "SendfileNotAvailableError",
        "TimeoutError",
    )
else:
    __all__ = (
        "CancelledError",
        "IncompleteReadError",
        "InvalidStateError",
        "LimitOverrunError",
        "SendfileNotAvailableError",
        "TimeoutError",
    )

class CancelledError(BaseException): ...

if sys.version_info >= (3, 11):
    from builtins import TimeoutError as TimeoutError
else:
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

if sys.version_info >= (3, 11):
    class BrokenBarrierError(RuntimeError): ...
