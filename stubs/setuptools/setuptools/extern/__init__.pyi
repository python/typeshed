from _typeshed import Incomplete
from typing import Any

class VendorImporter:
    root_name: Any
    vendored_names: Any
    vendor_pkg: Any
    def __init__(self, root_name, vendored_names=..., vendor_pkg: Incomplete | None = ...) -> None: ...
    @property
    def search_path(self) -> None: ...
    def load_module(self, fullname): ...
    def create_module(self, spec): ...
    def exec_module(self, module) -> None: ...
    def find_spec(self, fullname, path: Incomplete | None = ..., target: Incomplete | None = ...): ...
    def install(self) -> None: ...

names: Any