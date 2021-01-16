import sys
from typing import Any, Callable, Generic, Iterable, Iterator, Optional, Tuple, TypeVar, overload
from typing_extensions import Literal

_T = TypeVar("_T")
_S = TypeVar("_S")
_N = TypeVar("_N", int, float)
Predicate = Callable[[_T], object]

def count(start: _N = ..., step: _N = ...) -> Iterator[_N]: ...  # more general types?

class cycle(Iterator[_T], Generic[_T]):
    def __init__(self, __iterable: Iterable[_T]) -> None: ...
    def __next__(self) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...

@overload
def repeat(object: _T) -> Iterator[_T]: ...
@overload
def repeat(object: _T, times: int) -> Iterator[_T]: ...

if sys.version_info >= (3, 8):
    @overload
    def accumulate(iterable: Iterable[_T], func: None = ..., *, initial: Optional[_T] = ...) -> Iterator[_T]: ...
    @overload
    def accumulate(iterable: Iterable[_T], func: Callable[[_S, _T], _S], *, initial: Optional[_S] = ...) -> Iterator[_S]: ...

else:
    def accumulate(iterable: Iterable[_T], func: Optional[Callable[[_T, _T], _T]] = ...) -> Iterator[_T]: ...

class chain(Iterator[_T], Generic[_T]):
    def __init__(self, *iterables: Iterable[_T]) -> None: ...
    def __next__(self) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    @staticmethod
    def from_iterable(iterable: Iterable[Iterable[_S]]) -> Iterator[_S]: ...

def compress(data: Iterable[_T], selectors: Iterable[Any]) -> Iterator[_T]: ...
def dropwhile(__predicate: Predicate[_T], __iterable: Iterable[_T]) -> Iterator[_T]: ...
def filterfalse(__predicate: Optional[Predicate[_T]], __iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def groupby(iterable: Iterable[_T], key: None = ...) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
@overload
def groupby(iterable: Iterable[_T], key: Callable[[_T], _S]) -> Iterator[Tuple[_S, Iterator[_T]]]: ...
@overload
def islice(__iterable: Iterable[_T], __stop: Optional[int]) -> Iterator[_T]: ...
@overload
def islice(
    __iterable: Iterable[_T], __start: Optional[int], __stop: Optional[int], __step: Optional[int] = ...
) -> Iterator[_T]: ...
def starmap(__function: Callable[..., _S], __iterable: Iterable[Iterable[Any]]) -> Iterator[_S]: ...
def takewhile(__predicate: Predicate[_T], __iterable: Iterable[_T]) -> Iterator[_T]: ...
def tee(__iterable: Iterable[_T], __n: int = ...) -> Tuple[Iterator[_T], ...]: ...
def zip_longest(*p: Iterable[Any], fillvalue: Any = ...) -> Iterator[Any]: ...

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_T6 = TypeVar("_T6")
@overload
def product(__iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(__iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]
) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]
) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
    __iter5: Iterable[_T5],
    __iter6: Iterable[_T6],
) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(
    __iter1: Iterable[Any],
    __iter2: Iterable[Any],
    __iter3: Iterable[Any],
    __iter4: Iterable[Any],
    __iter5: Iterable[Any],
    __iter6: Iterable[Any],
    __iter7: Iterable[Any],
    *iterables: Iterable[Any],
) -> Iterator[Tuple[Any, ...]]: ...
@overload
def product(*iterables: Iterable[_T1], repeat: int) -> Iterator[Tuple[_T1, ...]]: ...
@overload
def product(*iterables: Iterable[Any], repeat: int = ...) -> Iterator[Tuple[Any, ...]]: ...
def permutations(iterable: Iterable[_T], r: Optional[int] = ...) -> Iterator[Tuple[_T, ...]]: ...
@overload
def combinations(iterable: Iterable[_T], r: Literal[2]) -> Iterator[Tuple[_T, _T]]: ...
@overload
def combinations(iterable: Iterable[_T], r: Literal[3]) -> Iterator[Tuple[_T, _T, _T]]: ...
@overload
def combinations(iterable: Iterable[_T], r: Literal[4]) -> Iterator[Tuple[_T, _T, _T, _T]]: ...
@overload
def combinations(iterable: Iterable[_T], r: Literal[5]) -> Iterator[Tuple[_T, _T, _T, _T, _T]]: ...
@overload
def combinations(iterable: Iterable[_T], r: int) -> Iterator[Tuple[_T, ...]]: ...
def combinations_with_replacement(iterable: Iterable[_T], r: int) -> Iterator[Tuple[_T, ...]]: ...
