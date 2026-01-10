from re import Pattern
from sre_constants import *
from sre_constants import _NamedIntConstant
from sre_parse import SubPattern
from typing import Any, Final
from typing_extensions import TypeGuard

MAXCODE: Final[int]

def dis(code: list[_NamedIntConstant]) -> None: ...
def isstring(obj: object) -> TypeGuard[str | bytes]: ...
def compile(p: str | bytes | SubPattern, flags: int = 0) -> Pattern[Any]: ...
