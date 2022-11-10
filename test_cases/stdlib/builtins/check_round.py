from typing_extensions import assert_type

class CustomIndex:
    def __index__(self) -> int:
        return 1

# float:

assert_type(round(5.5), int)
assert_type(round(5.5, None), int)
assert_type(round(5.5, 0), float)
assert_type(round(5.5, 1), float)
assert_type(round(5.5, 5), float)
assert_type(round(5.5, CustomIndex()), float)

# int:

assert_type(round(1), int)
assert_type(round(1, 1), int)
assert_type(round(1, None), int)
assert_type(round(1, CustomIndex()), int)

# Protocols:

class WithCustomRound1:
    def __round__(self) -> str:
        return "a"


assert_type(round(WithCustomRound1()), str)
assert_type(round(WithCustomRound1(), None), str)
# Errors:
round(WithCustomRound1(), 1)  # type: ignore
round(WithCustomRound1(), CustomIndex())  # type: ignore


class WithCustomRound2:
    def __round__(self, digits: int) -> str:
        return "a"


assert_type(round(WithCustomRound2(), 1), str)
assert_type(round(WithCustomRound2(), CustomIndex()), str)
# Errors:
round(WithCustomRound2(), None)  # type: ignore
round(WithCustomRound2())  # type: ignore
