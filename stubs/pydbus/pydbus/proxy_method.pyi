from _typeshed import Unused
from inspect import Signature
from typing import Generic, TypeVar

from .proxy import ProxyObject

_CT = TypeVar("_CT")  # __call__ return type
_GT = TypeVar("_GT")  # __get__ return type
_PT = TypeVar("_PT")  # ProxyObject type
put_signature_in_doc: bool = False

class DBUSSignature(Signature): ...

class ProxyMethod(Generic[_GT, _CT, _PT]):
    __signature__: DBUSSignature

    def __init__(self, iface_name: str, method: str) -> None: ...
    def __call__(self, instance: ProxyObject[_PT], *args: object, timeout: int | None = None) -> _CT: ...
    def __get__(self, instance: ProxyObject[_PT], owner: Unused) -> _GT: ...
