import sys
from _typeshed import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    ReadableBuffer,
    StrOrBytesPath,
    StrPath,
)
from collections.abc import Callable, Generator, Iterator, Sequence
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
from os import PathLike, stat_result
from types import TracebackType
from typing import IO, Any, BinaryIO, overload
from typing_extensions import Literal, Self

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ["PurePath", "PurePosixPath", "PureWindowsPath", "Path", "PosixPath", "WindowsPath"]

class PurePath(PathLike[str]):
    @property
    def parts(self) -> tuple[str, ...]: ...
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
    def __new__(cls, *args: StrPath) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __fspath__(self) -> str: ...
    def __lt__(self, other: PurePath) -> bool: ...
    def __le__(self, other: PurePath) -> bool: ...
    def __gt__(self, other: PurePath) -> bool: ...
    def __ge__(self, other: PurePath) -> bool: ...
    def __truediv__(self, key: StrPath) -> Self: ...
    def __rtruediv__(self, key: StrPath) -> Self: ...
    def __bytes__(self) -> bytes: ...
    def as_posix(self) -> str: ...
    def as_uri(self) -> str: ...
    def is_absolute(self) -> bool: ...
    def is_reserved(self) -> bool: ...
    if sys.version_info >= (3, 9):
        def is_relative_to(self, *other: StrPath) -> bool: ...

    def match(self, path_pattern: str) -> bool: ...
    def relative_to(self, *other: StrPath) -> Self: ...
    def with_name(self, name: str) -> Self: ...
    if sys.version_info >= (3, 9):
        def with_stem(self, stem: str) -> Self: ...

    def with_suffix(self, suffix: str) -> Self: ...
    def joinpath(self, *other: StrPath) -> Self: ...
    @property
    def parents(self) -> Sequence[Self]: ...
    @property
    def parent(self) -> Self: ...
    if sys.version_info >= (3, 9) and sys.version_info < (3, 11):
        def __class_getitem__(cls, type: Any) -> GenericAlias: ...

class PurePosixPath(PurePath): ...
class PureWindowsPath(PurePath): ...

class Path(PurePath):
    def __new__(cls, *args: StrPath, **kwargs: Any) -> Self: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
    @classmethod
    def cwd(cls) -> Self: ...
    if sys.version_info >= (3, 10):
        def stat(self, *, follow_symlinks: bool = True) -> stat_result: ...
        def chmod(self, mode: int, *, follow_symlinks: bool = True) -> None: ...
    else:
        def stat(self) -> stat_result: ...
        def chmod(self, mode: int) -> None: ...

    def exists(self) -> bool: ...
    def glob(self, pattern: str) -> Generator[Self, None, None]: ...
    def is_dir(self) -> bool: ...
    def is_file(self) -> bool: ...
    def is_symlink(self) -> bool: ...
    def is_socket(self) -> bool: ...
    def is_fifo(self) -> bool: ...
    def is_block_device(self) -> bool: ...
    def is_char_device(self) -> bool: ...
    def iterdir(self) -> Generator[Self, None, None]: ...
    def lchmod(self, mode: int) -> None: ...
    def lstat(self) -> stat_result: ...
    def mkdir(self, mode: int = 0o777, parents: bool = False, exist_ok: bool = False) -> None: ...
    # Adapted from builtins.open
    # Text mode: always returns a TextIOWrapper
    # The Traversable .open in stdlib/importlib/abc.pyi should be kept in sync with this.
    @overload
    def open(
        self,
        mode: OpenTextMode = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
    ) -> TextIOWrapper: ...
    # Unbuffered binary mode: returns a FileIO
    @overload
    def open(
        self, mode: OpenBinaryMode, buffering: Literal[0], encoding: None = None, errors: None = None, newline: None = None
    ) -> FileIO: ...
    # Buffering is on: return BufferedRandom, BufferedReader, or BufferedWriter
    @overload
    def open(
        self,
        mode: OpenBinaryModeUpdating,
        buffering: Literal[-1, 1] = -1,
        encoding: None = None,
        errors: None = None,
        newline: None = None,
    ) -> BufferedRandom: ...
    @overload
    def open(
        self,
        mode: OpenBinaryModeWriting,
        buffering: Literal[-1, 1] = -1,
        encoding: None = None,
        errors: None = None,
        newline: None = None,
    ) -> BufferedWriter: ...
    @overload
    def open(
        self,
        mode: OpenBinaryModeReading,
        buffering: Literal[-1, 1] = -1,
        encoding: None = None,
        errors: None = None,
        newline: None = None,
    ) -> BufferedReader: ...
    # Buffering cannot be determined: fall back to BinaryIO
    @overload
    def open(
        self, mode: OpenBinaryMode, buffering: int = -1, encoding: None = None, errors: None = None, newline: None = None
    ) -> BinaryIO: ...
    # Fallback if mode is not specified
    @overload
    def open(
        self, mode: str, buffering: int = -1, encoding: str | None = None, errors: str | None = None, newline: str | None = None
    ) -> IO[Any]: ...
    if sys.platform != "win32":
        # These methods do "exist" on Windows, but they always raise NotImplementedError,
        # so it's safer to pretend they don't exist
        def owner(self) -> str: ...
        def group(self) -> str: ...

    # This methods does "exist" on Windows, but always raises NotImplementedError on <3.12
    if sys.platform != "win32" or sys.version_info >= (3, 12):
        def is_mount(self) -> bool: ...

    if sys.version_info >= (3, 9):
        def readlink(self) -> Self: ...
    if sys.version_info >= (3, 8):
        def rename(self, target: str | PurePath) -> Self: ...
        def replace(self, target: str | PurePath) -> Self: ...
    else:
        def rename(self, target: str | PurePath) -> None: ...
        def replace(self, target: str | PurePath) -> None: ...

    def resolve(self, strict: bool = False) -> Self: ...
    def rglob(self, pattern: str) -> Generator[Self, None, None]: ...
    def rmdir(self) -> None: ...
    def symlink_to(self, target: StrOrBytesPath, target_is_directory: bool = False) -> None: ...
    if sys.version_info >= (3, 10):
        def hardlink_to(self, target: StrOrBytesPath) -> None: ...

    def touch(self, mode: int = 0o666, exist_ok: bool = True) -> None: ...
    if sys.version_info >= (3, 8):
        def unlink(self, missing_ok: bool = False) -> None: ...
    else:
        def unlink(self) -> None: ...

    @classmethod
    def home(cls) -> Self: ...
    def absolute(self) -> Self: ...
    def expanduser(self) -> Self: ...
    def read_bytes(self) -> bytes: ...
    def read_text(self, encoding: str | None = None, errors: str | None = None) -> str: ...
    def samefile(self, other_path: StrPath) -> bool: ...
    def write_bytes(self, data: ReadableBuffer) -> int: ...
    if sys.version_info >= (3, 10):
        def write_text(
            self, data: str, encoding: str | None = None, errors: str | None = None, newline: str | None = None
        ) -> int: ...
    else:
        def write_text(self, data: str, encoding: str | None = None, errors: str | None = None) -> int: ...
    if sys.version_info >= (3, 8) and sys.version_info < (3, 12):
        def link_to(self, target: StrOrBytesPath) -> None: ...
    if sys.version_info >= (3, 12):
        def walk(
            self, top_down: bool = ..., on_error: Callable[[OSError], object] | None = ..., follow_symlinks: bool = ...
        ) -> Iterator[tuple[Self, list[str], list[str]]]: ...

class PosixPath(Path, PurePosixPath): ...
class WindowsPath(Path, PureWindowsPath): ...
