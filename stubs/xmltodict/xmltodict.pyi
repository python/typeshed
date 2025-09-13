from _typeshed import Incomplete, ReadableBuffer, SupportsRead, SupportsWrite
from collections import OrderedDict
from collections.abc import Mapping
from types import GeneratorType
from typing import Any, Final, overload

__author__: Final[str]
__version__: Final[str]
__license__: Final[str]

class ParsingInterrupted(Exception): ...

def parse(
    xml_input: str | ReadableBuffer | SupportsRead[bytes] | GeneratorType[ReadableBuffer, Any, Any],
    encoding: str | None = None,
    expat: Any = ...,
    process_namespaces: bool = False,
    namespace_separator: str = ":",
    disable_entities: bool = True,
    process_comments: bool = False,
    *,
    item_depth: int = 0,
    item_callback=...,
    xml_attribs: bool = True,
    attr_prefix="@",
    cdata_key="#text",
    force_cdata: bool | Incomplete = False,
    cdata_separator="",
    postprocessor=None,
    dict_constructor: type = ...,
    strip_whitespace: bool = True,
    namespaces=None,
    force_list: bool | Incomplete = None,
    comment_key: str = "#comment",
) -> OrderedDict[str, Any]: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: SupportsWrite[bytes] | SupportsWrite[str],
    encoding: str = "utf-8",
    full_document: bool = True,
    short_empty_elements: bool = False,
    comment_key: str = "#comment",
    *,
    attr_prefix: str = "@",
    cdata_key="#text",
    depth: int = 0,
    preprocessor=None,
    pretty: bool = False,
    newl: str = "\n",
    indent: str | int = "\t",
    namespace_separator: str = ":",
    namespaces=None,
    expand_iter=None,
) -> None: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: None = None,
    encoding: str = "utf-8",
    full_document: bool = True,
    short_empty_elements: bool = False,
    comment_key: str = "#comment",
    *,
    attr_prefix: str = "@",
    cdata_key="#text",
    depth: int = 0,
    preprocessor=None,
    pretty: bool = False,
    newl: str = "\n",
    indent: str | int = "\t",
    namespace_separator: str = ":",
    namespaces=None,
    expand_iter=None,
) -> str: ...
