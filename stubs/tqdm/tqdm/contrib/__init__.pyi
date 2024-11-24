from _typeshed import Incomplete
from collections.abc import Callable, Generator

from ..utils import ObjectWrapper

__all__ = ["tenumerate", "tmap", "tzip"]

class DummyTqdmFile(ObjectWrapper):
    def __init__(self, wrapped) -> None: ...
    def write(self, x, nolock: bool = False) -> None: ...
    def __del__(self) -> None: ...

def tenumerate(iterable, start: int = 0, total: Incomplete | None = None, tqdm_class: type[Incomplete] = ..., **tqdm_kwargs): ...
def tzip(iter1, *iter2plus, **tqdm_kwargs) -> Generator[Incomplete, None, None]: ...
def tmap(function: Callable[..., Incomplete], *sequences, **tqdm_kwargs) -> Generator[Incomplete, None, None]: ...
