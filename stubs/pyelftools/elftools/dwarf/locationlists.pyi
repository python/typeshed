from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class LocationExpr(NamedTuple):
    loc_expr: Incomplete

class LocationEntry(NamedTuple):
    entry_offset: Incomplete
    entry_length: Incomplete
    begin_offset: Incomplete
    end_offset: Incomplete
    loc_expr: Incomplete
    is_absolute: Incomplete

class BaseAddressEntry(NamedTuple):
    entry_offset: Incomplete
    entry_length: Incomplete
    base_address: Incomplete

class LocationViewPair(NamedTuple):
    entry_offset: Incomplete
    begin: Incomplete
    end: Incomplete

entry_translate: Incomplete

class LocationListsPair:
    def __init__(self, streamv4, streamv5, structs, dwarfinfo: Incomplete | None = None) -> None: ...
    def get_location_list_at_offset(self, offset, die: Incomplete | None = None): ...
    def iter_location_lists(self) -> None: ...
    def iter_CUs(self) -> None: ...

class LocationLists:
    stream: Incomplete
    structs: Incomplete
    dwarfinfo: Incomplete
    version: Incomplete
    def __init__(self, stream, structs, version: int = 4, dwarfinfo: Incomplete | None = None) -> None: ...
    def get_location_list_at_offset(self, offset, die: Incomplete | None = None): ...
    def iter_location_lists(self) -> Generator[Incomplete, None, None]: ...
    def iter_CUs(self): ...

class LocationParser:
    location_lists: Incomplete
    def __init__(self, location_lists) -> None: ...
    @staticmethod
    def attribute_has_location(attr, dwarf_version): ...
    def parse_from_attribute(self, attr, dwarf_version, die: Incomplete | None = None): ...
