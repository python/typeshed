import sys
import xml.dom
from _typeshed import Incomplete, Self, SupportsRead
from typing_extensions import Literal
from xml.dom.xmlbuilder import DocumentLS, DOMImplementationLS
from xml.sax.xmlreader import XMLReader

def parse(file: str | SupportsRead[bytes] | SupportsRead[str], parser: XMLReader | None = ..., bufsize: int | None = ...): ...
def parseString(string: str | bytes, parser: XMLReader | None = ...): ...
def getDOMImplementation(features=...) -> DOMImplementation | None: ...

class Node(xml.dom.Node):
    namespaceURI: str | None
    parentNode: Incomplete
    ownerDocument: Incomplete
    nextSibling: Incomplete
    previousSibling: Incomplete
    prefix: Incomplete
    @property
    def firstChild(self) -> Node | None: ...
    @property
    def lastChild(self) -> Node | None: ...
    @property
    def localName(self) -> str | None: ...
    def __bool__(self) -> Literal[True]: ...
    if sys.version_info >= (3, 9):
        def toxml(self, encoding: Incomplete | None = ..., standalone: Incomplete | None = ...): ...
        def toprettyxml(
            self, indent: str = ..., newl: str = ..., encoding: Incomplete | None = ..., standalone: Incomplete | None = ...
        ): ...
    else:
        def toxml(self, encoding: Incomplete | None = ...): ...
        def toprettyxml(self, indent: str = ..., newl: str = ..., encoding: Incomplete | None = ...): ...

    def hasChildNodes(self) -> bool: ...
    def insertBefore(self, newChild, refChild): ...
    def appendChild(self, node): ...
    def replaceChild(self, newChild, oldChild): ...
    def removeChild(self, oldChild): ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep): ...
    def isSupported(self, feature, version): ...
    def isSameNode(self, other): ...
    def getInterface(self, feature): ...
    def getUserData(self, key): ...
    def setUserData(self, key, data, handler): ...
    childNodes: Incomplete
    def unlink(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, et, ev, tb) -> None: ...

class DocumentFragment(Node):
    nodeType: int
    nodeName: str
    nodeValue: Incomplete
    attributes: Incomplete
    parentNode: Incomplete
    childNodes: Incomplete
    def __init__(self) -> None: ...

class Attr(Node):
    name: str
    nodeType: int
    attributes: Incomplete
    specified: bool
    ownerElement: Incomplete
    namespaceURI: str | None
    childNodes: Incomplete
    nodeName: Incomplete
    nodeValue: str
    value: str
    prefix: Incomplete
    def __init__(
        self, qName: str, namespaceURI: str | None = ..., localName: Incomplete | None = ..., prefix: Incomplete | None = ...
    ) -> None: ...
    def unlink(self) -> None: ...
    @property
    def isId(self) -> bool: ...
    @property
    def schemaType(self): ...

class NamedNodeMap:
    def __init__(self, attrs, attrsNS, ownerElement) -> None: ...
    def item(self, index): ...
    def items(self): ...
    def itemsNS(self): ...
    def __contains__(self, key): ...
    def keys(self): ...
    def keysNS(self): ...
    def values(self): ...
    def get(self, name, value: Incomplete | None = ...): ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __getitem__(self, attname_or_tuple): ...
    def __setitem__(self, attname, value) -> None: ...
    def getNamedItem(self, name): ...
    def getNamedItemNS(self, namespaceURI: str, localName): ...
    def removeNamedItem(self, name): ...
    def removeNamedItemNS(self, namespaceURI: str, localName): ...
    def setNamedItem(self, node): ...
    def setNamedItemNS(self, node): ...
    def __delitem__(self, attname_or_tuple) -> None: ...
    @property
    def length(self) -> int: ...

AttributeList = NamedNodeMap

class TypeInfo:
    namespace: Incomplete
    name: Incomplete
    def __init__(self, namespace, name) -> None: ...

class Element(Node):
    nodeType: int
    nodeValue: Incomplete
    schemaType: Incomplete
    parentNode: Incomplete
    tagName: str
    nodeName: str
    prefix: Incomplete
    namespaceURI: str | None
    childNodes: Incomplete
    nextSibling: Incomplete
    def __init__(
        self, tagName, namespaceURI: str | None = ..., prefix: Incomplete | None = ..., localName: Incomplete | None = ...
    ) -> None: ...
    def unlink(self) -> None: ...
    def getAttribute(self, attname: str) -> str: ...
    def getAttributeNS(self, namespaceURI: str, localName): ...
    def setAttribute(self, attname: str, value: str) -> None: ...
    def setAttributeNS(self, namespaceURI: str, qualifiedName: str, value) -> None: ...
    def getAttributeNode(self, attrname: str): ...
    def getAttributeNodeNS(self, namespaceURI: str, localName): ...
    def setAttributeNode(self, attr): ...
    setAttributeNodeNS: Incomplete
    def removeAttribute(self, name: str) -> None: ...
    def removeAttributeNS(self, namespaceURI: str, localName) -> None: ...
    def removeAttributeNode(self, node): ...
    removeAttributeNodeNS: Incomplete
    def hasAttribute(self, name: str) -> bool: ...
    def hasAttributeNS(self, namespaceURI: str, localName) -> bool: ...
    def getElementsByTagName(self, name: str): ...
    def getElementsByTagNameNS(self, namespaceURI: str, localName): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...
    def hasAttributes(self) -> bool: ...
    def setIdAttribute(self, name) -> None: ...
    def setIdAttributeNS(self, namespaceURI: str, localName) -> None: ...
    def setIdAttributeNode(self, idAttr) -> None: ...
    @property
    def attributes(self) -> NamedNodeMap: ...

class Childless:
    attributes: Incomplete
    childNodes: Incomplete
    firstChild: Incomplete
    lastChild: Incomplete
    def appendChild(self, node) -> None: ...
    def hasChildNodes(self) -> bool: ...
    def insertBefore(self, newChild, refChild) -> None: ...
    def removeChild(self, oldChild) -> None: ...
    def normalize(self) -> None: ...
    def replaceChild(self, newChild, oldChild) -> None: ...

class ProcessingInstruction(Childless, Node):
    nodeType: int
    target: Incomplete
    data: Incomplete
    def __init__(self, target, data) -> None: ...
    nodeValue: Incomplete
    nodeName: Incomplete
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class CharacterData(Childless, Node):
    ownerDocument: Incomplete
    previousSibling: Incomplete
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    data: str
    nodeValue: Incomplete
    def substringData(self, offset: int, count: int) -> str: ...
    def appendData(self, arg: str) -> None: ...
    def insertData(self, offset: int, arg: str) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def replaceData(self, offset: int, count: int, arg: str) -> None: ...
    @property
    def length(self) -> int: ...

class Text(CharacterData):
    nodeType: int
    nodeName: str
    attributes: Incomplete
    data: Incomplete
    def splitText(self, offset): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...
    def replaceWholeText(self, content): ...
    @property
    def isWhitespaceInElementContent(self) -> bool: ...
    @property
    def wholeText(self) -> str: ...

class Comment(CharacterData):
    nodeType: int
    nodeName: str
    def __init__(self, data) -> None: ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class CDATASection(Text):
    nodeType: int
    nodeName: str
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class ReadOnlySequentialNamedNodeMap:
    def __init__(self, seq=...) -> None: ...
    def __len__(self): ...
    def getNamedItem(self, name): ...
    def getNamedItemNS(self, namespaceURI: str, localName): ...
    def __getitem__(self, name_or_tuple): ...
    def item(self, index): ...
    def removeNamedItem(self, name) -> None: ...
    def removeNamedItemNS(self, namespaceURI: str, localName) -> None: ...
    def setNamedItem(self, node) -> None: ...
    def setNamedItemNS(self, node) -> None: ...
    @property
    def length(self) -> int: ...

class Identified:
    publicId: Incomplete
    systemId: Incomplete

class DocumentType(Identified, Childless, Node):
    nodeType: int
    nodeValue: Incomplete
    name: Incomplete
    internalSubset: Incomplete
    entities: Incomplete
    notations: Incomplete
    nodeName: Incomplete
    def __init__(self, qualifiedName: str) -> None: ...
    def cloneNode(self, deep): ...
    def writexml(self, writer, indent: str = ..., addindent: str = ..., newl: str = ...) -> None: ...

class Entity(Identified, Node):
    attributes: Incomplete
    nodeType: int
    nodeValue: Incomplete
    actualEncoding: Incomplete
    encoding: Incomplete
    version: Incomplete
    nodeName: Incomplete
    notationName: Incomplete
    childNodes: Incomplete
    def __init__(self, name, publicId, systemId, notation) -> None: ...
    def appendChild(self, newChild) -> None: ...
    def insertBefore(self, newChild, refChild) -> None: ...
    def removeChild(self, oldChild) -> None: ...
    def replaceChild(self, newChild, oldChild) -> None: ...

class Notation(Identified, Childless, Node):
    nodeType: int
    nodeValue: Incomplete
    nodeName: Incomplete
    def __init__(self, name, publicId, systemId) -> None: ...

class DOMImplementation(DOMImplementationLS):
    def hasFeature(self, feature: str, version: str | None) -> bool: ...
    def createDocument(self, namespaceURI: str | None, qualifiedName: str | None, doctype: DocumentType | None) -> Document: ...
    def createDocumentType(self, qualifiedName: str | None, publicId: str, systemId: str) -> DocumentType: ...
    def getInterface(self: Self, feature: str) -> Self | None: ...

class ElementInfo:
    tagName: Incomplete
    def __init__(self, name) -> None: ...
    def getAttributeType(self, aname): ...
    def getAttributeTypeNS(self, namespaceURI: str, localName): ...
    def isElementContent(self): ...
    def isEmpty(self): ...
    def isId(self, aname): ...
    def isIdNS(self, namespaceURI: str, localName): ...

class Document(Node, DocumentLS):
    implementation: Incomplete
    nodeType: int
    nodeName: str
    nodeValue: Incomplete
    attributes: Incomplete
    parentNode: Incomplete
    previousSibling: Incomplete
    nextSibling: Incomplete
    actualEncoding: Incomplete
    encoding: Incomplete
    standalone: Incomplete
    version: Incomplete
    strictErrorChecking: bool
    errorHandler: Incomplete
    documentURI: Incomplete
    doctype: Incomplete
    childNodes: Incomplete
    def __init__(self) -> None: ...
    def appendChild(self, node): ...
    documentElement: Incomplete
    def removeChild(self, oldChild): ...
    def unlink(self) -> None: ...
    def cloneNode(self, deep): ...
    def createDocumentFragment(self): ...
    def createElement(self, tagName: str): ...
    def createTextNode(self, data): ...
    def createCDATASection(self, data): ...
    def createComment(self, data): ...
    def createProcessingInstruction(self, target, data): ...
    def createAttribute(self, qName) -> Attr: ...
    def createElementNS(self, namespaceURI: str, qualifiedName: str): ...
    def createAttributeNS(self, namespaceURI: str, qualifiedName: str) -> Attr: ...
    def getElementById(self, id): ...
    def getElementsByTagName(self, name: str): ...
    def getElementsByTagNameNS(self, namespaceURI: str, localName): ...
    def isSupported(self, feature, version): ...
    def importNode(self, node, deep): ...
    if sys.version_info >= (3, 9):
        def writexml(
            self,
            writer,
            indent: str = ...,
            addindent: str = ...,
            newl: str = ...,
            encoding: Incomplete | None = ...,
            standalone: Incomplete | None = ...,
        ) -> None: ...
    else:
        def writexml(
            self, writer, indent: str = ..., addindent: str = ..., newl: str = ..., encoding: Incomplete | None = ...
        ) -> None: ...

    def renameNode(self, n, namespaceURI: str, name): ...
