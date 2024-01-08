from _typeshed import Incomplete
from typing import NamedTuple

from .constants import *

class CallFrameInfo:
    stream: Incomplete
    size: Incomplete
    address: Incomplete
    base_structs: Incomplete
    entries: Incomplete
    for_eh_frame: Incomplete
    def __init__(self, stream, size, address, base_structs, for_eh_frame: bool = False) -> None: ...
    def get_entries(self): ...

def instruction_name(opcode): ...

class CallFrameInstruction:
    opcode: Incomplete
    args: Incomplete
    def __init__(self, opcode, args) -> None: ...

class CFIEntry:
    header: Incomplete
    structs: Incomplete
    instructions: Incomplete
    offset: Incomplete
    cie: Incomplete
    augmentation_dict: Incomplete
    augmentation_bytes: Incomplete
    def __init__(
        self,
        header,
        structs,
        instructions,
        offset,
        augmentation_dict: Incomplete | None = None,
        augmentation_bytes: bytes = b"",
        cie: Incomplete | None = None,
    ) -> None: ...
    def get_decoded(self): ...
    def __getitem__(self, name): ...

class CIE(CFIEntry): ...

class FDE(CFIEntry):
    lsda_pointer: Incomplete
    def __init__(
        self,
        header,
        structs,
        instructions,
        offset,
        augmentation_bytes: Incomplete | None = None,
        cie: Incomplete | None = None,
        lsda_pointer: Incomplete | None = None,
    ) -> None: ...

class ZERO:
    offset: Incomplete
    def __init__(self, offset) -> None: ...

class RegisterRule:
    UNDEFINED: str
    SAME_VALUE: str
    OFFSET: str
    VAL_OFFSET: str
    REGISTER: str
    EXPRESSION: str
    VAL_EXPRESSION: str
    ARCHITECTURAL: str
    type: Incomplete
    arg: Incomplete
    def __init__(self, type, arg: Incomplete | None = None) -> None: ...

class CFARule:
    reg: Incomplete
    offset: Incomplete
    expr: Incomplete
    def __init__(
        self, reg: Incomplete | None = None, offset: Incomplete | None = None, expr: Incomplete | None = None
    ) -> None: ...

class DecodedCallFrameTable(NamedTuple):
    table: Incomplete
    reg_order: Incomplete
