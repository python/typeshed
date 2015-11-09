from typing import Sequence, TypeVar

_T = TypeVar('_T')

def insort_left(a: Sequence[_T], x: _T, lo: int = ..., hi: int = ...): pass
def insort_right(a: Sequence[_T], x: _T, lo: int = ..., hi: int = ...): pass

def bisect_left(a: Sequence[_T], x: _T, lo: int = ..., hi: int = ...): pass
def bisect_right(a: Sequence[_T], x: _T, lo: int = ..., hi: int = ...): pass

insort = insort_right
bisect = bisect_right
