from typing import Any

class Binding:
    ffi: Any
    lib: Any
    def init_static_locks(self) -> None: ...
