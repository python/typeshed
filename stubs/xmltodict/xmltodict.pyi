from _typeshed import Incomplete, ReadableBuffer, SupportsRead, SupportsWrite
from collections.abc import Callable, Mapping
from types import GeneratorType
from typing import Any, overload

__author__: str
__version__: str
__license__: str

class ParsingInterrupted(Exception): ...

class _DictSAXHandler:
    path: Incomplete
    stack: Incomplete
    data: Incomplete
    item: Incomplete
    item_depth: Incomplete
    xml_attribs: Incomplete
    item_callback: Incomplete
    attr_prefix: Incomplete
    cdata_key: Incomplete
    force_cdata: Incomplete
    cdata_separator: Incomplete
    postprocessor: Incomplete
    dict_constructor: Incomplete
    strip_whitespace: Incomplete
    namespace_separator: Incomplete
    namespaces: Incomplete
    namespace_declarations: Incomplete
    force_list: Incomplete
    comment_key: Incomplete
    def __init__(
        self,
        item_depth: int = 0,
        item_callback=...,
        xml_attribs: bool = True,
        attr_prefix: str = "@",
        cdata_key: str = "#text",
        force_cdata: bool = False,
        cdata_separator: str = "",
        postprocessor=None,
        dict_constructor=...,
        strip_whitespace: bool = True,
        namespace_separator: str = ":",
        namespaces=None,
        force_list=None,
        comment_key: str = "#comment",
    ) -> None: ...
    def startNamespaceDecl(self, prefix, uri) -> None: ...
    def startElement(self, full_name, attrs) -> None: ...
    def endElement(self, full_name) -> None: ...
    def characters(self, data) -> None: ...
    def comments(self, data) -> None: ...
    def push_data(self, item, key, data): ...

def parse(
    xml_input: str | ReadableBuffer | SupportsRead[bytes] | GeneratorType[ReadableBuffer, Any, Any],
    encoding: str | None = None,
    expat=...,
    process_namespaces: bool = False,
    namespace_separator: str = ":",
    disable_entities: bool = True,
    process_comments: bool = False,
    **kwargs: Any,
) -> dict[str, Any]: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: SupportsWrite[bytes] | SupportsWrite[str],
    encoding: str = "utf-8",
    full_document: bool = True,
    short_empty_elements: bool = False,
    *,
    attr_prefix: str = "@",
    cdata_key: str = "#text",
    depth: int = 0,
    preprocessor: Callable[[str, Incomplete], tuple[str, Incomplete]] | None = None,
    pretty: bool = False,
    newl: str = "\n",
    indent: str = "\t",
    namespace_separator: str = ":",
    namespaces: dict[str, str] | None = None,
    expand_iter: str | None = None,
) -> None: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: None = ...,
    encoding: str = "utf-8",
    full_document: bool = True,
    short_empty_elements: bool = False,
    *,
    attr_prefix: str = "@",
    cdata_key: str = "#text",
    depth: int = 0,
    preprocessor: Callable[[str, Incomplete], tuple[str, Incomplete]] | None = None,
    pretty: bool = False,
    newl: str = "\n",
    indent: str = "\t",
    namespace_separator: str = ":",
    namespaces: dict[str, str] | None = None,
    expand_iter: str | None = None,
) -> str: ...
