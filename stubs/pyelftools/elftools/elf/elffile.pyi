from collections.abc import Callable
from pathlib import Path
from typing import Any, BinaryIO, Iterable
from typing_extensions import Self, TypeAlias

from ..construct import Struct
from ..dwarf.dwarfinfo import DWARFInfo
from ..ehabi.ehabiinfo import EHABIInfo
from .sections import Section
from .segments import Segment

_StreamLoader: TypeAlias = Callable[[str | Path], BinaryIO]

class ELFFile:
    stream: BinaryIO
    elfclass: Literal[32, 64]
    little_endian: bool
    elftype: str | int
    header: Struct  # self.structs.Elf_Ehdr
    e_ident_raw: bytes

    def __init__(self, stream: BinaryIO, stream_loader: _StreamLoader | None = None) -> None: ...
    @classmethod
    def load_from_path(cls, path: str | Path) -> Self: ...
    def num_sections(self) -> int: ...
    def get_section(self, n: int) -> Section: ...
    def get_section_by_name(self, name: str) -> Section | None: ...
    def get_section_index(self, section_name) -> int | None: ...
    def iter_sections(self, type: str | None = None) -> Iterable[Section]: ...
    def num_segments(self) -> int: ...
    def get_segment(self, n: int) -> Segment: ...
    def iter_segments(self, type: str | None = None) -> Iterable[Segment]: ...
    def address_offsets(self, start: int, size: int = 1) -> Iterable[int]: ...
    def has_dwarf_info(self) -> bool: ...
    def get_dwarf_info(self, relocate_dwarf_sections: bool = True, follow_links: bool = True) -> DWARFInfo: ...
    def get_supplementary_dwarfinfo(self, dwarfinfo: DWARFInfo) -> DWARFInfo | None: ...
    def has_ehabi_info(self) -> bool: ...
    def get_ehabi_infos(self) -> Iterable[EHABIInfo] | None: ...
    def get_machine_arch(self) -> str: ...
    def get_shstrndx(self) -> int: ...
    def __getitem__(self, name: str) -> Any: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
