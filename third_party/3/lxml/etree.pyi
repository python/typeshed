# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

import typing
from typing import Any, Dict, List, MutableMapping, Tuple, Union, Optional
from typing import Iterable, Iterator, SupportsBytes


# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
_AnyStr = Union[str, bytes]
_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]


class _ElementMatchIterator(Iterator['_Element']):
    def __iter__(self) -> '_ElementMatchIterator': ...
    def __next__(self) -> '_Element': ...

class ElementChildIterator(_ElementMatchIterator):
    def __iter__(self) -> 'ElementChildIterator': ...

class AncestorsIterator(_ElementMatchIterator):
    def __iter__(self) -> 'AncestorsIterator': ...

class SiblingsIterator(_ElementMatchIterator):
    def __iter__(self) -> 'SiblingsIterator': ...

class ElementDepthFirstIterator(Iterator['_Element']):
    def __iter__(self) -> 'ElementDepthFirstIterator': ...
    def __next__(self) -> '_Element': ...

class ElementTextIterator(Iterator[str]):
    def __iter__(self) -> 'ElementTextIterator': ...
    def __next__(self) -> str: ...

class _Element(Iterable['_Element']):
    # Docs: http://lxml.de/api/lxml.etree._Element-class.html
    def addprevious(self, element: '_Element') -> None: ...
    def addnext(self, element: '_Element') -> None: ...
    def clear(self) -> None: ...
    # Attributes
    def get(self, key: _AnyStr, default: Optional[_AnyStr] = ...) -> _AnyStr: ...
    def set(self, key: str, value: str) -> None: ...
    def xpath(self, _path: _AnyStr, namespaces: Optional[_DictAnyStr] = ..., extensions: Any = ..., smart_strings: bool = ..., **_variables: Any) -> Any: ...
    # indeed returns a Union[bool, float, _AnyStr, List[Union[ElementBase, _AnyStr, Tuple[]]]]: ...
    # http://lxml.de/xpathxslt.html#xpath-return-values
    attrib = ...  # type: MutableMapping[str, str]
    text = ...  # type: _AnyStr
    tag = ...  # type: str
    def append(self, element: '_Element') -> '_Element': ...

    # Iterators
    def __iter__(self) -> ElementChildIterator: ...
    def iter(self, 
        tag: Optional[Union[str, _Element]]=..., 
        *tags: Any) -> ElementDepthFirstIterator: ...
    def iterancestors(self, 
        tag: Optional[Union[str, _Element]]=..., 
        *tags: Any) -> AncestorsIterator: ...
    def iterchildren(self, 
        tag: Optional[Union[str, _Element]]=..., 
        reversed=False, 
        *tags: Any) -> ElementChildIterator: ...
    def iterdescendants(self, 
        tag: Optional[Union[str, _Element]]=..., 
        *tags: Any) -> ElementDepthFirstIterator: ...
    def itersiblings(self, 
        tag: Optional[Union[str, _Element]]=..., 
        preceding=False, 
        *tags: Any) -> SiblingsIterator: ...
    def itertext(self, 
        tag: Optional[Union[str, _Element]]=..., 
        with_tail=True, 
        *tags: Any) -> ElementTextIterator: ...


class ElementBase(_Element): ...

class _ElementTree:
    def write(self,
              file: Union[_AnyStr, typing.IO],
              encoding: _AnyStr = ...,
              method: _AnyStr = ...,
              pretty_print: bool = ...,
              xml_declaration: Any = ...,
              with_tail: Any = ...,
              standalone: bool = ...,
              compression: int = ...,
              exclusive: bool = ...,
              with_comments: bool = ...,
              inclusive_ns_prefixes: _ListAnyStr = ...) -> None: ...
    def xpath(self, _path: _AnyStr, namespaces: Optional[_DictAnyStr] = ..., extensions: Any = ..., smart_strings: bool = ..., **_variables: Any) -> Any: ...

class _XSLTResultTree(SupportsBytes): ...

class _XSLTQuotedStringParam: ...

class XMLParser: ...

class XMLSchema:
    def __init__(self,
                 etree: Union[_Element, _ElementTree] = ...,
                 file: Union[_AnyStr, typing.IO] = ...) -> None: ...
    def assertValid(self, etree: Union[_Element, _ElementTree]) -> None: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(self,
                 xslt_input: Union[_Element, _ElementTree],
                 extensions: _Dict_Tuple2AnyStr_Any = ...,
                 regexp: bool = ...,
                 access_control: XSLTAccessControl = ...) -> None: ...
    def __call__(self,
                 _input: Union[_Element, _ElementTree],
                 profile_run: bool = ...,
                 **kwargs: Union[_AnyStr, _XSLTQuotedStringParam]) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...

def Element(_tag: _AnyStr,
            attrib: _DictAnyStr = ...,
            nsmap: _DictAnyStr = ...,
            **extra: _AnyStr) -> _Element: ...
def SubElement(_parent: _Element, _tag: _AnyStr,
               attrib: _DictAnyStr = ...,
               nsmap: _DictAnyStr = ...,
               **extra: _AnyStr) -> _Element: ...
def ElementTree(element: _Element = ...,
                file: Union[_AnyStr, typing.IO] = ...,
                parser: XMLParser = ...) -> _ElementTree: ...
def ProcessingInstruction(target: _AnyStr, text: _AnyStr = ...) -> _Element: ...
def parse(source: Union[_AnyStr, typing.IO],
          parser: XMLParser = ...,
          base_url: _AnyStr = ...) -> _ElementTree: ...
def fromstring(text: _AnyStr,
               parser: XMLParser = ...,
               *,
               base_url: _AnyStr = ...) -> _Element: ...
def tostring(element_or_tree: Union[_Element, _ElementTree],
             encoding: Union[str, type] = ...,
             method: str = ...,
             xml_declaration: bool = ...,
             pretty_print: bool = ...,
             with_tail: bool = ...,
             standalone: bool = ...,
             doctype: str = ...,
             exclusive: bool = ...,
             with_comments: bool = ...,
             inclusive_ns_prefixes: Any = ...) -> _AnyStr: ...

class _ErrorLog: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _ErrorLog = ...) -> None: ...
    error_log = ...  # type: _ErrorLog

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...
class ParseError(LxmlSyntaxError): ...
class XMLSyntaxError(ParseError): ...

class _Validator: ...

class DTD(_Validator):
    def __init__(self,
                 file: Union[_AnyStr, typing.IO] = ...,
                 *,
                 external_id: Any = ...) -> None: ...

    def assertValid(self, etree: _Element) -> None: ...
