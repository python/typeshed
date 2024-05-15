from collections.abc import Iterable as _Iterable
from typing import Any
from typing_extensions import Self, TypeAlias

__tracebackhide__: bool

Iterable: TypeAlias = _Iterable[Any]

class ExceptionMixin:
    def raises(self, ex: BaseException) -> Self: ...
    def when_called_with(self, *some_args: Any, **some_kwargs: dict[str, Any]) -> Self: ...
