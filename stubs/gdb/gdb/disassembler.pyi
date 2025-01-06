import enum
from collections.abc import Sequence
from typing import Final, Protocol, final

import gdb
from gdb import Architecture, Progspace

class Disassembler:
    def __init__(self, name: str) -> None: ...
    def __call__(self, info): ...

class DisassembleInfo:
    address: int
    architecture: Architecture
    progspace: Progspace
    def __init__(self, info: DisassembleInfo) -> None: ...
    def address_part(self, address: int) -> DisassemblerAddressPart: ...
    def is_valid(self) -> bool: ...
    def read_memory(self, len: int, offset: int = 0): ...
    def text_part(self, style: Style, string: str) -> DisassemblerTextPart: ...

class DisassemblerPart:
    def __init__(self, /, *args, **kwargs) -> None: ...

@final
class DisassemblerAddressPart(DisassemblerPart):
    address: int
    string: str

@final
class DisassemblerTextPart(DisassemblerPart):
    string: str
    style: Style

@final
class DisassemblerResult:
    def __init__(self, length: int, string: str | None = None, parts: Sequence[DisassemblerPart] | None = None) -> None: ...
    length: int
    parts: Sequence[DisassemblerPart]
    string: str

class Style(enum.IntEnum):
    STYLE_TEXT = 0
    STYLE_MNEMONIC = 1
    STYLE_SUB_MNEMONIC = 2
    STYLE_ASSEMBLER_DIRECTIVE = 3
    STYLE_REGISTER = 4
    STYLE_IMMEDIATE = 5
    STYLE_ADDRESS = 6
    STYLE_ADDRESS_OFFSET = 7
    STYLE_SYMBOL = 8
    STYLE_COMMENT_START = 9

STYLE_TEXT: Final = 0
STYLE_MNEMONIC: Final = 1
STYLE_SUB_MNEMONIC: Final = 2
STYLE_ASSEMBLER_DIRECTIVE: Final = 3
STYLE_REGISTER: Final = 4
STYLE_IMMEDIATE: Final = 5
STYLE_ADDRESS: Final = 6
STYLE_ADDRESS_OFFSET: Final = 7
STYLE_SYMBOL: Final = 8
STYLE_COMMENT_START: Final = 9

class MemorySource(Protocol):
    def read_memory(self, len: int, offset: int): ...

def builtin_disassemble(info: DisassembleInfo, memory_source: MemorySource | None = None) -> None: ...

class maint_info_py_disassemblers_cmd(gdb.Command):
    def __init__(self) -> None: ...
    def invoke(self, args, from_tty): ...

def register_disassembler(disassembler: type[Disassembler], architecture: str | None = None): ...
