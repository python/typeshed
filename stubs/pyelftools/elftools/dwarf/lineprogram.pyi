from _typeshed import Incomplete
from typing import NamedTuple

from .constants import *

class LineProgramEntry(NamedTuple):
    command: Incomplete
    is_extended: Incomplete
    args: Incomplete
    state: Incomplete

class LineState:
    address: int
    file: int
    line: int
    column: int
    op_index: int
    is_stmt: Incomplete
    basic_block: bool
    end_sequence: bool
    prologue_end: bool
    epilogue_begin: bool
    isa: int
    discriminator: int
    def __init__(self, default_is_stmt) -> None: ...

class LineProgram:
    stream: Incomplete
    header: Incomplete
    structs: Incomplete
    program_start_offset: Incomplete
    program_end_offset: Incomplete
    def __init__(self, header, stream, structs, program_start_offset, program_end_offset) -> None: ...
    def get_entries(self): ...
    def __getitem__(self, name): ...
