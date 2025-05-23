from collections.abc import Callable, Sequence
from typing import TypeVar, overload
from typing_extensions import deprecated

from . import _Cached

__all__ = ("fifo_cache", "lfu_cache", "lru_cache", "mru_cache", "rr_cache", "ttl_cache")
_T = TypeVar("_T")
_S = TypeVar("_S")

def fifo_cache(maxsize: float | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
def lfu_cache(maxsize: float | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
def lru_cache(maxsize: float | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
@deprecated("@mru_cache is deprecated")
def mru_cache(maxsize: float | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
@overload
def rr_cache(maxsize: float | None = 128, *, typed: bool = False) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
@overload
def rr_cache(
    maxsize: float | None, choice: Callable[[Sequence[_S]], _S], typed: bool = False
) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
def ttl_cache(
    maxsize: float | None = 128, ttl: float = 600, timer: Callable[[], float] = ..., typed: bool = False
) -> Callable[[Callable[..., _T]], _Cached[_T]]: ...
