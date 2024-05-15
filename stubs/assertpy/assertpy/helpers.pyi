from collections.abc import Iterable as _Iterable
from typing import Any
from typing_extensions import TypeAlias

__tracebackhide__: bool

Iterable: TypeAlias = _Iterable[Any]

class HelpersMixin: ...
