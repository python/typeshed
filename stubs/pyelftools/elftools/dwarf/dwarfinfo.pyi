from _typeshed import Incomplete
from typing import NamedTuple

class DebugSectionDescriptor(NamedTuple):
    stream: Incomplete
    name: Incomplete
    global_offset: Incomplete
    size: Incomplete
    address: Incomplete

class DwarfConfig(NamedTuple):
    little_endian: Incomplete
    machine_arch: Incomplete
    default_address_size: Incomplete

class DWARFInfo:
    config: Incomplete
    debug_info_sec: Incomplete
    debug_aranges_sec: Incomplete
    debug_abbrev_sec: Incomplete
    debug_frame_sec: Incomplete
    eh_frame_sec: Incomplete
    debug_str_sec: Incomplete
    debug_loc_sec: Incomplete
    debug_ranges_sec: Incomplete
    debug_line_sec: Incomplete
    debug_addr_sec: Incomplete
    debug_str_offsets_sec: Incomplete
    debug_line_str_sec: Incomplete
    debug_pubtypes_sec: Incomplete
    debug_pubnames_sec: Incomplete
    debug_loclists_sec: Incomplete
    debug_rnglists_sec: Incomplete
    debug_sup_sec: Incomplete
    gnu_debugaltlink_sec: Incomplete
    supplementary_dwarfinfo: Incomplete
    structs: Incomplete
    def __init__(
        self,
        config,
        debug_info_sec,
        debug_aranges_sec,
        debug_abbrev_sec,
        debug_frame_sec,
        eh_frame_sec,
        debug_str_sec,
        debug_loc_sec,
        debug_ranges_sec,
        debug_line_sec,
        debug_pubtypes_sec,
        debug_pubnames_sec,
        debug_addr_sec,
        debug_str_offsets_sec,
        debug_line_str_sec,
        debug_loclists_sec,
        debug_rnglists_sec,
        debug_sup_sec,
        gnu_debugaltlink_sec,
    ) -> None: ...
    @property
    def has_debug_info(self): ...
    def get_DIE_from_lut_entry(self, lut_entry): ...
    def get_DIE_from_refaddr(self, refaddr, cu: Incomplete | None = None): ...
    def get_CU_containing(self, refaddr): ...
    def get_CU_at(self, offset): ...
    def iter_CUs(self): ...
    def get_abbrev_table(self, offset): ...
    def get_string_from_table(self, offset): ...
    def get_string_from_linetable(self, offset): ...
    def line_program_for_CU(self, CU): ...
    def has_CFI(self): ...
    def CFI_entries(self): ...
    def has_EH_CFI(self): ...
    def EH_CFI_entries(self): ...
    def get_pubtypes(self): ...
    def get_pubnames(self): ...
    def get_aranges(self): ...
    def location_lists(self): ...
    def range_lists(self): ...
    def get_addr(self, cu, addr_index): ...
    def parse_debugsupinfo(self): ...
