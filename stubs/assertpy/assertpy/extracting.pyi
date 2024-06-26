from collections.abc import Callable, Mapping, Iterable as _Iterable
from typing import Any
from typing_extensions import Self

__tracebackhide__: bool

class ExtractingMixin:
    def extracting(
        self,
        *names: str,
        filter: str | Mapping[str, Any] | Callable[[Any], bool],
        sort: str | _Iterable[str] | Callable[[Any], Any],
    ) -> Self: ...
