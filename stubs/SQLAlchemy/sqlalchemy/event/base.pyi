from _typeshed import Incomplete
from typing import Any

class _UnpickleDispatch:
    def __call__(self, _instance_cls): ...

class _Dispatch:
    def __init__(self, parent, instance_cls: Incomplete | None = ...) -> None: ...
    def __getattr__(self, name: str): ...
    def __reduce__(self): ...

class _EventMeta(type):
    def __init__(cls, classname, bases, dict_) -> None: ...

class Events:
    dispatch: Any

class _JoinedDispatcher:
    local: Any
    parent: Any
    def __init__(self, local, parent) -> None: ...
    def __getattr__(self, name: str): ...

class dispatcher:
    dispatch: Any
    events: Any
    def __init__(self, events) -> None: ...
    def __get__(self, obj, cls): ...

class slots_dispatcher(dispatcher):
    def __get__(self, obj, cls): ...