from collections.abc import Callable
from types import CodeType
from typing import Any

DEBUGGER_ID: int
COVERAGE_ID: int
PROFILER_ID: int
OPTIMIZER_ID: int

def use_tool_id(__id: int, __name: str) -> None: ...
def free_tool_id(__id: int) -> None: ...
def get_tool(__id: int) -> str | None: ...

events: _events

class _events:
    BRANCH: int
    CALL: int
    C_RAISE: int
    C_RETURN: int
    EXCEPTION_HANDLED: int
    INSTRUCTION: int
    JUMP: int
    LINE: int
    NO_EVENTS: int
    PY_RESUME: int
    PY_RETURN: int
    PY_START: int
    PY_THROW: int
    PY_UNWIND: int
    PY_YIELD: int
    RAISE: int
    RERAISE: int
    STOP_ITERATION: int

def get_events(__tool_id: int) -> int: ...
def set_events(__tool_id: int, __event_set: int) -> None: ...
def get_local_events(__tool_id: int, __code: CodeType) -> int: ...
def set_local_events(__tool_id: int, __code: CodeType, __event_set: int) -> int: ...
def restart_events() -> None: ...  # undocumented
def _all_events() -> dict[str, int]: ...  # undocumented

DISABLE: object
MISSING: object

def register_callback(tool_id: int, event: int, func: Callable[..., Any] | None) -> Callable[..., Any] | None: ...
