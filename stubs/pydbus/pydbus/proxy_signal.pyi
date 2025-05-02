from _typeshed import Unused
from collections.abc import Callable
from typing import Generic, TypeVar, overload
from typing_extensions import Self
from xml.etree.ElementTree import Element

from .generic import bound_signal
from .proxy import ProxyObject
from .subscription import Subscription

_PT = TypeVar("_PT")  # ProxyObject type
_T = TypeVar("_T")

class ProxySignal(Generic[_T, _PT]):
    def __init__(self, iface_name: str, signal: Element) -> None: ...
    def connect(self, object: str, callback: Callable[..., None]) -> Subscription: ...
    @overload
    def __get__(self, instance: None, owner: Unused) -> Self: ...
    @overload
    def __get__(self, instance: ProxyObject[_PT], owner: Unused) -> bound_signal[_T]: ...
    @overload
    def __get__(self, instance: ProxyObject[_PT] | None, owner: Unused) -> bound_signal[_T] | Self: ...
    def __set__(self, instance: Unused, value: Unused) -> None: ...  # Always raises

class OnSignal(Generic[_T, _PT]):
    signal: ProxySignal[_T, _PT]

    def __init__(self, signal: ProxySignal[_T, _PT]) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Unused) -> Self: ...
    @overload
    def __get__(self, instance: ProxyObject[_PT], owner: Unused) -> _T: ...
    @overload
    def __get__(self, instance: ProxyObject[_PT] | None, owner: Unused) -> _T: ...
    def __set__(self, instance: ProxyObject[_PT] | None, value: _T) -> None: ...
