# Provisional stubs for six.moves (Python 2.7)

from typing import overload, TypeVar, Tuple, Iterable, Iterator

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')

@overload
def zip(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2],
        iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def zip(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3],
        iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2,
                                               _T3, _T4]]: ... # TODO more than four iterables

# For re-export.
import cStringIO as cStringIO
import cPickle as cPickle
