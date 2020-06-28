from types import FrameType
from typing import List, Optional

from _typeshed import AnyPath

from . import tasks

def _task_repr_info(task: tasks.Task) -> List[str]: ...  # undocumented
def _task_get_stack(task: tasks.Task, limit: Optional[int]) -> List[FrameType]: ...  # undocumented
def _task_print_stack(task: tasks.Task, limit: Optional[int], file: AnyPath): ...  # undocumented
