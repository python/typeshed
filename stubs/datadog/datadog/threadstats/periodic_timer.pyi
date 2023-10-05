from _typeshed import Incomplete
from threading import Thread

class PeriodicTimer(Thread):
    daemon: bool
    interval: Incomplete
    function: Incomplete
    args: Incomplete
    kwargs: Incomplete
    finished: Incomplete
    def __init__(self, interval, function, *args, **kwargs) -> None: ...
    def end(self) -> None: ...
    def run(self) -> None: ...
