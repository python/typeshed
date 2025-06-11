from typing import TypedDict, type_check_only
from typing_extensions import NotRequired

@type_check_only
class _Thread(TypedDict):
    id: int
    name: NotRequired[str]

@type_check_only
class _ThreadsResult(TypedDict):
    threads: list[_Thread]

def threads(**args) -> _ThreadsResult: ...  # args argument is unused
