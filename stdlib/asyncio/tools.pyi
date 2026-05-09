import sys
from collections.abc import Iterable
from enum import Enum
from typing import SupportsIndex

from _remote_debugging import AwaitedInfo as _AwaitedInfo

class NodeType(Enum):
    COROUTINE = 1
    TASK = 2

class CycleFoundException(Exception):
    cycles: list[list[int]]
    id2name: dict[int, str]
    def __init__(self, cycles: list[list[int]], id2name: dict[int, str]) -> None: ...

def get_all_awaited_by(pid: SupportsIndex) -> list[_AwaitedInfo]: ...
def build_async_tree(result: Iterable[_AwaitedInfo], task_emoji: str = "(T)", cor_emoji: str = "") -> list[list[str]]: ...
def build_task_table(result: Iterable[_AwaitedInfo]) -> list[list[int | str]]: ...

if sys.version_info >= (3, 14):
    def exit_with_permission_help_text() -> None: ...

if sys.version_info >= (3, 15):
    def display_awaited_by_tasks_table(pid: SupportsIndex, retries: SupportsIndex = 3) -> None: ...
    def display_awaited_by_tasks_tree(pid: SupportsIndex, retries: SupportsIndex = 3) -> None: ...

else:
    def display_awaited_by_tasks_table(pid: SupportsIndex) -> None: ...
    def display_awaited_by_tasks_tree(pid: SupportsIndex) -> None: ...
