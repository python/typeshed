from _typeshed.wsgi import ErrorStream, InputStream, WSGIApplication
from collections.abc import Callable, Iterable, Iterator
from typing import Any, NoReturn
from typing_extensions import TypeAlias

__all__ = ["validator"]

class WSGIWarning(Warning): ...

def validator(application: WSGIApplication) -> WSGIApplication: ...

class InputWrapper:
    input: InputStream
    def __init__(self, wsgi_input: InputStream) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self, size: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> bytes: ...
    def __iter__(self) -> Iterable[bytes]: ...
    def close(self) -> NoReturn: ...

class ErrorWrapper:
    errors: ErrorStream
    def __init__(self, wsgi_errors: ErrorStream) -> None: ...
    def write(self, s: str) -> None: ...
    def flush(self) -> None: ...
    def writelines(self, seq: Iterable[str]) -> None: ...
    def close(self) -> NoReturn: ...

_WriterCallback: TypeAlias = Callable[[bytes], Any]

class WriteWrapper:
    writer: _WriterCallback
    def __init__(self, wsgi_writer: _WriterCallback) -> None: ...
    def __call__(self, s: bytes) -> None: ...

class PartialIteratorWrapper:
    iterator: Iterator[bytes]
    def __init__(self, wsgi_iterator: Iterator[bytes]) -> None: ...
    def __iter__(self) -> IteratorWrapper: ...

class IteratorWrapper:
    original_iterator: Iterator[bytes]
    iterator: Iterator[bytes]
    closed: bool
    check_start_response: bool | None
    def __init__(self, wsgi_iterator: Iterator[bytes], check_start_response: bool | None) -> None: ...
    def __iter__(self) -> IteratorWrapper: ...
    def __next__(self) -> bytes: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
