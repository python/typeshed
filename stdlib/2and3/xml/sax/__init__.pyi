from typing import Any, List, NoReturn, Optional, Text, Union, IO

import xml.sax
from xml.sax.xmlreader import InputSource, Locator
from xml.sax.handler import ContentHandler, ErrorHandler

class SAXException(Exception):
    def __init__(self, msg: str, exception: Optional[Exception] = ...) -> None: ...
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

default_parser_list = ...  # type: List[str]

def make_parser(parser_list: List[str] = ...) -> xml.sax.xmlreader.XMLReader: ...

def parse(source: Union[str, IO[str]], handler: xml.sax.handler.ContentHandler,
          errorHandler: xml.sax.handler.ErrorHandler = ...) -> None: ...

def parseString(string: Union[bytes, Text], handler: xml.sax.handler.ContentHandler,
                errorHandler: Optional[xml.sax.handler.ErrorHandler] = ...) -> None: ...

def _create_parser(parser_name: str) -> xml.sax.xmlreader.XMLReader: ...
