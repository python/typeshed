from typing import Any, Optional

class Binding(object):
    ffi: Any | None
    lib: Any | None
    def init_static_locks(self) -> None: ...
