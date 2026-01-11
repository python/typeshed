from re import Pattern
from sre_constants import *
from sre_constants import _NamedIntConstant
from sre_parse import SubPattern
from typing import Any, Final, Literal, overload
from typing_extensions import TypeIs

MAXCODE: Final[int]

def dis(code: list[_NamedIntConstant]) -> None: ...
@overload
def isstring(obj: str | bytes) -> Literal[True]: ...
@overload
def isstring(obj: object) -> TypeIs[str | bytes]: ...
def compile(p: str | bytes | SubPattern, flags: int = 0) -> Pattern[Any]: ...
