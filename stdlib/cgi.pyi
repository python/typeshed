from _typeshed import SupportsContainsAndGetItem, SupportsGetItem, SupportsItemAccess, Unused
from builtins import list as _list, type as _type
from collections.abc import Iterable, Iterator, Mapping
from email.message import Message
from types import TracebackType
from typing import IO, Any, Protocol, type_check_only
from typing_extensions import Self

__all__ = [
    "MiniFieldStorage",
    "FieldStorage",
    "parse",
    "parse_multipart",
    "parse_header",
    "test",
    "print_exception",
    "print_environ",
    "print_form",
    "print_directory",
    "print_arguments",
    "print_environ_usage",
]

def parse(
    fp: IO[Any] | None = None,
    environ: SupportsItemAccess[str, str] = ...,
    keep_blank_values: bool = ...,
    strict_parsing: bool = ...,
    separator: str = "&",
) -> dict[str, list[str]]: ...
def parse_multipart(
    fp: IO[Any], pdict: SupportsGetItem[str, bytes], encoding: str = "utf-8", errors: str = "replace", separator: str = "&"
) -> dict[str, list[Any]]: ...
@type_check_only
class _Environ(Protocol):
    def __getitem__(self, k: str, /) -> str: ...
    def keys(self) -> Iterable[str]: ...

def parse_header(line: str) -> tuple[str, dict[str, str]]: ...
def test(environ: _Environ = ...) -> None: ...
def print_environ(environ: _Environ = ...) -> None: ...
def print_form(form: dict[str, Any]) -> None: ...
def print_directory() -> None: ...
def print_environ_usage() -> None: ...

class MiniFieldStorage:
    # The first five "Any" attributes here are always None, but mypy doesn't support that
    filename: Any
    list: Any
    type: Any
    file: IO[bytes] | None
    type_options: dict[Any, Any]
    disposition: Any
    disposition_options: dict[Any, Any]
    headers: dict[Any, Any]
    name: Any
    value: Any
    def __init__(self, name: Any, value: Any) -> None: ...

class FieldStorage:
    FieldStorageClass: _type | None
    keep_blank_values: int
    strict_parsing: int
    qs_on_post: str | None
    headers: Mapping[str, str] | Message
    fp: IO[bytes]
    encoding: str
    errors: str
    outerboundary: bytes
    bytes_read: int
    limit: int | None
    disposition: str
    disposition_options: dict[str, str]
    filename: str | None
    file: IO[bytes] | None
    type: str
    type_options: dict[str, str]
    innerboundary: bytes
    length: int
    done: int
    list: _list[Any] | None
    value: None | bytes | _list[Any]
    def __init__(
        self,
        fp: IO[Any] | None = None,
        headers: Mapping[str, str] | Message | None = None,
        outerboundary: bytes = b"",
        environ: SupportsContainsAndGetItem[str, str] = ...,
        keep_blank_values: int = 0,
        strict_parsing: int = 0,
        limit: int | None = None,
        encoding: str = "utf-8",
        errors: str = "replace",
        max_num_fields: int | None = None,
        separator: str = "&",
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, key: str) -> Any: ...
    def getvalue(self, key: str, default: Any = None) -> Any: ...
    def getfirst(self, key: str, default: Any = None) -> Any: ...
    def getlist(self, key: str) -> _list[Any]: ...
    def keys(self) -> _list[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __del__(self) -> None: ...
    # Returns bytes or str IO depending on an internal flag
    def make_file(self) -> IO[Any]: ...

def print_exception(
    type: type[BaseException] | None = None,
    value: BaseException | None = None,
    tb: TracebackType | None = None,
    limit: int | None = None,
) -> None: ...
def print_arguments() -> None: ...
