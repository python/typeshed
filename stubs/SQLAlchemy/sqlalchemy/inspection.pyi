from typing import TypeVar, overload
from typing_extensions import Literal

from .engine.interfaces import Dialect
from .engine.reflection import Inspector

_D = TypeVar("_D", bound=Dialect)

@overload
def inspect(subject: _D, raiseerr: Literal[False]) -> _D | Inspector | None: ...
@overload
def inspect(subject: _D, raiseerr: Literal[True] = True) -> _D | Inspector: ...
@overload
def inspect(subject, raiseerr: Literal[False]) -> Inspector | None: ...
@overload
def inspect(subject, raiseerr: Literal[True] = True) -> Inspector: ...
