from typing import TypeVar

from .decoder import TomlDecoder
from .encoder import TomlEncoder

_T = TypeVar("_T")

class TomlOrderedDecoder(TomlDecoder[_T]):
    def __init__(self) -> None: ...

class TomlOrderedEncoder(TomlEncoder[_T]):
    def __init__(self) -> None: ...
