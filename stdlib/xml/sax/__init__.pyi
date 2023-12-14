import sys
from _typeshed import ReadableBuffer, StrPath, SupportsRead, _T_co
from collections.abc import Iterable
from typing import Protocol
from typing_extensions import TypeAlias
from xml.sax._exceptions import (
    SAXException as SAXException,
    SAXNotRecognizedException as SAXNotRecognizedException,
    SAXNotSupportedException as SAXNotSupportedException,
    SAXParseException as SAXParseException,
    SAXReaderNotAvailable as SAXReaderNotAvailable,
)
from xml.sax.handler import ContentHandler as ContentHandler, ErrorHandler as ErrorHandler
from xml.sax.xmlreader import XMLReader

class _SupportsReadClose(SupportsRead[_T_co], Protocol[_T_co]):
    def close(self) -> None: ...

if sys.version_info >= (3, 8):
    _Source: TypeAlias = StrPath | _SupportsReadClose[bytes] | _SupportsReadClose[str]
else:
    _Source: TypeAlias = str | _SupportsReadClose[bytes] | _SupportsReadClose[str]

default_parser_list: list[str]

if sys.version_info >= (3, 8):

    def make_parser(parser_list: Iterable[str] = ()) -> XMLReader: ...

else:

    def make_parser(parser_list: list[str] = []) -> XMLReader: ...

def parse(source: _Source, handler: ContentHandler, errorHandler: ErrorHandler = ...) -> None: ...
def parseString(string: ReadableBuffer | str, handler: ContentHandler, errorHandler: ErrorHandler | None = ...) -> None: ...
def _create_parser(parser_name: str) -> XMLReader: ...
