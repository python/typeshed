from _typeshed import Incomplete

from ..auto import tqdm as tqdm_auto
from .utils_worker import MonoWorker

class DiscordIO(MonoWorker):
    text: Incomplete
    message: Incomplete
    def __init__(self, token, channel_id) -> None: ...
    def write(self, s): ...

class tqdm_discord(tqdm_auto):
    dio: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> None: ...

def tdrange(*args, **kwargs): ...

tqdm = tqdm_discord
trange = tdrange
