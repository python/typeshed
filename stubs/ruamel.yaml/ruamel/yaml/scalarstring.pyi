from typing import Any

from ruamel.yaml.compat import SupportsIndex

__all__ = [
    "ScalarString",
    "LiteralScalarString",
    "FoldedScalarString",
    "SingleQuotedScalarString",
    "DoubleQuotedScalarString",
    "PlainScalarString",
    "PreservedScalarString",
]

class ScalarString(str):
    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def replace(self, old: Any, new: Any, maxreplace: SupportsIndex = -1) -> Any: ...
    @property
    def anchor(self) -> Any: ...
    def yaml_anchor(self, any: bool = False) -> Any: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...

class LiteralScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Any = None) -> Any: ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Any = None) -> Any: ...

class SingleQuotedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Any = None) -> Any: ...

class DoubleQuotedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Any = None) -> Any: ...

class PlainScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Any = None) -> Any: ...
