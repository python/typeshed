from _typeshed import Incomplete
from typing import Any

def add_class(classname, cls, decl_class_registry) -> None: ...
def remove_class(classname, cls, decl_class_registry) -> None: ...

class _MultipleClassMarker:
    on_remove: Any
    contents: Any
    def __init__(self, classes, on_remove: Incomplete | None = None) -> None: ...
    def remove_item(self, cls) -> None: ...
    def __iter__(self): ...
    def attempt_get(self, path, key): ...
    def add_item(self, item) -> None: ...

class _ModuleMarker:
    parent: Any
    name: Any
    contents: Any
    mod_ns: Any
    path: Any
    def __init__(self, name, parent) -> None: ...
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def resolve_attr(self, key): ...
    def get_module(self, name): ...
    def add_class(self, name, cls): ...
    def remove_class(self, name, cls) -> None: ...

class _ModNS:
    def __init__(self, parent) -> None: ...
    def __getattr__(self, key: str): ...

class _GetColumns:
    cls: Any
    def __init__(self, cls) -> None: ...
    def __getattr__(self, key: str): ...

class _GetTable:
    key: Any
    metadata: Any
    def __init__(self, key, metadata) -> None: ...
    def __getattr__(self, key: str): ...

class _class_resolver:
    cls: Any
    prop: Any
    arg: Any
    fallback: Any
    favor_tables: Any
    def __init__(self, cls, prop, fallback, arg, favor_tables: bool = False) -> None: ...
    def __call__(self): ...
