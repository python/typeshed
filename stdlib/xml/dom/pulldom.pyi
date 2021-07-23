from typing import Any, IO, Optional
from xml.sax.handler import ContentHandler
from xml.sax.xmlreader import XMLReader

START_ELEMENT: str
END_ELEMENT: str
COMMENT: str
START_DOCUMENT: str
END_DOCUMENT: str
PROCESSING_INSTRUCTION: str
IGNORABLE_WHITESPACE: str
CHARACTERS: str

class PullDOM(ContentHandler):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class ErrorHandler:
    def warning(self, exception) -> None: ...
    def error(self, exception) -> None: ...
    def fatalError(self, exception) -> None: ...

class DOMEventStream:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class SAX2DOM(PullDOM):
    def __getattr__(self, name: str) -> Any: ...  # incomplete

default_bufsize: int

def parse(stream_or_string: str | IO[bytes], parser: Optional[XMLReader] = ..., bufsize: Optional[int] = ...) -> DOMEventStream: ...
def parseString(string: str, parser: Optional[XMLReader] = ...) -> DOMEventStream: ...
