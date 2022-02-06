from typing import TypeVar

from .decoder import TomlDecoder
from .encoder import TomlEncoder

_T = TypeVar("_T")

class TomlOrderedDecoder(TomlDecoder[_T]): ...
class TomlOrderedEncoder(TomlEncoder): ...
