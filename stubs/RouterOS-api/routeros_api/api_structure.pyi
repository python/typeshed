from abc import ABCMeta, abstractmethod
from collections import defaultdict
from collections.abc import Iterable
from datetime import timedelta
from ipaddress import IPv4Network, IPv6Network
from typing import Generic, Protocol, TypeVar, type_check_only

_In = TypeVar("_In")
_Out = TypeVar("_Out")
_In_contra = TypeVar("_In_contra", contravariant=True)
_Out_co = TypeVar("_Out_co", covariant=True)

# What a resource's structure needs of a field: it encodes a value of an argument or a query, and
# decodes a value of a reply's row. A field need not derive from Field.
@type_check_only
class _Field(Protocol[_In_contra, _Out_co]):
    def get_mikrotik_value(self, arg: _In_contra, /) -> bytes: ...
    def get_python_value(self, bytes: bytes, /) -> _Out_co: ...

class Field(Generic[_In, _Out]):  # undocumented
    # Python 2's spelling of a metaclass: on Python 3 an ordinary attribute, the class's metaclass
    # being type.
    __metaclass__: type[ABCMeta]
    @abstractmethod
    def get_mikrotik_value(self, arg: _In) -> bytes: ...
    @abstractmethod
    def get_python_value(self, bytes: bytes) -> _Out: ...

class StringField(Field[str, str]):
    encoding: str  # undocumented
    def __init__(self, encoding: str = "utf-8") -> None: ...
    def get_mikrotik_value(self, string: str) -> bytes: ...  # undocumented
    def get_python_value(self, bytes: bytes) -> str: ...  # undocumented

class BytesField(Field[bytes, bytes]):  # undocumented
    def get_mikrotik_value(self, bytes: bytes) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> bytes: ...

class BooleanField(Field[bool, bool]):  # undocumented
    def get_mikrotik_value(self, condition: bool) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> bool: ...

class IntegerField(Field[int, int]):  # undocumented
    def get_mikrotik_value(self, number: int) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> int: ...

# The field decodes the router's "none" as None. Through a resource a None argument is sent without a
# value and a None query raises TypeError, so the field takes no None, though get_mikrotik_value
# called directly encodes None as "none".
class TimedeltaField(Field[timedelta, timedelta | None]):  # undocumented
    def get_mikrotik_value(self, timedelta: timedelta) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> timedelta | None: ...
    def parse_mikrotik_timedelta(self, time_string: str) -> timedelta: ...

# The field decodes empty as None. It takes no None for the reason TimedeltaField gives, though
# get_mikrotik_value called directly encodes None as empty.
class IpNetworkField(Field[IPv4Network | IPv6Network, IPv4Network | IPv6Network | None]):  # undocumented
    def get_mikrotik_value(self, ip_network: IPv4Network | IPv6Network) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> IPv4Network | IPv6Network | None: ...

class ListField(Field[Iterable[_In], list[_Out]]):  # undocumented
    subfield: _Field[_In, _Out]
    def __init__(self, subfield: _Field[_In, _Out]) -> None: ...
    def get_mikrotik_value(self, objects: Iterable[_In]) -> bytes: ...
    def get_python_value(self, bytes: bytes) -> list[_Out]: ...

default_structure: defaultdict[str, StringField]
