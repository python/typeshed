from __future__ import annotations

import sys
from typing import Any, Dict, Tuple
from typing_extensions import assert_type


# Empty tuples, see #8275
class TupleSub(Tuple[int, ...]):
    pass


assert_type(TupleSub(), TupleSub)
assert_type(TupleSub([1, 2, 3]), TupleSub)

# Hashability shenanigans, see #15852
t: Tuple[int, int] = (1, 3)
hash(t)
u: Tuple[bytes, ...] = tuple(b"spam")
hash(u)
v: Tuple[str] = ("",)
hash(v)
w: Tuple[()] = ()
hash(w)
hash(tuple(sys.platform))
hash(([],))  # type: ignore
x: Tuple[Any, Any] = ((), ())
hash(x)
z: Tuple[Tuple[Any, ...], Dict[str, Any]] = ((), {})
hash(z)  # type: ignore
