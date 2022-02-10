from typing import Any, OrderedDict

from .decoder import TomlDecoder
from .encoder import TomlEncoder

class TomlOrderedDecoder(TomlDecoder[OrderedDict[str, Any]]):
    def __init__(self) -> None: ...

class TomlOrderedEncoder(TomlEncoder[OrderedDict[str, Any]]):
    def __init__(self) -> None: ...
