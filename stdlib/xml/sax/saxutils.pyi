from _typeshed import SupportsWrite
from codecs import StreamReaderWriter, StreamWriter
from collections.abc import Mapping
from io import RawIOBase, TextIOBase
from xml.sax import _Source, handler, xmlreader

def escape(data: str, entities: Mapping[str, str] = {}) -> str: ...
def unescape(data: str, entities: Mapping[str, str] = {}) -> str: ...
def quoteattr(data: str, entities: Mapping[str, str] = {}) -> str: ...

class XMLGenerator(handler.ContentHandler):
    def __init__(
        self,
        out: TextIOBase | RawIOBase | StreamWriter | StreamReaderWriter | SupportsWrite[bytes] | None = None,
        encoding: str = "iso-8859-1",
        short_empty_elements: bool = False,
    ) -> None: ...
    def startDocument(self) -> None: ...
    def endDocument(self) -> None: ...
    def startPrefixMapping(self, prefix: str | None, uri: str) -> None: ...
    def endPrefixMapping(self, prefix: str | None) -> None: ...
    def startElement(self, name: str, attrs: xmlreader.AttributesImpl) -> None: ...
    def endElement(self, name: str) -> None: ...
    def startElementNS(self, name: tuple[str, str], qname: str, attrs: xmlreader.AttributesNSImpl) -> None: ...
    def endElementNS(self, name: tuple[str, str], qname: str) -> None: ...
    def characters(self, content: str) -> None: ...
    def ignorableWhitespace(self, content: str) -> None: ...
    def processingInstruction(self, target: str, data: str) -> None: ...

class XMLFilterBase(xmlreader.XMLReader):
    def __init__(self, parent: xmlreader.XMLReader | None = None) -> None: ...
    def error(self, exception): ...
    def fatalError(self, exception): ...
    def warning(self, exception): ...
    def setDocumentLocator(self, locator: xmlreader.Locator) -> None: ...
    def startDocument(self) -> None: ...
    def endDocument(self) -> None: ...
    def startPrefixMapping(self, prefix: str | None, uri: str) -> None: ...
    def endPrefixMapping(self, prefix: str | None) -> None: ...
    def startElement(self, name: str, attrs: xmlreader.AttributesImpl) -> None: ...
    def endElement(self, name: str) -> None: ...
    def startElementNS(self, name: tuple[str, str], qname: str, attrs: xmlreader.AttributesNSImpl) -> None: ...
    def endElementNS(self, name: tuple[str, str], qname: str) -> None: ...
    def characters(self, content: str) -> None: ...
    def ignorableWhitespace(self, chars: str) -> None: ...
    def processingInstruction(self, target: str, data: str) -> None: ...
    def skippedEntity(self, name: str) -> None: ...
    def notationDecl(self, name, publicId, systemId): ...
    def unparsedEntityDecl(self, name, publicId, systemId, ndata): ...
    def resolveEntity(self, publicId, systemId): ...
    def parse(self, source: _Source) -> None: ...
    def setLocale(self, locale): ...
    def getFeature(self, name: str) -> object: ...
    def setFeature(self, name: str, state: object) -> None: ...
    def getProperty(self, name: str) -> object: ...
    def setProperty(self, name: str, value: object) -> None: ...
    def getParent(self) -> xmlreader.XMLReader: ...
    def setParent(self, parent: xmlreader.XMLReader) -> None: ...

def prepare_input_source(source, base=""): ...
