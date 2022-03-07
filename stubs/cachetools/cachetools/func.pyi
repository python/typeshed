from _typeshed import IdentityFunction
from typing import Callable, Sequence, TypeVar

_T = TypeVar("_T")

__all__ = ("fifo_cache", "lfu_cache", "lru_cache", "mru_cache", "rr_cache", "ttl_cache")

def fifo_cache(maxsize: float | None = ..., typed: bool = ...) -> IdentityFunction: ...
def lfu_cache(maxsize: float | None = ..., typed: bool = ...) -> IdentityFunction: ...
def lru_cache(maxsize: float | None = ..., typed: bool = ...) -> IdentityFunction: ...
def mru_cache(maxsize: float | None = ..., typed: bool = ...) -> IdentityFunction: ...
def rr_cache(
    maxsize: float | None = ..., choice: Callable[[Sequence[_T]], _T] | None = ..., typed: bool = ...
) -> IdentityFunction: ...
def ttl_cache(
    maxsize: float | None = ..., ttl: float = ..., timer: Callable[[], float] = ..., typed: bool = ...
) -> IdentityFunction: ...
