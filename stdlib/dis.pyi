import sys
import types
from opcode import EXTENDED_ARG as EXTENDED_ARG
from opcode import HAVE_ARGUMENT as HAVE_ARGUMENT
from opcode import cmp_op as cmp_op
from opcode import hascompare as hascompare
from opcode import hasconst as hasconst
from opcode import hasfree as hasfree
from opcode import hasjabs as hasjabs
from opcode import hasjrel as hasjrel
from opcode import haslocal as haslocal
from opcode import hasname as hasname
from opcode import hasnargs as hasnargs
from opcode import opmap as opmap
from opcode import opname as opname
from opcode import stack_effect as stack_effect
from typing import (IO, Any, Callable, Dict, Iterator, List, NamedTuple,
                    Optional, Tuple, Union)

# Strictly this should not have to include Callable, but mypy doesn't use FunctionType
# for functions (python/mypy#3171)
_have_code = Union[types.MethodType, types.FunctionType, types.CodeType, type, Callable[..., Any]]
_have_code_or_string = Union[_have_code, str, bytes]

class Instruction(NamedTuple):
    opname: str
    opcode: int
    arg: Optional[int]
    argval: Any
    argrepr: str
    offset: int
    starts_line: Optional[int]
    is_jump_target: bool

class Bytecode:
    codeobj: types.CodeType
    first_line: int
    def __init__(
        self, x: _have_code_or_string, *, first_line: Optional[int] = ..., current_offset: Optional[int] = ...
    ) -> None: ...
    def __iter__(self) -> Iterator[Instruction]: ...
    def __repr__(self) -> str: ...
    def info(self) -> str: ...
    def dis(self) -> str: ...
    @classmethod
    def from_traceback(cls, tb: types.TracebackType) -> Bytecode: ...

COMPILER_FLAG_NAMES: Dict[int, str]

def findlabels(code: _have_code) -> List[int]: ...
def findlinestarts(code: _have_code) -> Iterator[Tuple[int, int]]: ...
def pretty_flags(flags: int) -> str: ...
def code_info(x: _have_code_or_string) -> str: ...

if sys.version_info >= (3, 7):
    def dis(x: Optional[_have_code_or_string] = ..., *, file: Optional[IO[str]] = ..., depth: Optional[int] = ...) -> None: ...

else:
    def dis(x: Optional[_have_code_or_string] = ..., *, file: Optional[IO[str]] = ...) -> None: ...

def distb(tb: Optional[types.TracebackType] = ..., *, file: Optional[IO[str]] = ...) -> None: ...
def disassemble(co: _have_code, lasti: int = ..., *, file: Optional[IO[str]] = ...) -> None: ...
def disco(co: _have_code, lasti: int = ..., *, file: Optional[IO[str]] = ...) -> None: ...
def show_code(co: _have_code, *, file: Optional[IO[str]] = ...) -> None: ...
def get_instructions(x: _have_code, *, first_line: Optional[int] = ...) -> Iterator[Instruction]: ...
