from random import Random
from thread import LockType
from typing import IO, Any, AnyStr, Iterable, Iterator, List, Text, Tuple, Union, overload

TMP_MAX: int
tempdir: str
template: str
_name_sequence: _RandomNameSequence | None

class _RandomNameSequence:
    characters: str = ...
    mutex: LockType
    @property
    def rng(self) -> Random: ...
    def __iter__(self) -> _RandomNameSequence: ...
    def next(self) -> str: ...
    # from os.path:
    def normcase(self, path: AnyStr) -> AnyStr: ...

class _TemporaryFileWrapper(IO[str]):
    delete: bool
    file: IO[str]
    name: Any
    def __init__(self, file: IO[str], name: Any, delete: bool = ...) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> _TemporaryFileWrapper: ...
    def __exit__(self, exc, value, tb) -> bool | None: ...
    def __getattr__(self, name: unicode) -> Any: ...
    def close(self) -> None: ...
    def unlink(self, path: unicode) -> None: ...
    # These methods don't exist directly on this object, but
    # are delegated to the underlying IO object through __getattr__.
    # We need to add them here so that this class is concrete.
    def __iter__(self) -> Iterator[str]: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def next(self) -> str: ...
    def read(self, n: int = ...) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> str: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: Text) -> int: ...
    def writelines(self, lines: Iterable[str]) -> None: ...

# TODO text files

def TemporaryFile(
    mode: bytes | unicode = ...,
    bufsize: int = ...,
    suffix: bytes | unicode = ...,
    prefix: bytes | unicode = ...,
    dir: bytes | unicode = ...,
) -> _TemporaryFileWrapper: ...
def NamedTemporaryFile(
    mode: bytes | unicode = ...,
    bufsize: int = ...,
    suffix: bytes | unicode = ...,
    prefix: bytes | unicode = ...,
    dir: bytes | unicode = ...,
    delete: bool = ...,
) -> _TemporaryFileWrapper: ...
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: bytes | unicode = ...,
    buffering: int = ...,
    suffix: bytes | unicode = ...,
    prefix: bytes | unicode = ...,
    dir: bytes | unicode = ...,
) -> _TemporaryFileWrapper: ...

class TemporaryDirectory:
    name: Any
    def __init__(
        self, suffix: bytes | unicode = ..., prefix: bytes | unicode = ..., dir: bytes | unicode = ...
    ) -> None: ...
    def cleanup(self) -> None: ...
    def __enter__(self) -> Any: ...  # Can be str or unicode
    def __exit__(self, type, value, traceback) -> None: ...

@overload
def mkstemp() -> Tuple[int, str]: ...
@overload
def mkstemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr | None = ..., text: bool = ...) -> Tuple[int, AnyStr]: ...
@overload
def mkdtemp() -> str: ...
@overload
def mkdtemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr | None = ...) -> AnyStr: ...
@overload
def mktemp() -> str: ...
@overload
def mktemp(suffix: AnyStr = ..., prefix: AnyStr = ..., dir: AnyStr | None = ...) -> AnyStr: ...
def gettempdir() -> str: ...
def gettempprefix() -> str: ...
def _candidate_tempdir_list() -> List[str]: ...
def _get_candidate_names() -> _RandomNameSequence | None: ...
def _get_default_tempdir() -> str: ...
