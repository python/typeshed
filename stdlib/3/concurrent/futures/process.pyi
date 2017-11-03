from typing import Optional, Any

import sys

from ._base import Future, Executor

EXTRA_QUEUED_CALLS = ...  # type: Any

class BrokenProcessPool(RuntimeError): ...

if sys.version_info >= (3, 6):
    class ProcessPoolExecutor(Executor[ProcessPoolExecutor]):
        def __init__(self, max_workers: Optional[int] = ...) -> None: ...

else:
    class ProcessPoolExecutor(Executor):
        def __init__(self, max_workers: Optional[int] = ...) -> None: ...
