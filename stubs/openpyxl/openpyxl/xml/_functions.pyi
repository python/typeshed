# This file does not exist at runtime. It is a helper file to overload imports in openpyxl.xml.functions
# TODO: Create missing stubs and add missing types upstream
from _typeshed import Incomplete
from collections.abc import Iterator
from typing import overload
from typing_extensions import TypeAlias

from lxml.etree import _AnyStr, _Element

_Unused: TypeAlias = object

# lxml re-definitions are a mix of lxml-stubs and pylance
# defusedxml stubs are missing. But we can still represent them.

# from lxml.etree import register_namespace
# https://github.com/lxml/lxml-stubs/issues/78
def register_namespace(prefix, uri): ...

# from lxml.etree import fromstring
# But made partial, removing parser arg
@overload
def fromstring(text: _AnyStr, *, base_url: _AnyStr = ...) -> _Element: ...  # type: ignore[misc]  # Overlap with incompatible return types

# from defusedxml.ElementTree import fromstring
@overload
def fromstring(text, forbid_dtd: bool = ..., forbid_entities: bool = ..., forbid_external: bool = ...) -> int: ...

# from et_xmlfile.xmlfile import xmlfile
class _et_xmlfile_xmlfile:
    def __init__(
        self, output_file: Incomplete | str, buffered: _Unused = ..., encoding: _Unused = ..., close: bool = ...
    ) -> None: ...
    def __enter__(self) -> Incomplete: ...
    def __exit__(self, type: object, value: object, traceback: object) -> None: ...

# Should be importable from lxml.etree but is missing from lxml-stubs
# https://github.com/lxml/lxml-stubs/issues/77
class _lxml_xmlfile:
    def __aenter__(self): ...
    def __aexit__(self, exc_type, exc_val, exc_tb): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def __init__(self, output_file, encoding=..., compression=..., close=..., buffered=...) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def __subclasshook__(cls, subclass) -> bool: ...
    def __getattr__(self, name): ...

xmlfile: TypeAlias = _et_xmlfile_xmlfile | _lxml_xmlfile  # noqa: Y042  # This is the correct name

# from defusedxml.ElementTree import iterparse
def iterparse(
    source,
    events: Incomplete | None = ...,
    parser: Incomplete | None = ...,
    forbid_dtd: bool = ...,
    forbid_entities: bool = ...,
    forbid_external: bool = ...,
) -> Iterator[tuple[str, Incomplete]]: ...
