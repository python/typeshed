from collections.abc import Callable
from typing import Any
from typing_extensions import NotRequired, TypedDict

TYPES_MAP: dict[str, str]
REVERSE_TYPES_MAP: dict[str, str]

class _Signature(TypedDict):
    types: list[str]
    variadic: NotRequired[bool]

def signature(*arguments: _Signature) -> Callable[..., Callable[..., Any]]: ...

class FunctionRegistry(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class Functions:
    FUNCTION_TABLE: Any
    def call_function(self, function_name, resolved_args): ...
