from typing import Any
from ldap.controls import RequestControl, ResponseControl

class SimplePagedResultsControl(RequestControl, ResponseControl):
    controlType: Any
    size: int
    cookie: Any
    def __init__(self, size: int = 0, cookie: Any = ...) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...
