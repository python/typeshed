import ctypes
from typing_extensions import assert_type


class Foo:
    def __bool__(self) -> bool:
        return True


class Bar:
    def __len__(self) -> int:
        return 1


assert_type(ctypes.c_bool(True), ctypes.c_bool)
assert_type(ctypes.c_bool(0), ctypes.c_bool)
assert_type(ctypes.c_bool([]), ctypes.c_bool)
assert_type(ctypes.c_bool({}), ctypes.c_bool)
assert_type(ctypes.c_bool(()), ctypes.c_bool)
assert_type(ctypes.c_bool(set[str]()), ctypes.c_bool)
assert_type(ctypes.c_bool(1.5), ctypes.c_bool)
assert_type(ctypes.c_bool("non-empty"), ctypes.c_bool)
assert_type(ctypes.c_bool(None), ctypes.c_bool)
assert_type(ctypes.c_bool(Foo()), ctypes.c_bool)
assert_type(ctypes.c_bool(Bar()), ctypes.c_bool)
