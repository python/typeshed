import sys
import types
from collections import UserDict

# test `types.SimpleNamespace`

# Valid:
types.SimpleNamespace()
types.SimpleNamespace(x=1, y=2)

if sys.version_info >= (3, 13):
    types.SimpleNamespace(())
    types.SimpleNamespace([])
    types.SimpleNamespace([("x", "y"), ("z", 1)])
    types.SimpleNamespace({})
    types.SimpleNamespace(UserDict({"x": 1, "y": 2}))


# Invalid:
types.SimpleNamespace(1)  # type: ignore
types.SimpleNamespace([1])  # type: ignore
types.SimpleNamespace([["x"]])  # type: ignore
types.SimpleNamespace(**{1: 2})  # type: ignore
types.SimpleNamespace({1: 2})  # type: ignore
types.SimpleNamespace([[1, 2]])  # type: ignore
types.SimpleNamespace(UserDict({1: 2}))  # type: ignore
types.SimpleNamespace([[[], 2]])  # type: ignore
