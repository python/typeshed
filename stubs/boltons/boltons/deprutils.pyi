# TODO: DONE!

from types import ModuleType
from typing import Any, NoReturn

class DeprecatableModule(ModuleType):
    def __init__(self, module: ModuleType) -> NoReturn: ...
    def __getattribute__(self, name: str) -> Any: ...

def deprecate_module_member(mod_name: str, name: str, message: str) -> NoReturn: ...
