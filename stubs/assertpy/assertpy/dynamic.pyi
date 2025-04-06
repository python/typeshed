import collections.abc
from collections.abc import Callable
from typing_extensions import Self

Iterable = collections.abc.Iterable
__tracebackhide__: bool

class DynamicMixin:
    def __getattr__(self, attr: str) -> Callable[..., Self]: ...
