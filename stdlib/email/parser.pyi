from collections.abc import Callable
from email.feedparser import BytesFeedParser as BytesFeedParser, FeedParser as FeedParser
from email.message import Message
from email.policy import Policy
from typing import BinaryIO, TextIO

__all__ = ["Parser", "HeaderParser", "BytesParser", "BytesHeaderParser", "FeedParser", "BytesFeedParser"]

class Parser:
    def __init__(self, _class: Callable[[], Message] | None = ..., *, policy: Policy = ...) -> None: ...
    def parse(self, fp: TextIO, headersonly: bool = ...) -> Message: ...
    def parsestr(self, text: str, headersonly: bool = ...) -> Message: ...

class HeaderParser(Parser): ...

class BytesParser:
    def __init__(self, _class: Callable[[], Message] = ..., *, policy: Policy = ...) -> None: ...
    def parse(self, fp: BinaryIO, headersonly: bool = ...) -> Message: ...
    def parsebytes(self, text: bytes, headersonly: bool = ...) -> Message: ...

class BytesHeaderParser(BytesParser): ...
