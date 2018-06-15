from typing import Optional, Any
from ._base import Future, Executor
import sys

EXTRA_QUEUED_CALLS = ...  # type: Any

if sys.version_info >= (3,):
    class BrokenProcessPool(RuntimeError): ...

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: Optional[int] = ...) -> None: ...
