# Stubs for statistics
# See: http://docs.python.org/3/library/statistics.html

import sys
from typing import Iterable, Iterator, Sequence, TypeVar, Union, overload
from decimal import Decimal
from fractions import Fraction

# Note: according to the docs, statistics only explicitly supports
# int, float, Decimal, and Fraction. Other types within the numeric
# tower are not supported. It also states mixing together different
# types results in undefined behavior, so the type signatures below
# deliberately enforce that numeric types may not be mixed.
_TNum = TypeVar('_TNum', int, float, Decimal, Fraction)
_T = TypeVar('_T')

def mean(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> _TNum: ...
if sys.version_info >= (3, 6):
    def geometric_mean(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> _TNum: ...
    def harmonic_mean(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> _TNum: ...

# Note: in CPython, the output of median_grouped may sometimes be coerced to
# float as an implementation detail. In the interests of not breaking code
# that relies on this implementation detail, the return type is set to the
# Union of float and the contained numeric type.
def median(data: Iterable[_TNum]) -> _TNum: ...
def median_low(data: Iterable[_TNum]) -> _TNum: ...
def median_high(data: Iterable[_TNum]) -> _TNum: ...
def median_grouped(data: Iterable[_TNum],
                   interval: Union[int, float, Fraction] = 1
                   ) -> Union[_TNum, float]: ...

def mode(data: Iterable[_T]) -> _T: ...

def pstdev(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> Union[float, Decimal]: ...
def stdev(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> Union[float, Decimal]: ...
def pvariance(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> _TNum: ...
def variance(data: Union[Iterator[_TNum], Sequence[_TNum]]) -> _TNum: ...

class StatisticsError(ValueError): pass
