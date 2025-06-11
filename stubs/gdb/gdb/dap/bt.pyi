from typing import TypedDict, type_check_only
from typing_extensions import NotRequired

from .sources import Source

@type_check_only
class _StackFrameFormat(TypedDict, total=False):
    hex: bool
    parameters: bool
    parameterTypes: bool
    parameterNames: bool
    parameterValues: bool
    line: bool
    module: bool
    includeAll: bool

@type_check_only
class _StackFrame(TypedDict):
    id: int
    name: str
    line: int
    column: int
    instructionPointerReference: str
    moduleId: NotRequired[str | None]
    source: NotRequired[Source]

class _StaceTraceResult(TypedDict):
    stackFrames: list[_StackFrame]

def check_stack_frame(
    *,
    hex: bool = False,
    parameters: bool = False,
    parameterTypes: bool = False,
    parameterNames: bool = False,
    parameterValues: bool = False,
    line: bool = False,
    module: bool = False,
    includeAll: bool = False,
    **rest,
) -> _StackFrameFormat: ...  # rest argument is unused
def stacktrace(
    *, levels: int = 0, startFrame: int = 0, threadId: int, format: _StackFrameFormat | None = None, **extra
) -> _StaceTraceResult: ...  # extra argument is unused
