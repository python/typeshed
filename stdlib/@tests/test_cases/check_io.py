from _io import BufferedReader, BufferedRWPair, BufferedWriter
from gzip import GzipFile
from io import FileIO, RawIOBase, TextIOWrapper
from typing_extensions import assert_type

BufferedReader(RawIOBase())
BufferedWriter(RawIOBase())

BufferedRWPair(open("", "rb"), open("", "wb"))

assert_type(TextIOWrapper(FileIO("")).buffer, FileIO)
assert_type(TextIOWrapper(FileIO(13)).detach(), FileIO)
assert_type(TextIOWrapper(GzipFile("")).buffer, GzipFile)
