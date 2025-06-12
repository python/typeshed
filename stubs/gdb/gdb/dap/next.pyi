from typing import Literal, TypedDict, type_check_only
from typing_extensions import TypeAlias

@type_check_only
class _ContinueRequestResult(TypedDict):
    allThreadsContinued: bool

_Granularity: TypeAlias = Literal["statement", "instruction"]

def next(
    *, threadId: int, singleThread: bool = False, granularity: _Granularity = "statement", **args
) -> None: ...  # args argument is unused
def step_in(
    *, threadId: int, singleThread: bool = False, granularity: _Granularity = "statement", **args
) -> None: ...  # args argument is unused
def step_out(*, threadId: int, singleThread: bool = False, **args): ...  # args argument is unused
def continue_request(
    *, threadId: int, singleThread: bool = False, **args
) -> _ContinueRequestResult: ...  # args argument is unused
