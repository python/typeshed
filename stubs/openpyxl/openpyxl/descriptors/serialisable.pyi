from _typeshed import Incomplete, SupportsIter
from typing import Any, ClassVar, NoReturn, Protocol
from typing_extensions import Final

from openpyxl.descriptors import MetaSerialisable

from ..xml._functions_overloads import _HasTagAndGet, _HasTagAndTextAndAttrib

class _SerialisableTreeElement(_HasTagAndGet[Incomplete], _HasTagAndTextAndAttrib, SupportsIter[Incomplete], Protocol):
    def find(self, __path: str) -> Incomplete | None: ...

KEYWORDS: Final[frozenset[str]]
seq_types: Final[tuple[type[list[Any]], type[tuple[Any, ...]]]]

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
    namespace: ClassVar[str | None]
    # Note: To respect the Liskov substitution principle, the protocol for node includes all child class requirements
    # See comment in xml/functions.pyi as to why use a protocol instead of Element
    @classmethod
    def from_tree(cls, node: _SerialisableTreeElement): ...
    def to_tree(self, tagname: str | None = None, idx: Incomplete | None = None, namespace: str | None = None): ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...
    def __add__(self, other): ...
    def __copy__(self): ...
