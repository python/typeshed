from typing import Any, Callable, Dict, Optional, Tuple
from typing_extensions import TypeAlias, assert_type
from weakref import finalize

_ResultStructure: TypeAlias = Optional[Tuple[str, Callable[[int, int], int], Tuple[Any, ...], Dict[str, Any]]]


class TObj:
    """_T type var in stubs"""

    pass


def callback(x: int, y: int) -> int:
    return x + y


final = finalize(TObj, callback, 1, y=2)
assert_type(final.peek(), _ResultStructure)
assert_type(final.detach(), _ResultStructure)
assert_type(final1(), int | None)
