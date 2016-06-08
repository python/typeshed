from typing import Iterator, List, Mapping, Any, TypeVar

class Enum:
    def __new__(cls, value: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __dir__(self) -> List[str]: ...
    def __format__(self, format_spec: str) -> str: ...
    def __hash__(self) -> Any: ...
    def __iter__(self) -> Iterator['Enum']: ...
    def __reduce_ex__(self, proto: Any) -> Any: ...

    name = ...  # type: str
    value = None  # type: Any

    __members__ = ...  # type: Mapping[str, 'Enum']

class IntEnum(int, Enum): ...

_T = TypeVar('_T')

def unique(enumeration: _T) -> _T: ...
