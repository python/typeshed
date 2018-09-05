# Stubs for xml.etree.ElementTree

from typing import Any, Callable, Dict, Generator, IO, ItemsView, Iterable, Iterator, KeysView, List, MutableSequence, Optional, overload, Sequence, Text, Tuple, TypeVar, Union
import io
import sys

VERSION = ...  # type: str

class ParseError(SyntaxError): ...

def iselement(element: Element) -> bool: ...

_T = TypeVar('_T')

# Type for parser inputs. Parser will accept any unicode/str/bytes and coerce,
# and this is true in py2 and py3 (even fromstringlist() in python3 can be
# called with a heterogeneous list)
_parser_input_type = Union[bytes, Text]

# Type for individual tag/attr/ns/text values in args to most functions.
# In py2, the library accepts str or unicode everywhere and coerces
# aggressively.
# In py3, bytes is not coerced to str and so use of bytes is probably an error,
# so we exclude it. (why? the parser never produces bytes when it parses XML,
# so e.g., element.get(b'name') will always return None for parsed XML, even if
# there is a 'name' attribute.)
_str_argument_type = Union[str, Text]

# Type for return values from individual tag/attr/text values and serialization
if sys.version_info >= (3,):
    # note: in python3, everything comes out as str, yay:
    _str_result_type = str
    # unfortunately, tostring and tostringlist can return either bytes or str
    # depending on the value of `encoding` parameter. Client code knows best:
    _tostring_result_type = Any
else:
    # in python2, if the tag/attribute/text wasn't decode-able as ascii, it
    # comes out as a unicode string; otherwise it comes out as str. (see
    # _fixtext function in the source). Client code knows best:
    _str_result_type = Any
    # On the bright side, tostring and tostringlist always return bytes:
    _tostring_result_type = bytes

class Element(MutableSequence[Element]):
    tag = ...  # type: _str_result_type
    attrib = ...  # type: Dict[_str_result_type, _str_result_type]
    text = ...  # type: Optional[_str_result_type]
    tail = ...  # type: Optional[_str_result_type]
    def __init__(self, tag: Union[_str_argument_type, Callable[..., Element]], attrib: Dict[_str_argument_type, _str_argument_type]=..., **extra: _str_argument_type) -> None: ...
    def append(self, subelement: Element) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> Element: ...
    def extend(self, elements: Iterable[Element]) -> None: ...
    def find(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> Optional[Element]: ...
    def findall(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> List[Element]: ...
    def findtext(self, path: _str_argument_type, default: _T=..., namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> Union[_T, _str_result_type]: ...
    def get(self, key: _str_argument_type, default: _T=...) -> Union[_str_result_type, _T]: ...
    def getchildren(self) -> List[Element]: ...
    def getiterator(self, tag: _str_argument_type=...) -> List[Element]: ...
    if sys.version_info >= (3, 2):
        def insert(self, index: int, subelement: Element) -> None: ...
    else:
        def insert(self, index: int, element: Element) -> None: ...
    def items(self) -> ItemsView[_str_result_type, _str_result_type]: ...
    def iter(self, tag: _str_argument_type=...) -> Generator[Element, None, None]: ...
    def iterfind(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> List[Element]: ...
    def itertext(self) -> Generator[_str_result_type, None, None]: ...
    def keys(self) -> KeysView[_str_result_type]: ...
    def makeelement(self, tag: _str_argument_type, attrib: Dict[_str_argument_type, _str_argument_type]) -> Element: ...
    def remove(self, subelement: Element) -> None: ...
    def set(self, key: _str_argument_type, value: _str_argument_type) -> None: ...
    def __bool__(self) -> bool: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    @overload
    def __getitem__(self, i: int) -> Element: ...
    @overload
    def __getitem__(self, s: slice) -> MutableSequence[Element]: ...
    def __len__(self) -> int: ...
    @overload
    def __setitem__(self, i: int, o: Element) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[Element]) -> None: ...


def SubElement(parent: Element, tag: _str_argument_type, attrib: Dict[_str_argument_type, _str_argument_type]=..., **extra: _str_argument_type) -> Element: ...
def Comment(text: _str_argument_type=...) -> Element: ...
def ProcessingInstruction(target: _str_argument_type, text: _str_argument_type=...) -> Element: ...

PI = ...  # type: Callable[..., Element]

class QName:
    text = ...  # type: str
    def __init__(self, text_or_uri: _str_argument_type, tag: _str_argument_type=...) -> None: ...


_file_or_filename = Union[str, bytes, int, IO[Any]]

class ElementTree:
    def __init__(self, element: Element=..., file: _file_or_filename=...) -> None: ...
    def getroot(self) -> Element: ...
    def parse(self, source: _file_or_filename, parser: XMLParser=...) -> Element: ...
    def iter(self, tag: _str_argument_type=...) -> Generator[Element, None, None]: ...
    def getiterator(self, tag: _str_argument_type=...) -> List[Element]: ...
    def find(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> Optional[Element]: ...
    def findtext(self, path: _str_argument_type, default: _T=..., namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> Union[_T, _str_result_type]: ...
    def findall(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> List[Element]: ...
    def iterfind(self, path: _str_argument_type, namespaces: Dict[_str_argument_type, _str_argument_type]=...) -> List[Element]: ...
    if sys.version_info >= (3, 4):
        def write(self, file_or_filename: _file_or_filename, encoding: str=..., xml_declaration: Optional[bool]=..., default_namespace: _str_argument_type=..., method: str=..., *, short_empty_elements: bool=...) -> None: ...
    else:
        def write(self, file_or_filename: _file_or_filename, encoding: str=..., xml_declaration: Optional[bool]=..., default_namespace: _str_argument_type=..., method: str=...) -> None: ...
    def write_c14n(self, file: _file_or_filename) -> None: ...

def register_namespace(prefix: _str_argument_type, uri: _str_argument_type) -> None: ...
if sys.version_info >= (3, 4):
    def tostring(element: Element, encoding: str=..., method: str=..., *, short_empty_elements: bool=...) -> _tostring_result_type: ...
    def tostringlist(element: Element, encoding: str=..., method: str=..., *, short_empty_elements: bool=...) -> List[_tostring_result_type]: ...
else:
    def tostring(element: Element, encoding: str=..., method: str=...) -> _tostring_result_type: ...
    def tostringlist(element: Element, encoding: str=..., method: str=...) -> List[_tostring_result_type]: ...
def dump(elem: Element) -> None: ...
def parse(source: _file_or_filename, parser: XMLParser=...) -> ElementTree: ...
def iterparse(source: _file_or_filename, events: Sequence[str]=..., parser: XMLParser=...) -> Iterator[Tuple[str, Any]]: ...

if sys.version_info >= (3, 4):
    class XMLPullParser:
        def __init__(self, events: Sequence[str]=..., *, _parser: XMLParser=...) -> None: ...
        def feed(self, data: bytes) -> None: ...
        def close(self) -> None: ...
        def read_events(self) -> Iterator[Tuple[str, Element]]: ...

def XML(text: _parser_input_type, parser: XMLParser=...) -> Element: ...
def XMLID(text: _parser_input_type, parser: XMLParser=...) -> Tuple[Element, Dict[_str_result_type, Element]]: ...

# This is aliased to XML in the source.
fromstring = XML

def fromstringlist(sequence: Sequence[_parser_input_type], parser: XMLParser=...) -> Element: ...

# This type is both not precise enough and too precise. The TreeBuilder
# requires the elementfactory to accept tag and attrs in its args and produce
# some kind of object that has .text and .tail properties.
# I've chosen to constrain the ElementFactory to always produce an Element
# because that is how almost everyone will use it.
# Unfortunately, the type of the factory arguments is dependent on how
# TreeBuilder is called by client code (they could pass strs, bytes or whatever);
# but we don't want to use a too-broad type, or it would be too hard to write
# elementfactories.
_ElementFactory = Callable[[Any, Dict[Any, Any]], Element]

class TreeBuilder:
    def __init__(self, element_factory: _ElementFactory=...) -> None: ...
    def close(self) -> Element: ...
    def data(self, data: _parser_input_type) -> None: ...
    def start(self, tag: _parser_input_type, attrs: Dict[_parser_input_type, _parser_input_type]) -> Element: ...
    def end(self, tag: _parser_input_type) -> Element: ...

class XMLParser:
    parser = ...  # type: Any
    target = ...  # type: TreeBuilder
    # TODO-what is entity used for???
    entity = ...  # type: Any
    version = ...  # type: str
    def __init__(self, html: int=..., target: TreeBuilder=..., encoding: str=...) -> None: ...
    def doctype(self, name: str, pubid: str, system: str) -> None: ...
    def close(self) -> Element: ...
    def feed(self, data: _parser_input_type) -> None: ...
