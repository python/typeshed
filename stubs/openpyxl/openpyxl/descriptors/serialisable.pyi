from _typeshed import Incomplete
from typing import ClassVar, NoReturn

from openpyxl.descriptors import MetaSerialisable

KEYWORDS: Incomplete
seq_types: Incomplete

class Serialisable(metaclass=MetaSerialisable):
    # These dunders are always set at runtime by MetaSerialisable so they can't be None
    __attrs__: ClassVar[tuple[str, ...]]
    __nested__: ClassVar[tuple[str, ...]]
    __elements__: ClassVar[tuple[str, ...]]
    __namespaced__: ClassVar[tuple[tuple[str, str], ...]]
    idx_base: int
    # Needs overrides in many sub-classes. But a lot of subclasses are instanciated without overriding it, so can't be abstract
    @property
    def tagname(self) -> str | NoReturn: ...
    namespace: Incomplete
    @classmethod
    def from_tree(cls, node): ...
    def to_tree(self, tagname: str | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...
    def __add__(self, other): ...
    def __copy__(self): ...
