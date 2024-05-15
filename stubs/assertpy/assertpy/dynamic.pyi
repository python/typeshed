from collections.abc import Iterable as _Iterable
from typing import Any
from typing_extensions import Self, TypeAlias

__tracebackhide__: bool

Iterable: TypeAlias = _Iterable[Any]

class DynamicMixin:
    def __getattr__(self, attr: str) -> Self: ...
