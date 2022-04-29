from _typeshed import Incomplete

from gevent.event import AsyncResult  # type: ignore
from huey.api import crontab as crontab
from huey.utils import time_clock as time_clock

logger: Incomplete

class MiniHueyResult(AsyncResult):
    __call__: Incomplete

class MiniHuey:
    name: Incomplete
    def __init__(self, name: str = ..., interval: int = ..., pool_size: Incomplete | None = ...) -> None: ...
    def task(self, validate_func: Incomplete | None = ...): ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
