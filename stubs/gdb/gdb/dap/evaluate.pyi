from typing import Literal, TypedDict, type_check_only

import gdb

from .varref import ValueFormat, VariableReference, VariableReferenceDescriptor

class EvaluateResult(VariableReference):
    def __init__(self, value: gdb.Value) -> None: ...

@type_check_only
class _VariablesResult(TypedDict):
    variables: list[VariableReferenceDescriptor]

def eval_request(
    *,
    expression: str,
    frameId: int | None = None,
    context: Literal["watch", "variables", "hover", "repl"] = "variables",
    format: ValueFormat | None = None,
    **args,
) -> VariableReferenceDescriptor: ...  # args argument is unused
def variables(
    *, variablesReference: int, start: int = 0, count: int = 0, format: ValueFormat | None = None, **args
) -> _VariablesResult: ...  # args argument is unused
def set_expression(
    *, expression: str, value: str, frameId: int | None = None, format: ValueFormat | None = None, **args
) -> VariableReferenceDescriptor: ...  # args argument is unused
def set_variable(
    *, variablesReference: int, name: str, value: str, format: ValueFormat | None = None, **args
) -> VariableReferenceDescriptor: ...  # args argument is unused
