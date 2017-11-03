from typing import Optional
from ._base import Executor, Future
import sys

if sys.version_info >= (3, 6):
    class ThreadPoolExecutor(Executor[ThreadPoolExecutor]):
        def __init__(self, max_workers: Optional[int] = ..., thread_name_prefix: str = ...) -> None: ...

else:
    class ThreadPoolExecutor(Executor):
        def __init__(self, max_workers: Optional[int] = ...) -> None: ...
