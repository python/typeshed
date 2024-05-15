from _typeshed import Incomplete
from collections.abc import Iterable as _Iterable
from typing import Any
from typing_extensions import Self, TypeAlias

Iterable: TypeAlias = _Iterable[Any]
str_types: Incomplete
__tracebackhide__: bool

class ExtractingMixin:
    def extracting(self, *names: Any, **kwargs: dict[str, Any]) -> Self: ...
