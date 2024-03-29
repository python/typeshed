from _typeshed import Incomplete
from logging.config import valid_ident as valid_ident

from ..construct import Adapter, Sequence as Sequence
from .enums import *

class DWARFStructs:
    little_endian: Incomplete
    dwarf_format: Incomplete
    address_size: Incomplete
    dwarf_version: Incomplete
    def __new__(cls, little_endian, dwarf_format, address_size, dwarf_version: int = 2): ...
    def initial_length_field_size(self): ...

class _InitialLengthAdapter(Adapter): ...
