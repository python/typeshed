import sys
import xml.etree.ElementTree
from _typeshed import Incomplete
from re import Pattern
from typing import overload
from typing_extensions import TypeAlias

# mypy will default to the first import. Pyright will automatically overload
from xml.etree.ElementTree import (
    Element as Element,
    QName as QName,
    SubElement as SubElement,
    fromstring as fromstring,
    iterparse as iterparse,
    register_namespace as register_namespace,
)

import lxml.etree
from lxml.etree import (  # type: ignore[assignment,no-redef]  # noqa: F811  # Implied overload
    Element as Element,
    QName as QName,
    SubElement as SubElement,
    _ElementOrTree,
)

from ._functions import (  # type: ignore[assignment,no-redef]  # noqa: F811  # Implied overload
    fromstring as fromstring,
    iterparse as iterparse,
    register_namespace as register_namespace,
    xmlfile as xmlfile,
)

# Referenced outside this module
_Element: TypeAlias = lxml.etree._Element | xml.etree.ElementTree.Element  # noqa: Y047

NS_REGEX: Pattern[str]

def localname(node): ...
def whitespace(node) -> None: ...

# from xml.etree.ElementTree import tostring
# But made partial, removing encoding arg
if sys.version_info >= (3, 8):
    @overload
    def tostring(
        element: xml.etree.ElementTree.Element,
        method: str | None = ...,
        *,
        xml_declaration: bool | None = ...,
        default_namespace: str | None = ...,
        short_empty_elements: bool = ...,
    ) -> str: ...

else:
    @overload
    def tostring(
        element: xml.etree.ElementTree.Element, method: str | None = ..., *, short_empty_elements: bool = ...
    ) -> str: ...

# from lxml.etree import tostring
# But made partial, removing encoding arg
@overload
def tostring(
    element_or_tree: _ElementOrTree,
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Incomplete = ...,
) -> bytes: ...
