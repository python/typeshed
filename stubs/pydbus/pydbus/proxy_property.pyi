from _typeshed import Unused
from typing import Generic, TypeVar, overload
from typing_extensions import Self
from xml.etree.ElementTree import Element

from .proxy import ProxyObject

_T = TypeVar("_T")

class ProxyProperty(Generic[_T]):
    def __init__(self, iface_name: str, property: Element) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Unused) -> Self: ...
    @overload
    def __get__(self, instance: ProxyObject[_T], owner: Unused) -> _T: ...
    @overload
    def __get__(self, instance: ProxyObject[_T] | None, owner: Unused) -> Self | _T: ...
    def __set__(self, instance: ProxyObject[_T] | None, value: _T) -> None: ...
