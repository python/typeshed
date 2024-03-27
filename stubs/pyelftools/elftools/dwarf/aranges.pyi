from _typeshed import Incomplete
from typing import NamedTuple

class ARangeEntry(NamedTuple):
    begin_addr: Incomplete
    length: Incomplete
    info_offset: Incomplete
    unit_length: Incomplete
    version: Incomplete
    address_size: Incomplete
    segment_size: Incomplete

class ARanges:
    stream: Incomplete
    size: Incomplete
    structs: Incomplete
    entries: Incomplete
    keys: Incomplete
    def __init__(self, stream, size, structs) -> None: ...
    def cu_offset_at_addr(self, addr): ...
