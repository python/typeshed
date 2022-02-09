from typing import Any, Mapping, MutableMapping, TypeVar

from .decoder import TomlDecoder
from .encoder import TomlEncoder

_MutableMappingT = TypeVar("_MutableMappingT", bound=MutableMapping[str, Any])
_MappingT = TypeVar("_MappingT", bound=Mapping[str, Any])

class TomlOrderedDecoder(TomlDecoder[_MutableMappingT]):
    def __init__(self) -> None: ...

class TomlOrderedEncoder(TomlEncoder[_MappingT]):
    def __init__(self) -> None: ...
