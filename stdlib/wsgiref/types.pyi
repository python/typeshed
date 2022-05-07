from collections.abc import Callable, Iterable
from sys import _OptExcInfo
from typing import Any, Protocol
from typing_extensions import TypeAlias

__all__ = ["StartResponse", "WSGIEnvironment", "WSGIApplication", "InputStream", "ErrorStream", "FileWrapper"]

class StartResponse(Protocol):
    def __call__(
        self, __status: str, __headers: list[tuple[str, str]], __exc_info: _OptExcInfo | None = ...
    ) -> Callable[[bytes], object]: ...

WSGIEnvironment: TypeAlias = dict[str, Any]
WSGIApplication: TypeAlias = Callable[[WSGIEnvironment, StartResponse], Iterable[bytes]]

class InputStream(Protocol):
    def read(self, __size: int = ...) -> bytes: ...
    def readline(self, __size: int = ...) -> bytes: ...
    def readlines(self, __hint: int = ...) -> list[bytes]: ...
    def __iter__(self) -> Iterable[bytes]: ...

class ErrorStream(Protocol):
    def flush(self) -> object: ...
    def write(self, __s: str) -> object: ...
    def writelines(self, __seq: list[str]) -> object: ...

class _Readable(Protocol):
    def read(self, __size: int = ...) -> bytes: ...
    # Optional: def close(self) -> object: ...

class FileWrapper(Protocol):
    def __call__(self, __file: _Readable, __block_size: int = ...) -> Iterable[bytes]: ...
