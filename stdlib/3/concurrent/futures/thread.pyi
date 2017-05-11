from typing import Optional
from ._base import Executor, Future

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: Optional[int] = ...) -> None: ...
