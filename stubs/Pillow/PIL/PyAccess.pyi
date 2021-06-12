from typing import Any

defs: str
ffi: Any
logger: Any

class PyAccess:
    readonly: Any
    image8: Any
    image32: Any
    image: Any
    def __init__(self, img, readonly: bool = ...) -> None: ...
    def __setitem__(self, xy, color): ...
    def __getitem__(self, xy): ...
    putpixel: Any
    getpixel: Any
    def check_xy(self, xy): ...

class _PyAccess32_2(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess32_3(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess32_4(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccess8(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_N(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_L(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI16_B(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI32_N(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessI32_Swap(PyAccess):
    def reverse(self, i): ...
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

class _PyAccessF(PyAccess):
    def get_pixel(self, x, y): ...
    def set_pixel(self, x, y, color) -> None: ...

mode_map: Any

def new(img, readonly: bool = ...): ...
