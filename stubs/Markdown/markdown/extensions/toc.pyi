from collections.abc import Iterator, MutableSet
from re import Pattern
from typing import Any, TypedDict
from xml.etree.ElementTree import Element

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

IDCOUNT_RE: Pattern[str]

class _FlatTocToken(TypedDict):
    level: int
    id: str
    name: str

class _TocToken(_FlatTocToken):
    children: list[_TocToken]

def slugify(value: str, separator: str, unicode: bool = False) -> str: ...
def slugify_unicode(value: str, separator: str) -> str: ...
def unique(id: str, ids: MutableSet[str]) -> str: ...
def get_name(el: Element) -> str: ...
def stashedHTML2text(text: str, md: Markdown, strip_entities: bool = True) -> str: ...
def unescape(text: str) -> str: ...
def nest_toc_tokens(toc_list: list[_FlatTocToken]) -> list[_TocToken]: ...

class TocTreeprocessor(Treeprocessor):
    marker: str
    title: str
    base_level: int
    slugify: Any
    sep: Any
    toc_class: Any
    title_class: str
    use_anchors: bool
    anchorlink_class: str
    use_permalinks: bool
    permalink_class: str
    permalink_title: str
    permalink_leading: bool
    header_rgx: Pattern[str]
    toc_top: int
    toc_bottom: int
    def __init__(self, md: Markdown, config: dict[str, Any]) -> None: ...
    def iterparent(self, node: Element) -> Iterator[tuple[Element, Element]]: ...
    def replace_marker(self, root: Element, elem: Element) -> None: ...
    def set_level(self, elem: Element) -> None: ...
    def add_anchor(self, c: Element, elem_id: str) -> None: ...
    def add_permalink(self, c: Element, elem_id: str) -> None: ...
    def build_toc_div(self, toc_list: list[_TocToken]) -> Element: ...
    def run(self, doc: Element) -> None: ...

class TocExtension(Extension):
    TreeProcessorClass: type[TocTreeprocessor]
    def __init__(self, **kwargs) -> None: ...
    md: Markdown
    def reset(self) -> None: ...

def makeExtension(**kwargs) -> TocExtension: ...
