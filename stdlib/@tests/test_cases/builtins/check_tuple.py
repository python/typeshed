from __future__ import annotations

import sys
from typing import Any
from typing_extensions import assert_type


# Empty tuples, see #8275
class TupleSub(tuple[int, ...]):
    pass


assert_type(TupleSub(), TupleSub)
assert_type(TupleSub([1, 2, 3]), TupleSub)

# Hashability shenanigans, see #15852
t: tuple[int, int] = (1, 3)
hash(t)
u: tuple[int, ...] = tuple(b"spam")
hash(u)
v: tuple[str] = ("",)
hash(v)
w: tuple[()] = ()
hash(w)
hash(tuple(sys.platform))
x: tuple[Any, Any] = ((), ())
hash(x)
