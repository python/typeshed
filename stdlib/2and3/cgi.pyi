import sys
from typing import Any, AnyStr, Dict, IO, Iterable, List, Mapping, Optional, Tuple, TypeVar, Union

_T = TypeVar('_T', bound=FieldStorage)

def parse(fp: IO[Any] = ..., environ: Mapping[str, str] = ...,
          keep_blank_values: bool = ..., strict_parsing: bool = ...) -> Dict[str, List[str]]: ...
def parse_qs(qs: str, keep_blank_values: bool = ..., strict_parsing: bool = ...) -> Dict[str, List[str]]: ...
def parse_qsl(qs: str, keep_blank_values: bool = ..., strict_parsing: bool = ...) -> Dict[str, List[str]]: ...
if sys.version_info >= (3, 7):
    def parse_multipart(fp: IO[Any], pdict: Mapping[str, bytes], encoding: str, errors: str) -> Dict[str, List[Union[str, bytes]]]: ...
else:
    def parse_multipart(fp: IO[Any], pdict: Mapping[str, bytes]) -> Dict[str, List[bytes]]: ...
def parse_header(s: str) -> Tuple[str, Dict[str, str]]: ...
def test(environ: Mapping[str, str] = ...) -> None: ...
def print_environ(environ: Mapping[str, str] = ...) -> None: ...
def print_form(form: Dict[str, Any]) -> None: ...
def print_directory() -> None: ...
def print_environ_usage() -> None: ...
if sys.version_info >= (3, 0):
    def escape(s: str, quote: bool = ...) -> str: ...
else:
    def escape(s: AnyStr, quote: bool = ...) -> AnyStr: ...


class MiniFieldStorage:
    # The first five "Any" attributes here are always None, but mypy doesn't support that
    filename = ...  # type: Any
    list = ...  # type: Any
    type = ...  # type: Any
    file = ...  # type: Optional[IO[bytes]]  # Always None
    type_options = ...  # type: Dict[Any, Any]
    disposition = ...  # type: Any
    disposition_options = ...  # type: Dict[Any, Any]
    headers = ...  # type: Dict[Any, Any]
    name = ...  # type: Any
    value = ...  # type: Any

    def __init__(self, name: Any, value: Any) -> None: ...
    def __repr__(self) -> str: ...


class FieldStorage(object):
    FieldStorageClass = ...  # type: Optional[type]
    keep_blank_values = ...  # type: int
    strict_parsing = ...  # type: int
    qs_on_post = ...  # type: Optional[str]
    headers = ...  # type: Mapping[str, str]
    fp = ...  # type: IO[bytes]
    encoding = ...  # type: str
    errors = ...  # type: str
    outerboundary = ...  # type: bytes
    bytes_read = ...  # type: int
    limit = ...  # type: Optional[int]
    disposition = ...  # type: str
    disposition_options = ...  # type: Dict[str, str]
    filename = ...  # type: Optional[str]
    file = ...  # type: Optional[IO[bytes]]
    type = ...  # type: str
    type_options = ...  # type: Dict[str, str]
    innerboundary = ...  # type: bytes
    length = ...  # type: int
    done = ...  # type: int
    list = ...  # type: Optional[List[Any]]
    value = ...  # type: Union[None, bytes, List[Any]]

    if sys.version_info >= (3, 0):
        def __init__(self, fp: IO[Any] = ..., headers: Mapping[str, str] = ..., outerboundary: bytes = ...,
                     environ: Mapping[str, str] = ..., keep_blank_values: int = ..., strict_parsing: int = ...,
                     limit: int = ..., encoding: str = ..., errors: str = ...) -> None: ...
    else:
        def __init__(self, fp: IO[Any] = ..., headers: Mapping[str, str] = ..., outerboundary: bytes = ...,
                     environ: Mapping[str, str] = ..., keep_blank_values: int = ..., strict_parsing: int = ...) -> None: ...

    if sys.version_info >= (3, 0):
        def __enter__(self: _T) -> _T: ...
        def __exit__(self, *args: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterable[str]: ...
    def __getitem__(self, key: str) -> Any: ...
    def getvalue(self, key: str, default: Any = ...) -> Any: ...
    def getfirst(self, key: str, default: Any = ...) -> Any: ...
    def getlist(self, key: str) -> List[Any]: ...
    def keys(self) -> List[str]: ...
    if sys.version_info < (3, 0):
        def has_key(self, key: str) -> bool: ...
    def __contains__(self, key: str) -> bool: ...
    def __len__(self) -> int: ...
    if sys.version_info >= (3, 0):
        def __bool__(self) -> bool: ...
    else:
        def __nonzero__(self) -> bool: ...
    if sys.version_info >= (3, 0):
        # In Python 3 it returns bytes or str IO depending on an internal flag
        def make_file(self) -> IO[Any]: ...
    else:
        # In Python 2 it always returns bytes and ignores the "binary" flag
        def make_file(self, binary: Any = ...) -> IO[bytes]: ...


if sys.version_info < (3, 0):
    from UserDict import UserDict

    class FormContentDict(UserDict):
        query_string = ...  # type: str
        def __init__(self, environ: Mapping[str, str] = ..., keep_blank_values: int = ..., strict_parsing: int = ...) -> None: ...

    class SvFormContentDict(FormContentDict):
        def getlist(self, key: Any) -> Any: ...

    class InterpFormContentDict(SvFormContentDict): ...

    class FormContent(FormContentDict):
        # TODO this should have
        # def values(self, key: Any) -> Any: ...
        # but this is incompatible with the supertype, and adding '# type: ignore' triggers
        # a parse error in pytype (https://github.com/google/pytype/issues/53)
        def indexed_value(self, key: Any, location: int) -> Any: ...
        def value(self, key: Any) -> Any: ...
        def length(self, key: Any) -> int: ...
        def stripped(self, key: Any) -> Any: ...
        def pars(self) -> Dict[Any, Any]: ...
