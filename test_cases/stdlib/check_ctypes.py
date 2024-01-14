# pyright: reportUninitializedInstanceVariable=false

from __future__ import annotations

import ctypes
from typing import Any
from typing_extensions import assert_type


class Annotated(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int), ("f", ctypes.c_float)]
    i: ctypes.c_int
    f: ctypes.c_float


class NoAnnotation(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int), ("f", ctypes.c_float)]


class NonCType:
    i: ctypes.c_int
    f: ctypes.c_float


assert_type(ctypes.c_int().value, int)
ctypes.c_int() + 2  # type: ignore

assert_type(ctypes.c_float().value, float)
ctypes.c_float() + 2  # type: ignore

# All passes; all access are Any
assert_type(NoAnnotation().x + 2, Any)
assert_type(NoAnnotation().vec.x + 2, Any)

Annotated.x.value + 2  # type: ignore
Annotated.x + 2  # type: ignore
assert_type(Annotated().i, int)
Annotated().i.value + 2  # type: ignore
assert_type(Annotated().f, float)
Annotated().f.value + 3.14  # type: ignore

assert_type(NonCType.i.value, int)
NonCType.i + 2  # type: ignore
NonCType().i + 2  # type: ignore
assert_type(NonCType().i.value, int)
