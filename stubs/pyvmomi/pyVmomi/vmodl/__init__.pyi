from typing import Any

from .query import *
from .fault import *

class DynamicProperty:
    def __init__(self, *, name: str = ..., val: Any = ...) -> None: ...
    name: str
    val: Any

class ManagedObject: ...

class KeyAnyValue:
    key: str
    value: Any

class LocalizableMessage:
    key: str
    arg: list[KeyAnyValue] | None
    message: str | None

class MethodFault:
    msg: str | None
    faultCause: MethodFault | None
    faultMessage: list[LocalizableMessage] | None
