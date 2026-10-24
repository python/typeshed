from .function_hooks import enabled_hooks as enabled_hooks
from .import_hook import instrument_imports as instrument_imports
from .instrument_bytecode import instrument_all as instrument_all, instrument_func as instrument_func
from .native import (
    ALL_REMAINING as ALL_REMAINING,
    Fuzz as Fuzz,
    FuzzedDataProvider as FuzzedDataProvider,
    Mutate as Mutate,
    Setup as Setup,
)
from .utils import path as path

def get_hook_dirs() -> list[str]: ...  # undocumented
