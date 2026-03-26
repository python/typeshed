from _typeshed import StrOrBytesPath
from types import FrameType
from typing import Any

from .tasks import Task

def _task_repr_info(task: Task[Any]) -> list[str]: ...  # undocumented
def _task_repr(task: Task[Any]) -> str: ... # undocumented
def _task_get_stack(task: Task[Any], limit: int | None) -> list[FrameType]: ...  # undocumented
def _task_print_stack(task: Task[Any], limit: int | None, file: StrOrBytesPath) -> None: ...  # undocumented
