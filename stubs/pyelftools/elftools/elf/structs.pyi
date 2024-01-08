from _typeshed import Incomplete

from .enums import *

class ELFStructs:
    little_endian: Incomplete
    elfclass: Incomplete
    e_type: Incomplete
    e_machine: Incomplete
    e_ident_osabi: Incomplete
    def __init__(self, little_endian: bool = True, elfclass: int = 32) -> None: ...
    Elf_byte: Incomplete
    Elf_half: Incomplete
    Elf_word: Incomplete
    Elf_word64: Incomplete
    Elf_addr: Incomplete
    Elf_offset: Incomplete
    Elf_sword: Incomplete
    Elf_xword: Incomplete
    Elf_sxword: Incomplete
    def create_basic_structs(self) -> None: ...
    def create_advanced_structs(
        self, e_type: Incomplete | None = None, e_machine: Incomplete | None = None, e_ident_osabi: Incomplete | None = None
    ) -> None: ...
