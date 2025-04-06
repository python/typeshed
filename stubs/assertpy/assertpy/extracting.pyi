import collections.abc
from collections.abc import Callable, Iterable as _Iterable, Mapping
from typing import Any
from typing_extensions import Self

str_types: tuple[type[str]]
Iterable = collections.abc.Iterable
__tracebackhide__: bool

class ExtractingMixin:
    def extracting(
        self,
        *names: str,
        filter: str | Mapping[str, Any] | Callable[[Any], bool] = ...,
        sort: str | _Iterable[str] | Callable[[Any], Any] = ...,
    ) -> Self: ...
