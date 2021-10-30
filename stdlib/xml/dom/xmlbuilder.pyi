from typing import Any, BinaryIO, NoReturn, Optional
from typing_extensions import Literal
from urllib.request import OpenerDirector
from xml.dom.expatbuilder import ExpatBuilder, ExpatBuilderNS
from xml.dom.minidom import Node

# UNKNOWN TYPES:
# - `Options.errorHandler`.
#       The same as `_DOMBuilderErrorHandlerType`?
#       Maybe `xml.sax.handler.ErrorHandler`?
# - Return type of DOMBuilder.getFeature().
#       We could get rid of the `Any` if we knew more
#       about `Options.errorHandler`.

# ALIASES REPRESENTING MORE UNKNOWN TYPES:

# probably the same as `Options.errorHandler`?
# Maybe `xml.sax.handler.ErrorHandler`?
_DOMBuilderErrorHandlerType = Optional[Any]
# probably some kind of IO...
_DOMInputSourceCharacterStreamType = Optional[Any]
# probably a string??
_DOMInputSourceStringDataType = Optional[Any]
# probably a string??
_DOMInputSourceEncodingType = Optional[Any]

class Options:
    namespaces: int
    namespace_declarations: bool
    validation: bool
    external_parameter_entities: bool
    external_general_entities: bool
    external_dtd_subset: bool
    validate_if_schema: bool
    validate: bool
    datatype_normalization: bool
    create_entity_ref_nodes: bool
    entities: bool
    whitespace_in_element_content: bool
    cdata_sections: bool
    comments: bool
    charset_overrides_xml_encoding: bool
    infoset: bool
    supported_mediatypes_only: bool
    errorHandler: Any | None
    filter: DOMBuilderFilter | None  # a guess, but seems likely

class DOMBuilder:
    entityResolver: DOMEntityResolver | None  # a guess, but seems likely
    errorHandler: _DOMBuilderErrorHandlerType
    filter: DOMBuilderFilter | None  # a guess, but seems likely
    ACTION_REPLACE: Literal[1]
    ACTION_APPEND_AS_CHILDREN: Literal[2]
    ACTION_INSERT_AFTER: Literal[3]
    ACTION_INSERT_BEFORE: Literal[4]
    _legal_actions: tuple[Literal[1], Literal[2], Literal[3], Literal[4]]
    def __init__(self) -> None: ...
    _options: Options
    def _get_entityResolver(self) -> DOMEntityResolver | None: ...  # a guess, but seems likely
    def _set_entityResolver(self, entityResolver: DOMEntityResolver | None) -> None: ...  # a guess, but seems likely
    def _get_errorHandler(self) -> _DOMBuilderErrorHandlerType: ...
    def _set_errorHandler(self, errorHandler: _DOMBuilderErrorHandlerType) -> None: ...
    def _get_filter(self) -> DOMBuilderFilter | None: ...  # a guess, but seems likely
    def _set_filter(self, filter: DOMBuilderFilter | None) -> None: ...  # a guess, but seems likely
    def setFeature(self, name: str, state: int) -> None: ...
    def supportsFeature(self, name: str) -> bool: ...
    def canSetFeature(self, name: str, state: int) -> bool: ...
    _settings: dict[tuple[str, int], list[tuple[str, int]]]
    # getFeature could return any attribute from an instance of `Options`
    def getFeature(self, name: str) -> int | bool | None | Any: ...
    def parseURI(self, uri: str) -> ExpatBuilder | ExpatBuilderNS: ...
    def parse(self, input: DOMInputSource) -> ExpatBuilder | ExpatBuilderNS: ...
    # `input` and `cnode` argtypes for `parseWithContext` are unknowable
    # as the function does nothing with them, and always raises an exception.
    # But `input` is *probably* `DOMInputSource`?
    def parseWithContext(self, input: object, cnode: object, action: Literal[1, 2, 3, 4]) -> NoReturn: ...
    def _parse_bytestream(self, stream: BinaryIO, options: Options) -> ExpatBuilder | ExpatBuilderNS: ...

def _name_xform(name: str) -> str: ...

class DOMEntityResolver:
    _opener: OpenerDirector
    def resolveEntity(self, publicId: str | None, systemId: str) -> DOMInputSource: ...
    def _get_opener(self) -> OpenerDirector: ...
    def _create_opener(self) -> OpenerDirector: ...
    def _guess_media_encoding(self, source: DOMInputSource) -> str: ...

class DOMInputSource:
    byteStream: OpenerDirector | None
    characterStream: _DOMInputSourceCharacterStreamType
    stringData: _DOMInputSourceStringDataType
    encoding: _DOMInputSourceEncodingType
    publicId: str | None
    systemId: str | None
    baseURI: str | None
    def _get_byteStream(self) -> OpenerDirector | None: ...
    def _set_byteStream(self, byteStream: OpenerDirector | None) -> None: ...
    def _get_characterStream(self) -> _DOMInputSourceCharacterStreamType: ...
    def _set_characterStream(self, characterStream: _DOMInputSourceCharacterStreamType) -> None: ...
    def _get_stringData(self) -> _DOMInputSourceStringDataType: ...
    def _set_stringData(self, data: _DOMInputSourceStringDataType) -> None: ...
    def _get_encoding(self) -> _DOMInputSourceEncodingType: ...
    def _set_encoding(self, encoding: _DOMInputSourceEncodingType) -> None: ...
    def _get_publicId(self) -> str | None: ...
    def _set_publicId(self, publicId: str | None) -> None: ...
    def _get_systemId(self) -> str | None: ...
    def _set_systemId(self, systemId: str | None) -> None: ...
    def _get_baseURI(self) -> str | None: ...
    def _set_baseURI(self, uri: str | None) -> None: ...

class DOMBuilderFilter:
    FILTER_ACCEPT: Literal[1]
    FILTER_REJECT: Literal[2]
    FILTER_SKIP: Literal[3]
    FILTER_INTERRUPT: Literal[4]
    whatToShow: int
    def _get_whatToShow(self) -> int: ...
    # The argtypes for acceptNode and startContainer appear to be irrelevant.
    def acceptNode(self, element: object) -> Literal[1]: ...
    def startContainer(self, element: object) -> Literal[1]: ...

class DocumentLS:
    async_: bool
    def _get_async(self) -> Literal[False]: ...
    # The only requirements on the `flag` argument
    # are that it can safely be passed to `bool()`.
    def _set_async(self, flag: object) -> None: ...
    def abort(self) -> NoReturn: ...
    # `load()` and `loadXML()` always raise exceptions
    # so the argtypes of `uri` and `source` are unknowable.
    # `source` is *probably* `DOMInputSource`?
    # `uri` is *probably* a str? (see DOMBuilder.parseURI())
    def load(self, uri: object) -> NoReturn: ...
    def loadXML(self, source: object) -> NoReturn: ...
    def saveXML(self, snode: Node | None) -> str: ...

class DOMImplementationLS:
    MODE_SYNCHRONOUS: Literal[1]
    MODE_ASYNCHRONOUS: Literal[2]
    def createDOMBuilder(self, mode: Literal[1], schemaType: None) -> DOMBuilder: ...
    def createDOMWriter(self) -> NoReturn: ...
    def createDOMInputSource(self) -> DOMInputSource: ...
