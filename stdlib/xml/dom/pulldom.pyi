import xml.sax.handler
from typing import Any, BytesIO, Optional

START_ELEMENT: str
END_ELEMENT: str
COMMENT: str
START_DOCUMENT: str
END_DOCUMENT: str
PROCESSING_INSTRUCTION: str
IGNORABLE_WHITESPACE: str
CHARACTERS: str

class PullDOM(xml.sax.ContentHandler):
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

def parse(stream_or_string: str | BytesIO, parser: Optional[XMLReader] = ..., bufsize: Optional[int] = ...) -> DOMEventStream: ...
def parseString(string: str, parser: Optional[XMLReader] = ...) -> DOMEventStream: ...
