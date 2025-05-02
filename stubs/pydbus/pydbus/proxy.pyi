from typing import Generic, TypeVar, type_check_only
from typing_extensions import Self
from xml.etree.ElementTree import Element

from .bus import Bus

_T = TypeVar("_T")

class ProxyMixin(Generic[_T]):
    def get(self, bus_name: str, object_path: str | None = None, *, timeout: int | None = None) -> _CompositeObject[_T]: ...

class ProxyObject(Generic[_T]):
    def __init__(self, bus: Bus[_T], bus_name: str, path: str, object: Self | None = None) -> None: ...
    def __getattr__(self, name: str) -> _T: ...
    def __setattr__(self, name: str, value: _T) -> None: ...

@type_check_only
class _CompositeObject(ProxyObject[_T]):  # Inside CompositeInterface
    def __getitem__(self, iface: str) -> ProxyObject[_T]: ...

@type_check_only
class _interface(ProxyObject[_T]):  # inside Interface
    @staticmethod
    def _Introspect() -> None: ...

def Interface(iface: Element) -> _interface[object]: ...
def CompositeInterface(introspection: Element) -> _CompositeObject[object]: ...
