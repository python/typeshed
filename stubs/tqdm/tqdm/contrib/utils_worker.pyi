from _typeshed import Incomplete

class MonoWorker:
    pool: Incomplete
    futures: Incomplete
    def __init__(self) -> None: ...
    def submit(self, func, *args, **kwargs): ...
