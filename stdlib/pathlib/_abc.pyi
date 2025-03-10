import types
from _typeshed import AnyOrLiteralStr, BytesPath, ReadableBuffer, StrOrBytesPath, StrPath
from collections.abc import Callable, Generator, Iterator, Sequence
from os import PathLike, stat_result
from typing import IO, Any, AnyStr, ClassVar, overload
from typing_extensions import LiteralString, Self

__all__ = ["UnsupportedOperation"]

class UnsupportedOperation(NotImplementedError): ...

class ParserBase:
    @property
    def sep(self) -> str: ...
    @overload
    def join(self, path: LiteralString, *paths: LiteralString) -> LiteralString: ...
    @overload
    def join(self, path: StrPath, *paths: StrPath) -> str: ...
    @overload
    def join(self, path: BytesPath, *paths: BytesPath) -> bytes: ...
    @overload
    def split(self, path: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
    @overload
    def split(self, path: AnyOrLiteralStr) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
    @overload
    def splitdrive(self, path: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
    @overload
    def splitdrive(self, path: AnyOrLiteralStr) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
    @overload
    def normcase(self, path: PathLike[AnyStr]) -> AnyStr: ...
    @overload
    def normcase(self, path: AnyOrLiteralStr) -> AnyOrLiteralStr: ...
    def isabs(self, path: StrOrBytesPath) -> bool: ...

class PurePathBase:
    parser: ClassVar[types.ModuleType | ParserBase]
    def __init__(self, path: StrPath, *paths: StrPath) -> None: ...
    def with_segments(self, *pathsegments: StrPath) -> Self: ...
    def as_posix(self) -> str: ...
    @property
    def drive(self) -> str: ...
    @property
    def root(self) -> str: ...
    @property
    def anchor(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def suffix(self) -> str: ...
    @property
    def suffixes(self) -> list[str]: ...
    @property
    def stem(self) -> str: ...
    def with_name(self, name: str) -> Self: ...
    def with_stem(self, stem: str) -> Self: ...
    def with_suffix(self, suffix: str) -> Self: ...
    def relative_to(self, other: StrPath, *, walk_up: bool = False) -> Self: ...
    def is_relative_to(self, other: StrPath) -> bool: ...
    @property
    def parts(self) -> tuple[str, ...]: ...
    def joinpath(self, *pathsegments: StrPath) -> Self: ...
    def __truediv__(self, key: StrPath) -> Self: ...
    def __rtruediv__(self, key: StrPath) -> Self: ...
    @property
    def parent(self) -> Self: ...
    @property
    def parents(self) -> Sequence[Self]: ...
    def is_absolute(self) -> bool: ...
    def match(self, path_pattern: str, *, case_sensitive: bool | None = None) -> bool: ...
    def full_match(self, pattern: StrPath, *, case_sensitive: bool | None = None) -> bool: ...

class PathBase(PurePathBase):
    def stat(self, *, follow_symlinks: bool = True) -> stat_result: ...
    def lstat(self) -> stat_result: ...
    def exists(self, *, follow_symlinks: bool = True) -> bool: ...
    def is_dir(self, *, follow_symlinks: bool = True) -> bool: ...
    def is_file(self, *, follow_symlinks: bool = True) -> bool: ...
    def is_mount(self) -> bool: ...
    def is_symlink(self) -> bool: ...
    def is_junction(self) -> bool: ...
    def is_block_device(self) -> bool: ...
    def is_char_device(self) -> bool: ...
    def is_fifo(self) -> bool: ...
    def is_socket(self) -> bool: ...
    def samefile(self, other_path: StrPath) -> bool: ...
    def open(
        self,
        mode: str = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
    ) -> IO[Any]: ...
    def read_bytes(self) -> bytes: ...
    def read_text(self, encoding: str | None = None, errors: str | None = None, newline: str | None = None) -> str: ...
    def write_bytes(self, data: ReadableBuffer) -> int: ...
    def write_text(
        self, data: str, encoding: str | None = None, errors: str | None = None, newline: str | None = None
    ) -> int: ...
    def iterdir(self) -> Generator[Self, None, None]: ...
    def glob(self, pattern: str, *, case_sensitive: bool | None = None, recurse_symlinks: bool = True) -> Iterator[Self]: ...
    def rglob(self, pattern: str, *, case_sensitive: bool | None = None, recurse_symlinks: bool = True) -> Iterator[Self]: ...
    def walk(
        self, top_down: bool = True, on_error: Callable[[OSError], object] | None = None, follow_symlinks: bool = False
    ) -> Iterator[tuple[Self, list[str], list[str]]]: ...
    def absolute(self) -> Self: ...
    @classmethod
    def cwd(cls) -> Self: ...
    def expanduser(self) -> Self: ...
    @classmethod
    def home(cls) -> Self: ...
    def readlink(self) -> Self: ...
    def resolve(self, strict: bool = False) -> Self: ...
    def symlink_to(self, target: StrOrBytesPath, target_is_directory: bool = False) -> None: ...
    def hardlink_to(self, target: StrOrBytesPath) -> None: ...
    def touch(self, mode: int = 0o666, exist_ok: bool = True) -> None: ...
    def mkdir(self, mode: int = 0o777, parents: bool = False, exist_ok: bool = False) -> None: ...
    def rename(self, target: StrPath) -> Self: ...
    def replace(self, target: StrPath) -> Self: ...
    def chmod(self, mode: int, *, follow_symlinks: bool = True) -> None: ...
    def lchmod(self, mode: int) -> None: ...
    def unlink(self, missing_ok: bool = False) -> None: ...
    def rmdir(self) -> None: ...
    def owner(self, *, follow_symlinks: bool = True) -> str: ...
    def group(self, *, follow_symlinks: bool = True) -> str: ...
    @classmethod
    def from_uri(cls, uri: str) -> Self: ...
    def as_uri(self) -> str: ...
