from __future__ import annotations

from multiprocessing import Array, Value
from multiprocessing.sharedctypes import Synchronized, SynchronizedString
from ctypes import c_char, c_float
from typing_extensions import assert_type


string = Array(c_char, 12)
assert_type(string, SynchronizedString)

field = Value(c_float, 0.0)
assert_type(field, Synchronized[float])
