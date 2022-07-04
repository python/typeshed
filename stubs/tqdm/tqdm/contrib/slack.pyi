from _typeshed import Incomplete

from ..auto import tqdm as tqdm_auto
from .utils_worker import MonoWorker

class SlackIO(MonoWorker):
    client: Incomplete
    text: Incomplete
    message: Incomplete
    def __init__(self, token, channel) -> None: ...
    def write(self, s): ...

class tqdm_slack(tqdm_auto):
    sio: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, msg: str | None = ..., pos: int | None = ...) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def tsrange(*args, **kwargs): ...

tqdm = tqdm_slack
trange = tsrange
