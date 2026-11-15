import operator


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
