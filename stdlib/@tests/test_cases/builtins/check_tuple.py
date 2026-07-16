from __future__ import annotations

import sys
from collections.abc import MutableSequence
from typing import Any, Tuple, TypeVar
from typing_extensions import assert_type


# Empty tuples, see #8275
class TupleSub(Tuple[int, ...]):
    pass


assert_type(TupleSub(), TupleSub)
assert_type(TupleSub([1, 2, 3]), TupleSub)

# Hashability shenanigans, see #15852
t: Tuple[int, int] = (1, 3)
hash(t)
u: Tuple[int, ...] = t
hash(u)
v: Tuple[int] = u
hash(v)
w: Tuple[()] = u
hash(w)
hash(tuple(sys.platform))
hash(([],))  # type: ignore
x: Tuple[Any, Any] = ({}, ())
hash(x)
y = ((),)
assert_type(y, Tuple[Tuple[()]])
hash(y)
z = ({}, ())
hash(z)  # type: ignore
