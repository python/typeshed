from typing import TypedDict, type_check_only

@type_check_only
class _ContinueRequestResult(TypedDict):
    allThreadsContinued: bool

def next(
    *, threadId: int, singleThread: bool = False, granularity: str = "statement", **args
) -> None: ...  # args argument is unused
def step_in(
    *, threadId: int, singleThread: bool = False, granularity: str = "statement", **args
) -> None: ...  # args argument is unused
def step_out(*, threadId: int, singleThread: bool = False, **args): ...  # args argument is unused
def continue_request(
    *, threadId: int, singleThread: bool = False, **args
) -> _ContinueRequestResult: ...  # args argument is unused
