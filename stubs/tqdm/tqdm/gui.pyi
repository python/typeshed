from _typeshed import Incomplete
from typing import Generic, TypeVar

from .std import tqdm as std_tqdm

_T = TypeVar('_T')
class tqdm_gui(Generic[_T], std_tqdm[_T]):
    mpl: Incomplete
    plt: Incomplete
    toolbar: Incomplete
    mininterval: Incomplete
    xdata: Incomplete
    ydata: Incomplete
    zdata: Incomplete
    hspan: Incomplete
    wasion: Incomplete
    ax: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    disable: bool
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...

def tgrange(*args, **kwargs): ...

tqdm = tqdm_gui
trange = tgrange
