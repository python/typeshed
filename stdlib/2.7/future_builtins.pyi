from typing import (
    Iterator,
    TypeVar,
    Iterable,
    overload,
    Any,
    Callable,
    Tuple,
)


_T = TypeVar('_T')
_S = TypeVar('_S')


_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')


def ascii(
    obj: Any,
) -> str: ...


# Stolen from itertools.ifilter
def filter(
    predicate: Callable[[_T], Any],
    iterable: Iterable[_T],
) -> Iterator[_T]: ...


def hex(
    x: int,
) -> str: ...


# Stolen from itertools.imap
@overload
def map(
    func: Callable[[_T1], _S],
    iter1: Iterable[_T1],
) -> Iterable[_S]: ...
@overload
def map(
    func: Callable[[_T1, _T2], _S],
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
) -> Iterable[_S]: ...
# TODO more than two iterables


def oct(
    x: int,
) -> str: ...


# Stolen from itertools.izip
@overload
def zip(
    iter1: Iterable[_T1],
) -> Iterable[Tuple[_T1]]: ...
@overload
def zip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
) -> Iterable[Tuple[_T1, _T2]]: ...
@overload
def zip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
) -> Iterable[Tuple[_T1, _T2, _T3]]: ...
@overload
def zip(
    iter1: Iterable[_T1],
    iter2: Iterable[_T2],
    iter3: Iterable[_T3],
    iter4: Iterable[_T4],
) -> Iterable[Tuple[_T1, _T2, _T3, _T4]]: ...
# TODO more than four iterables
