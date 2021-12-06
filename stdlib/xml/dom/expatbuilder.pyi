from typing import Any, NoReturn
from typing_extensions import Literal
from xml.dom.minidom import Document, DOMImplementation, Node, TypeInfo
from xml.dom.xmlbuilder import DOMBuilderFilter, Options

TEXT_NODE = Node.TEXT_NODE
CDATA_SECTION_NODE = Node.CDATA_SECTION_NODE
DOCUMENT_NODE = Node.DOCUMENT_NODE
FILTER_ACCEPT = DOMBuilderFilter.FILTER_ACCEPT
FILTER_REJECT = DOMBuilderFilter.FILTER_REJECT
FILTER_SKIP = DOMBuilderFilter.FILTER_SKIP
FILTER_INTERRUPT = DOMBuilderFilter.FILTER_INTERRUPT
theDOMImplementation: DOMImplementation | None

class ElementInfo:
    tagName: Any
    def __init__(self, tagName, model: Any | None = ...) -> None: ...
    def getAttributeType(self, aname) -> TypeInfo: ...
    def getAttributeTypeNS(self, namespaceURI, localName) -> TypeInfo: ...
    def isElementContent(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isId(self, aname) -> bool: ...
    def isIdNS(self, euri, ename, auri, aname) -> bool: ...

class ExpatBuilder:
    doc: Document
    curnode: Document
    def __init__(self, options: Options | None = ...) -> None: ...
    def createParser(self) -> Any: ...
    def getParser(self) -> Any | None: ...
    def reset(self) -> None: ...
    def install(self, parser) -> None: ...
    def parseFile(self, file) -> Document: ...
    def parseString(self, string: str) -> Document: ...
    def start_doctype_decl_handler(self, doctypeName, systemId, publicId, has_internal_subset) -> None: ...
    def end_doctype_decl_handler(self) -> None: ...
    def pi_handler(self, target, data) -> None: ...
    def character_data_handler_cdata(self, data) -> None: ...
    def character_data_handler(self, data) -> None: ...
    def start_cdata_section_handler(self) -> None: ...
    def end_cdata_section_handler(self) -> None: ...
    def entity_decl_handler(self, entityName, is_parameter_entity, value, base, systemId, publicId, notationName) -> None: ...
    def notation_decl_handler(self, notationName, base, systemId, publicId) -> None: ...
    def comment_handler(self, data) -> None: ...
    def external_entity_ref_handler(self, context, base, systemId, publicId) -> Literal[1]: ...
    def first_element_handler(self, name, attributes) -> None: ...
    def start_element_handler(self, name, attributes) -> None: ...
    def end_element_handler(self, name) -> None: ...
    def element_decl_handler(self, name, model) -> None: ...
    def attlist_decl_handler(self, elem, name, type, default, required) -> None: ...
    def xml_decl_handler(self, version, encoding, standalone) -> None: ...

_ALLOWED_FILTER_RETURN_TYPE = Literal[1, 2, 3]

class FilterVisibilityController:
    filter: DOMBuilderFilter
    def startContainer(self, node: Node) -> _ALLOWED_FILTER_RETURN_TYPE: ...
    def acceptNode(self, node: Node) -> _ALLOWED_FILTER_RETURN_TYPE: ...

class FilterCrutch:
    def __init__(self, builder) -> None: ...

class Rejecter(FilterCrutch):
    def start_element_handler(self, *args: Any) -> None: ...
    def end_element_handler(self, *args: Any) -> None: ...

class Skipper(FilterCrutch):
    def start_element_handler(self, *args: Any) -> None: ...
    def end_element_handler(self, *args: Any) -> None: ...

class FragmentBuilder(ExpatBuilder):
    fragment: Any | None
    originalDocument: Any
    context: Any
    def __init__(self, context, options: Options | None = ...) -> None: ...
    def external_entity_ref_handler(self, context, base, systemId, publicId) -> Literal[1, -1]: ...  # type: ignore[override]

class Namespaces:
    def createParser(self): ...
    def install(self, parser) -> None: ...
    def start_namespace_decl_hander(self, prefix, uri) -> None: ...
    def start_element_handler(self, name, attributes) -> None: ...

class ExpatBuilderNS(Namespaces, ExpatBuilder): ...
class FragmentBuilderNS(Namespaces, FragmentBuilder): ...
class ParseEscape(Exception): ...

class InternalSubsetExtractor(ExpatBuilder):
    subset: Any | None
    def getSubset(self) -> Any | None: ...
    def parseFile(self, file) -> None: ...  # type: ignore[override]
    def parseString(self, string: str) -> None: ...  # type: ignore[override]
    def end_doctype_decl_handler(self) -> NoReturn: ...
    def start_element_handler(self, name, attrs) -> NoReturn: ...

def parse(file, namespaces: bool = ...): ...
def parseString(string: str, namespaces: bool = ...): ...
def parseFragment(file, context, namespaces: bool = ...): ...
def parseFragmentString(string: str, context, namespaces: bool = ...): ...
def makeBuilder(options: Options) -> ExpatBuilderNS | ExpatBuilder: ...
