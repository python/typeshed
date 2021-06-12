from typing import Any

class ImagePalette:
    mode: Any
    rawmode: Any
    palette: Any
    colors: Any
    dirty: Any
    def __init__(self, mode: str = ..., palette: Any | None = ..., size: int = ...) -> None: ...
    def copy(self): ...
    def getdata(self): ...
    def tobytes(self): ...
    tostring: Any
    def getcolor(self, color): ...
    def save(self, fp) -> None: ...

def raw(rawmode, data): ...
def make_linear_lut(black, white): ...
def make_gamma_lut(exp): ...
def negative(mode: str = ...): ...
def random(mode: str = ...): ...
def sepia(white: str = ...): ...
def wedge(mode: str = ...): ...
def load(filename): ...
