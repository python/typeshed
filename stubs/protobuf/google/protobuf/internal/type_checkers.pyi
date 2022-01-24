from typing import Any, TypeVar

_T = TypeVar("_T")

class TypeChecker:
    def __init__(self, *acceptable_types: Any): ...
    def CheckValue(self, proposed_value: _T) -> _T: ...
