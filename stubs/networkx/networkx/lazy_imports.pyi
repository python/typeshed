import types
from _typeshed import Incomplete

def attach(module_name, submodules: Incomplete | None = None, submod_attrs: Incomplete | None = None): ...

class DelayedImportErrorModule(types.ModuleType):
    def __init__(self, frame_data, *args, **kwargs) -> None: ...
    def __getattr__(self, x) -> None: ...

# Names in __all__ with no definition:
#   _lazy_import
