from typing import IO, Any, List, NoReturn, Text
from xml.sax.handler import ContentHandler, ErrorHandler
from xml.sax.xmlreader import Locator, XMLReader

class SAXException(Exception):
    def __init__(self, msg: str, exception: Exception | None = ...) -> None: ...
    def getMessage(self) -> str: ...
    def getException(self) -> Exception: ...
    def __getitem__(self, ix: Any) -> NoReturn: ...

class SAXParseException(SAXException):
    def __init__(self, msg: str, exception: Exception, locator: Locator) -> None: ...
    def getColumnNumber(self) -> int: ...
    def getLineNumber(self) -> int: ...
    def getPublicId(self): ...
    def getSystemId(self): ...

class SAXNotRecognizedException(SAXException): ...
class SAXNotSupportedException(SAXException): ...
class SAXReaderNotAvailable(SAXNotSupportedException): ...

default_parser_list: List[str]

def make_parser(parser_list: List[str] = ...) -> XMLReader: ...
def parse(source: str | IO[str] | IO[bytes], handler: ContentHandler, errorHandler: ErrorHandler = ...) -> None: ...
def parseString(string: bytes | Text, handler: ContentHandler, errorHandler: ErrorHandler | None = ...) -> None: ...
def _create_parser(parser_name: str) -> XMLReader: ...
