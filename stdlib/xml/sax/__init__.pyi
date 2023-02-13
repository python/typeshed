import sys
from _typeshed import ReadableBuffer, StrPath, SupportsRead, _T_co
from collections.abc import Iterable
from typing import Any, NoReturn, Protocol
from xml.sax.handler import ContentHandler as ContentHandler, ErrorHandler as ErrorHandler
from xml.sax.xmlreader import Locator, XMLReader

class _SupportsReadClose(SupportsRead[_T_co], Protocol[_T_co]):
    def close(self) -> None: ...

class SAXException(Exception):
    def __init__(self, msg: str, exception: Exception | None = None) -> None: ...
    def getMessage(self) -> str: ...
    def getException(self) -> Exception: ...
    def __getitem__(self, ix: Any) -> NoReturn: ...

class SAXParseException(SAXException):
    def __init__(self, msg: str, exception: Exception | None, locator: Locator) -> None: ...
    def getColumnNumber(self) -> int: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self): ...
    def getSystemId(self): ...

class SAXNotRecognizedException(SAXException): ...
class SAXNotSupportedException(SAXException): ...
class SAXReaderNotAvailable(SAXNotSupportedException): ...

default_parser_list: list[str]

if sys.version_info >= (3, 8):
    def make_parser(parser_list: Iterable[str] = ...) -> XMLReader: ...
    def parse(
        source: StrPath | _SupportsReadClose[bytes] | _SupportsReadClose[str],
        handler: ContentHandler,
        errorHandler: ErrorHandler = ...,
    ) -> None: ...

else:
    def make_parser(parser_list: list[str] = ...) -> XMLReader: ...
    def parse(
        source: str | _SupportsReadClose[bytes] | _SupportsReadClose[str],
        handler: ContentHandler,
        errorHandler: ErrorHandler = ...,
    ) -> None: ...


def parseString(string: ReadableBuffer | str, handler: ContentHandler, errorHandler: ErrorHandler | None = ...) -> None: ...
def _create_parser(parser_name: str) -> XMLReader: ...
