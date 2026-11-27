import threading
from _typeshed import Incomplete, ReadableBuffer, StrOrBytesPath, SupportsRead, Unused
from collections.abc import Iterable, Iterator
from typing import Any, Final, Literal, NoReturn, TypeAlias, overload, type_check_only

LXML3: bool
__origin__: Final = "lxml.etree"

# lxml lacks typeshed stubs
_LxmlElement: TypeAlias = Any
_LxmlElementTree: TypeAlias = Any
_LxmlXMLParser: TypeAlias = Any
_LxmlTag: TypeAlias = Any

@overload
def tostring(
    element_or_tree: _LxmlElement | _LxmlElementTree,
    *,
    encoding: None = None,
    method: Literal["xml", "html", "text", "c14n", "c14n2"] = "xml",
    xml_declaration: bool | None = None,
    pretty_print: bool = False,
    with_tail: bool = True,
    standalone: bool | None = None,
    doctype: str | bytes | None = None,
    exclusive: bool = False,
    inclusive_ns_prefixes: Iterable[str | bytes] | None = None,
    with_comments: bool = True,
    strip_text: bool = False,
) -> bytes: ...
@overload
def tostring(
    element_or_tree: _LxmlElement | _LxmlElementTree,
    *,
    encoding: Literal["unicode"] | type[str],
    method: Literal["xml", "html", "text", "c14n", "c14n2"] = "xml",
    xml_declaration: bool | None = None,
    pretty_print: bool = False,
    with_tail: bool = True,
    standalone: bool | None = None,
    doctype: str | bytes | None = None,
    exclusive: bool = False,
    inclusive_ns_prefixes: Iterable[str | bytes] | None = None,
    with_comments: bool = True,
    strip_text: bool = False,
) -> str: ...
@overload
def tostring(
    element_or_tree: _LxmlElement | _LxmlElementTree,
    *,
    encoding: str | bytes,
    method: Literal["xml", "html", "text", "c14n", "c14n2"] = "xml",
    xml_declaration: bool | None = None,
    pretty_print: bool = False,
    with_tail: bool = True,
    standalone: bool | None = None,
    doctype: str | bytes | None = None,
    exclusive: bool = False,
    inclusive_ns_prefixes: Iterable[str | bytes] | None = None,
    with_comments: bool = True,
    strip_text: bool = False,
) -> Any: ...

# Should be imported from lxml.etree.ElementBase, but lxml lacks types
@type_check_only
class _ElementBase: ...

class RestrictedElement(_ElementBase):
    __slots__ = ()
    blacklist: Incomplete
    def __iter__(self) -> Iterator[_LxmlElement]: ...
    def iterchildren(self, tag: _LxmlTag | None = None, reversed: bool = False) -> Iterator[_LxmlElement]: ...
    def iter(self, tag: _LxmlTag | None = None, *tags: _LxmlTag) -> Iterator[_LxmlElement]: ...
    def iterdescendants(self, tag: _LxmlTag | None = None, *tags: _LxmlTag) -> Iterator[_LxmlElement]: ...
    def itersiblings(self, tag: _LxmlTag | None = None, preceding: bool = False) -> Iterator[_LxmlElement]: ...
    def getchildren(self) -> list[_LxmlElement]: ...
    def getiterator(self, tag: _LxmlTag | None = None) -> Iterator[_LxmlElement]: ...

class GlobalParserTLS(threading.local):
    parser_config: dict[str, Any]
    element_class: type[_LxmlElement] | None
    def createDefaultParser(self) -> _LxmlXMLParser: ...
    def setDefaultParser(self, parser: _LxmlXMLParser) -> None: ...
    def getDefaultParser(self) -> _LxmlXMLParser: ...

def getDefaultParser() -> _LxmlXMLParser: ...
def check_docinfo(elementtree: _LxmlElementTree, forbid_dtd: bool = False, forbid_entities: bool = True) -> None: ...
def parse(
    source: StrOrBytesPath | SupportsRead[bytes | str],
    parser: _LxmlXMLParser | None = None,
    base_url: str | bytes | None = None,
    forbid_dtd: bool = False,
    forbid_entities: bool = True,
) -> _LxmlElementTree: ...
def fromstring(
    text: str | ReadableBuffer,
    parser: _LxmlXMLParser | None = None,
    base_url: str | bytes | None = None,
    forbid_dtd: bool = False,
    forbid_entities: bool = True,
) -> RestrictedElement | _LxmlElement: ...

XML = fromstring

def iterparse(*args: Unused, **kwargs: Unused) -> NoReturn: ...
