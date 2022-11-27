# TODO: DONE!

from typing import NoReturn, TypeVar

_T = TypeVar("_T")

def get_all(type_obj: _T, include_subtypes: bool = ...) -> list[_T]: ...

class GCToggler:
    postcollect: bool
    def __init__(self, postcollect: bool = ...) -> NoReturn: ...
    def __enter__(self) -> NoReturn: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> NoReturn: ...

toggle_gc: GCToggler
toggle_gc_postcollect: GCToggler
