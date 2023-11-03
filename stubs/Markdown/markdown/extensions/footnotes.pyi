from collections import OrderedDict
from re import Pattern
from typing import Any
from xml.etree.ElementTree import Element

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor

FN_BACKLINK_TEXT: Any
NBSP_PLACEHOLDER: Any
DEF_RE: Pattern[str]
TABBED_RE: Pattern[str]
RE_REF_ID: Any

class FootnoteExtension(Extension):
    unique_prefix: int
    found_refs: Any
    used_refs: Any
    def __init__(self, **kwargs) -> None: ...
    parser: Any
    md: Markdown
    footnotes: OrderedDict[str, str]
    def reset(self) -> None: ...
    def unique_ref(self, reference: str, found: bool = False) -> str: ...
    def findFootnotesPlaceholder(self, root: Element): ...
    def setFootnote(self, id: str, text: str) -> None: ...
    def get_separator(self) -> str: ...
    def makeFootnoteId(self, id: str) -> str: ...
    def makeFootnoteRefId(self, id: str, found: bool = False) -> str: ...
    def makeFootnotesDiv(self, root: Element) -> Element | None: ...

class FootnoteInlineProcessor(InlineProcessor):
    footnotes: FootnoteExtension
    def __init__(self, pattern: str, footnotes: FootnoteExtension) -> None: ...

class FootnotePostTreeprocessor(Treeprocessor):
    footnotes: FootnoteExtension
    def __init__(self, footnotes: FootnoteExtension) -> None: ...
    def add_duplicates(self, li, duplicates) -> None: ...
    def get_num_duplicates(self, li): ...
    def handle_duplicates(self, parent) -> None: ...
    offset: int

class FootnoteTreeprocessor(Treeprocessor):
    footnotes: FootnoteExtension
    def __init__(self, footnotes: FootnoteExtension) -> None: ...

class FootnotePostprocessor(Postprocessor):
    footnotes: FootnoteExtension
    def __init__(self, footnotes: FootnoteExtension) -> None: ...

def makeExtension(**kwargs) -> FootnoteExtension: ...
