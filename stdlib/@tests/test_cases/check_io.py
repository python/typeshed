from _io import BufferedReader
from gzip import GzipFile
from io import FileIO, RawIOBase, TextIOWrapper
from typing_extensions import assert_type

BufferedReader(RawIOBase())

assert_type(TextIOWrapper(FileIO("")).buffer, FileIO)
assert_type(TextIOWrapper(FileIO(13)).detach(), FileIO)
assert_type(TextIOWrapper(GzipFile("")).buffer, GzipFile)


# def read(self, n: int = ..., /) -> bytes: ...
# def readinto(self, b: memoryview, /) -> int: ...
## def seek(self, pos: int, whence: int, /) -> int: ...
## def tell(self) -> int: ...
## def truncate(self, size: int, /) -> int: ...
## def flush(self) -> object: ...
## def close(self) -> object: ...
## def readable(self) -> bool: ...
## def seekable(self) -> bool: ...
## @property
## def closed(self) -> bool: ...
# @property
# def name(self) -> Any: ...  # Type is inconsistent between the various I/O types.
# @property
# def mode(self) -> str: ...
## def fileno(self) -> int: ...
## def isatty(self) -> bool: ...


# class _RawIOBase(_IOBase):
#     # def close(self) -> None: ...
#     # def fileno(self) -> int: ...
#     # def flush(self) -> None: ...
#     # def isatty(self) -> bool: ...
#     # def readable(self) -> bool: ...
#     read: Callable[..., Any]
#     # def seek(self, offset: int, whence: int = 0, /) -> int: ...
#     # def seekable(self) -> bool: ...
#     # def tell(self) -> int: ...
#     # def truncate(self, size: int | None = None, /) -> int: ...
#     # @property
#     # def closed(self) -> bool: ...
#     # The following methods can return None if the file is in non-blocking mode
#     # and no data is available.
#     def readinto(self, buffer: WriteableBuffer, /) -> int | MaybeNone: ...
#     def read(self, size: int = -1, /) -> bytes | MaybeNone: ...
