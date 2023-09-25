from _typeshed import SupportsRead
from collections.abc import Callable
from email.feedparser import BytesFeedParser as BytesFeedParser, FeedParser as FeedParser
from email.message import Message
from email.policy import Policy
from typing import IO

__all__ = ["Parser", "HeaderParser", "BytesParser", "BytesHeaderParser", "FeedParser", "BytesFeedParser"]

class Parser:
    def __init__(self, _class: Callable[[], Message] | None = None, *, policy: Policy[Message] = ...) -> None: ...
    def parse(self, fp: SupportsRead[str], headersonly: bool = False) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = False) -> Message: ...

class HeaderParser(Parser):
    def parse(self, fp: SupportsRead[str], headersonly: bool = True) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = True) -> Message: ...

class BytesParser:
    def __init__(self, _class: Callable[[], Message] = ..., *, policy: Policy[Message] = ...) -> None: ...
    def parse(self, fp: IO[bytes], headersonly: bool = False) -> Message: ...
    def parsebytes(self, text: bytes | bytearray, headersonly: bool = False) -> Message: ...

class BytesHeaderParser(BytesParser):
    def parse(self, fp: IO[bytes], headersonly: bool = True) -> Message: ...
    def parsebytes(self, text: bytes | bytearray, headersonly: bool = True) -> Message: ...
