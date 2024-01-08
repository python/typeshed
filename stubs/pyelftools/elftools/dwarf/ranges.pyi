from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class RangeEntry(NamedTuple):
    entry_offset: Incomplete
    entry_length: Incomplete
    begin_offset: Incomplete
    end_offset: Incomplete
    is_absolute: Incomplete

class BaseAddressEntry(NamedTuple):
    entry_offset: Incomplete
    base_address: Incomplete

entry_translate: Incomplete

class RangeListsPair:
    def __init__(self, streamv4, streamv5, structs, dwarfinfo: Incomplete | None = None) -> None: ...
    def get_range_list_at_offset(self, offset, cu: Incomplete | None = None): ...
    def get_range_list_at_offset_ex(self, offset): ...
    def iter_range_lists(self) -> None: ...
    def iter_CUs(self): ...
    def iter_CU_range_lists_ex(self, cu): ...

class RangeLists:
    stream: Incomplete
    structs: Incomplete
    version: Incomplete
    def __init__(self, stream, structs, version, dwarfinfo) -> None: ...
    def get_range_list_at_offset(self, offset, cu: Incomplete | None = None): ...
    def get_range_list_at_offset_ex(self, offset): ...
    def iter_range_lists(self) -> Generator[Incomplete, None, None]: ...
    def iter_CUs(self): ...
    def iter_CU_range_lists_ex(self, cu) -> Generator[Incomplete, None, None]: ...
    def translate_v5_entry(self, entry, cu): ...
