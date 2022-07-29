from collections.abc import Callable
from typing_extensions import assert_type, TypeAlias
from weakref import finalize

_ResultStructure: TypeAlias = tuple[str, Callable[[int, int], int], tuple[int], dict[str, int]]


class TObj:
    """_T type var in stubs"""

    pass


def callback(x: int, y: int) -> int:
    return x + y


final = finalize(TObj, callback, 1, y=2)
final2 = finalize(TObj, callback, 1, y=2)
assert_type(final1.peek(), _ResultStructure)
assert_type(final1.detach(), _ResultStructure)
assert_type(final2(), int)
