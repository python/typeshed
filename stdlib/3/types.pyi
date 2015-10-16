# Stubs for types

# TODO this is work in progress

from typing import Any, Callable, Dict, Sequence, Optional, Tuple

class ModuleType:
    __name__ = ... # type: str
    __file__ = ... # type: str
    def __init__(self, name: str, doc: Any) -> None: ...

class MethodType: ...
class BuiltinMethodType: ...

class CodeType:
    """Create a code object.  Not for the faint of heart."""
    co_argcount = ... # type: int
    co_kwonlyargcount = ... # type: int
    co_nlocals = ... # type: int
    co_stacksize = ... # type: int
    co_flags = ... # type: int
    co_code = ... # type: bytes
    co_consts = ... # type: Tuple[Any, ...]
    co_names = ... # type: Tuple[str, ...]
    co_varnames = ... # type: Tuple[str, ...]
    co_filename = ... # type: Optional[str]
    co_name = ... # type: str
    co_firstlineno = ... # type: int
    co_lnotab = ... # type: bytes
    co_freevars = ... # type: Tuple[str, ...]
    co_cellvars = ... # type: Tuple[str, ...]
    def __init__(self,
            argcount: int,
            kwonlyargcount: int,
            nlocals: int,
            stacksize: int,
            flags: int,
            codestring: bytes,
            constants: Tuple[Any, ...],
            names: Tuple[str, ...],
            varnames: Tuple[str, ...],
            filename: str,
            name: str,
            firstlineno: int,
            lnotab: bytes,
            freevars: Tuple[str, ...] = (),
            cellvars: Tuple[str, ...] = (),
    ) -> None: ...

class FrameType:
    f_back = ... # type: FrameType
    f_builtins = ... # type: Dict[str, Any]
    f_code = ... # type: CodeType
    f_globals = ... # type: Dict[str, Any]
    f_lasti = ... # type: int
    f_lineno = ... # type: int
    f_locals = ... # type: Dict[str, Any]
    f_trace = ... # type: Callable[[], None]

    def clear(self) -> None: pass

class TracebackType:
    tb_frame = ... # type: FrameType
    tb_lasti = ... # type: int
    tb_lineno = ... # type: int
    tb_next = ... # type: TracebackType
