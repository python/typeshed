from _io import BufferedReader, BufferedRWPair, BufferedWriter
from gzip import GzipFile
from io import BufferedRandom, BytesIO, FileIO, RawIOBase, TextIOWrapper
from socket import SocketIO
from typing import Any
from typing_extensions import assert_type

socket: Any = None

BufferedReader(RawIOBase())
BufferedWriter(RawIOBase())
BufferedWriter(SocketIO(socket, "r"))

BufferedRWPair(open("", "rb"), open("", "wb"))

assert_type(TextIOWrapper(FileIO("")).buffer, FileIO)
assert_type(TextIOWrapper(FileIO(13)).detach(), FileIO)
assert_type(TextIOWrapper(GzipFile("")).buffer, GzipFile)


class Index:
    def __index__(self) -> int:
        return 1


assert_type(FileIO("").seek(Index()), int)
assert_type(BufferedReader(BytesIO()).seek(Index()), int)
assert_type(BufferedWriter(BytesIO()).seek(Index()), int)
assert_type(BufferedRandom(FileIO("")).seek(Index()), int)
FileIO("").seek("1")  # type: ignore[arg-type]


class NarrowBytesIO(BytesIO):
    def seek(self, pos: int, whence: int = 0, /) -> int:
        return super().seek(pos, whence)


assert_type(NarrowBytesIO().seek(1), int)
