from _typeshed import Incomplete

from .compat import SupportsIndex

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
    def __new__(cls, *args, **kw): ...
    def replace(self, old, new, maxreplace: SupportsIndex = -1): ...
    @property
    def anchor(self): ...
    def yaml_anchor(self, any: bool = False): ...
    def yaml_set_anchor(self, value, always_dump: bool = False) -> None: ...

class LiteralScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Incomplete | None = None): ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Incomplete | None = None): ...

class SingleQuotedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Incomplete | None = None): ...

class DoubleQuotedScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Incomplete | None = None): ...

class PlainScalarString(ScalarString):
    style: str
    def __new__(cls, value: str, anchor: Incomplete | None = None): ...
