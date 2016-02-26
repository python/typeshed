from typing import overload, Union

import numbers
import decimal

AnyNumber = Union[numbers.Rational, float, decimal.Decimal, str]


class Fraction(numbers.Rational):
    @overload
    def __init__(self, numerator: numbers.Rational = ...,
                 denominator: numbers.Rational = ...) -> None: ...

    @overload
    def __init__(self, number: AnyNumber) -> None: ...

    @classmethod
    def from_float(flt: float) -> Fraction: ...

    @classmethod
    def from_decimal(dec: decimal.Decimal) -> Fraction: ...

    def limit_denominator(max_denominator: int = ...) -> Fraction: ...

    # TODO: floor, ceil and __round__ are Python 3 only
    def floor(self) -> int: ...
    def ceil(self) -> int: ...
    def __round__(self, ndigits: int = ...) -> Fraction: ...


def gcd(a: int, b: int) -> int: ...
