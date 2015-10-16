# Stubs for types

from typing import Any, Tuple, Optional

class ModuleType:
    __name__ = ... # type: str
    __file__ = ... # type: str
    def __init__(self, name: str, doc: str) -> None: ...

class TracebackType:
    ...

class FrameType:
    ...

class GeneratorType:
    ...

class ListType:
    ...

class CodeType:
    co_argcount = ...  # type: int
    co_cellvars = ...  # type: Tuple[str, ...]
    co_code = ...  # type: str
    co_consts = ...  # type: Tuple[Any, ...]
    co_filename = ...  # type: Optional[str]
    co_firstlineno = ...  # type: int
    co_flags = ...  # type: int
    co_freevars = ...  # type: Tuple[str, ...]
    co_lnotab = ...  # type: str
    co_name = ...  # type: str
    co_names = ...  # type: Tuple[str, ...]
    co_nlocals= ...  # type: int
    co_stacksize= ...  # type: int
    co_varnames = ...  # type: Tuple[str, ...]
