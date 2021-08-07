from _typeshed import StrOrBytesPath
from types import FrameType
from typing import Any, List

from . import tasks

def _task_repr_info(task: tasks.Task[Any]) -> List[str]: ...  # undocumented
def _task_get_stack(task: tasks.Task[Any], limit: int | None) -> List[FrameType]: ...  # undocumented
def _task_print_stack(task: tasks.Task[Any], limit: int | None, file: StrOrBytesPath) -> None: ...  # undocumented
