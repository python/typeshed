from _typeshed import Incomplete
from typing import Any

from bs4.builder import HTMLTreeBuilder, TreeBuilder

class LXMLTreeBuilderForXML(TreeBuilder):
    DEFAULT_PARSER_CLASS: Any
    is_xml: bool
    processing_instruction_class: Any
    NAME: str
    ALTERNATE_NAMES: Any
    features: Any
    CHUNK_SIZE: int
    DEFAULT_NSMAPS: Any
    DEFAULT_NSMAPS_INVERTED: Any
    def initialize_soup(self, soup) -> None: ...
    def default_parser(self, encoding): ...
    def parser_for(self, encoding): ...
    empty_element_tags: Any
    soup: Any
    nsmaps: Any
    def __init__(self, parser: Incomplete | None = ..., empty_element_tags: Incomplete | None = ..., **kwargs) -> None: ...
    def prepare_markup(  # type: ignore[override]  # the order of the parameters is different
        self,
        markup,
        user_specified_encoding: Incomplete | None = ...,
        exclude_encodings: Incomplete | None = ...,
        document_declared_encoding: Incomplete | None = ...,
    ) -> None: ...
    parser: Any
    def feed(self, markup) -> None: ...
    def close(self) -> None: ...
    def start(self, name, attrs, nsmap=...) -> None: ...
    def end(self, name) -> None: ...
    def pi(self, target, data) -> None: ...
    def data(self, content) -> None: ...
    def doctype(self, name, pubid, system) -> None: ...
    def comment(self, content) -> None: ...
    def test_fragment_to_document(self, fragment): ...

class LXMLTreeBuilder(HTMLTreeBuilder, LXMLTreeBuilderForXML):
    NAME: Any
    ALTERNATE_NAMES: Any
    features: Any
    is_xml: bool
    processing_instruction_class: Any
    def default_parser(self, encoding): ...
    parser: Any
    def feed(self, markup) -> None: ...
    def test_fragment_to_document(self, fragment): ...
