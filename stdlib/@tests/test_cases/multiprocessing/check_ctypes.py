from __future__ import annotations

import ctypes
from ctypes import Structure, c_char, c_float, c_int
from multiprocessing import Array, Value, sharedctypes
from multiprocessing.sharedctypes import Synchronized, SynchronizedArray, SynchronizedBase, SynchronizedString
from typing import Any
from typing_extensions import assert_type


class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]


string = Array(c_char, 12)
assert_type(string, SynchronizedString)
assert_type(string.value, bytes)

numbers = Array(c_int, 3)
assert_type(numbers, SynchronizedArray[int])
numbers[0] = 3
numbers[:] = [0, 1, 2]

field = Value(c_float, 0.0)
assert_type(field, Synchronized[float])
field.value = 1.2

assert_type(Value("i", 0), Synchronized[Any])
assert_type(Value(c_int, 0, lock=False), c_int)
assert_type(Value(Point), SynchronizedBase[Point])
assert_type(Array(c_int, 3, lock=False), ctypes.Array[c_int])

assert_type(sharedctypes.Value(c_int, 0), Synchronized[int])
assert_type(sharedctypes.Value("i", 0), Synchronized[Any])
assert_type(sharedctypes.Value(c_int, 0, lock=False), c_int)
assert_type(sharedctypes.Value(Point), SynchronizedBase[Point])
assert_type(sharedctypes.Array(c_int, 3, lock=False), ctypes.Array[c_int])
