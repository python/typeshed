import operator
from typing import overload


class Result: ...


class Operand: ...


class LessThan(Operand):
    def __lt__(self, other: Operand, /) -> Result:
        return Result()


class GreaterEqual:
    def __ge__(self, other: Operand, /) -> Result:
        return Result()


def check_comparisons(lt: LessThan, ge: GreaterEqual) -> None:
    operator.lt(lt, lt)
    operator.gt(lt, lt)
    operator.ge(ge, lt)
    operator.le(lt, ge)


def check_one_sided_comparisons(lt: LessThan, ge: GreaterEqual, other: Operand) -> None:
    operator.lt(lt, other)
    operator.gt(other, lt)
    operator.ge(ge, other)
    operator.le(other, ge)
    operator.lt(1, other)  # type: ignore[misc]

    operators = {"<": operator.lt, "<=": operator.le, ">": operator.gt, ">=": operator.ge, "==": operator.eq, "!=": operator.ne}
    operators["<"](lt, other)


class Overloaded:
    @overload
    def __lt__(self, other: int, /) -> int: ...
    @overload
    def __lt__(self, other: str, /) -> str: ...
    def __lt__(self, other: int | str, /) -> int | str:
        return other


def check_overloaded(value: Overloaded, other: int | str) -> None:
    operator.lt(value, other)
