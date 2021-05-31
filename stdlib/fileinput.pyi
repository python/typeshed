import sys
from _typeshed import StrOrBytesPath
from typing import IO, Any, AnyStr, Callable, Generic, Iterable, Iterator, Optional, Union

if sys.version_info >= (3, 10):
    def input(
        files: Union[StrOrBytesPath, Iterable[StrOrBytesPath], None] = ...,
        inplace: bool = ...,
        backup: str = ...,
        *,
        mode: str = ...,
        openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
    ) -> FileInput[AnyStr]: ...

elif sys.version_info >= (3, 8):
    def input(
        files: Union[StrOrBytesPath, Iterable[StrOrBytesPath], None] = ...,
        inplace: bool = ...,
        backup: str = ...,
        *,
        mode: str = ...,
        openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
    ) -> FileInput[AnyStr]: ...

else:
    def input(
        files: Union[StrOrBytesPath, Iterable[StrOrBytesPath], None] = ...,
        inplace: bool = ...,
        backup: str = ...,
        bufsize: int = ...,
        mode: str = ...,
        openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
    ) -> FileInput[AnyStr]: ...

def close() -> None: ...
def nextfile() -> None: ...
def filename() -> str: ...
def lineno() -> int: ...
def filelineno() -> int: ...
def fileno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...

class FileInput(Iterable[AnyStr], Generic[AnyStr]):
    if sys.version_info >= (3, 10):
        def __init__(
            self,
            files: Union[None, StrOrBytesPath, Iterable[StrOrBytesPath]] = ...,
            inplace: bool = ...,
            backup: str = ...,
            *,
            mode: str = ...,
            openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
            encoding: Optional[str] = ...,
            errors: Optional[str] = ...,
        ) -> None: ...
    elif sys.version_info >= (3, 8):
        def __init__(
            self,
            files: Union[None, StrOrBytesPath, Iterable[StrOrBytesPath]] = ...,
            inplace: bool = ...,
            backup: str = ...,
            *,
            mode: str = ...,
            openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            files: Union[None, StrOrBytesPath, Iterable[StrOrBytesPath]] = ...,
            inplace: bool = ...,
            backup: str = ...,
            bufsize: int = ...,
            mode: str = ...,
            openhook: Callable[[StrOrBytesPath, str], IO[AnyStr]] = ...,
        ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> FileInput[AnyStr]: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def __iter__(self) -> Iterator[AnyStr]: ...
    def __next__(self) -> AnyStr: ...
    def __getitem__(self, i: int) -> AnyStr: ...
    def nextfile(self) -> None: ...
    def readline(self) -> AnyStr: ...
    def filename(self) -> str: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...

if sys.version_info >= (3, 10):
    def hook_compressed(
        filename: StrOrBytesPath, mode: str, encoding: Optional[str] = ..., errors: Optional[str] = ...
    ) -> IO[Any]: ...

else:
    def hook_compressed(filename: StrOrBytesPath, mode: str) -> IO[Any]: ...

def hook_encoded(encoding: str, errors: Optional[str] = ...) -> Callable[[StrOrBytesPath, str], IO[Any]]: ...
