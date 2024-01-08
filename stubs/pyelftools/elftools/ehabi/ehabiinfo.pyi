from _typeshed import Incomplete

class EHABIInfo:
    def __init__(self, arm_idx_section, little_endian) -> None: ...
    def section_name(self): ...
    def section_offset(self): ...
    def num_entry(self): ...
    def get_entry(self, n): ...

class EHABIEntry:
    function_offset: Incomplete
    personality: Incomplete
    bytecode_array: Incomplete
    eh_table_offset: Incomplete
    unwindable: Incomplete
    corrupt: Incomplete
    def __init__(
        self,
        function_offset,
        personality,
        bytecode_array,
        eh_table_offset: Incomplete | None = None,
        unwindable: bool = True,
        corrupt: bool = False,
    ) -> None: ...
    def mnmemonic_array(self): ...

class CorruptEHABIEntry(EHABIEntry):
    reason: Incomplete
    def __init__(self, reason) -> None: ...

class CannotUnwindEHABIEntry(EHABIEntry):
    def __init__(self, function_offset) -> None: ...

class GenericEHABIEntry(EHABIEntry):
    def __init__(self, function_offset, personality) -> None: ...

def arm_expand_prel31(address, place): ...
