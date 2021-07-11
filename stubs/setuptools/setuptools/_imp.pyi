from typing import Any

from .py34compat import module_from_spec as module_from_spec

PY_SOURCE: int
PY_COMPILED: int
C_EXTENSION: int
C_BUILTIN: int
PY_FROZEN: int

def find_spec(module, paths): ...
def find_module(module, paths: Any | None = ...): ...
def get_frozen_object(module, paths: Any | None = ...): ...
def get_module(module, paths, info): ...
