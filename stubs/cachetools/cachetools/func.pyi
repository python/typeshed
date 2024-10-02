from _typeshed import IdentityFunction
from collections.abc import Callable, Sequence
from typing import TypeVar
from typing_extensions import deprecated

__all__ = ("fifo_cache", "lfu_cache", "lru_cache", "mru_cache", "rr_cache", "ttl_cache")
_T = TypeVar("_T")

def fifo_cache(maxsize: float | None = 128, typed: bool = False) -> IdentityFunction: ...
def lfu_cache(maxsize: float | None = 128, typed: bool = False) -> IdentityFunction: ...
def lru_cache(maxsize: float | None = 128, typed: bool = False) -> IdentityFunction: ...
@deprecated("@mru_cache is deprecated")
def mru_cache(maxsize: float | None = 128, typed: bool = False) -> IdentityFunction: ...
def rr_cache(
    maxsize: float | None = 128, choice: Callable[[Sequence[_T]], _T] | None = ..., typed: bool = False
) -> IdentityFunction: ...
def ttl_cache(
    maxsize: float | None = 128, ttl: float = 600, timer: Callable[[], float] = ..., typed: bool = False
) -> IdentityFunction: ...
