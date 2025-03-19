import sys
from collections.abc import Callable
from typing import Any, Protocol, TextIO

from .timemachine import *

DEBUG: int

class HasAttrs(Protocol):
    def __setattr__(self, name: str, value: Any) -> None: ...

class XLRDError(Exception): ...

class BaseObject:
    _repr_these: list[str]
    def dump(self, f: TextIO | None = None, header: str | None = None, footer: str | None = None, indent: int = 0) -> None: ...

FUN: int
FDT: int
FNU: int
FGE: int
FTX: int
DATEFORMAT = FDT
NUMBERFORMAT = FNU
XL_CELL_EMPTY: int
XL_CELL_TEXT: int
XL_CELL_NUMBER: int
XL_CELL_DATE: int
XL_CELL_BOOLEAN: int
XL_CELL_ERROR: int
XL_CELL_BLANK: int
biff_text_from_num: dict[int, str]
error_text_from_code: dict[int, str]
BIFF_FIRST_UNICODE: int
XL_WORKBOOK_GLOBALS: int
WBKBLOBAL: int
XL_WORKBOOK_GLOBALS_4W: int
XL_WORKSHEET: int
WRKSHEET: int
XL_BOUNDSHEET_WORKSHEET: int
XL_BOUNDSHEET_CHART: int
XL_BOUNDSHEET_VB_MODULE: int
XL_ARRAY: int
XL_ARRAY2: int
XL_BLANK: int
XL_BLANK_B2: int
XL_BOF: int
XL_BOOLERR: int
XL_BOOLERR_B2: int
XL_BOUNDSHEET: int
XL_BUILTINFMTCOUNT: int
XL_CF: int
XL_CODEPAGE: int
XL_COLINFO: int
XL_COLUMNDEFAULT: int
XL_COLWIDTH: int
XL_CONDFMT: int
XL_CONTINUE: int
XL_COUNTRY: int
XL_DATEMODE: int
XL_DEFAULTROWHEIGHT: int
XL_DEFCOLWIDTH: int
XL_DIMENSION: int
XL_DIMENSION2: int
XL_EFONT: int
XL_EOF: int
XL_EXTERNNAME: int
XL_EXTERNSHEET: int
XL_EXTSST: int
XL_FEAT11: int
XL_FILEPASS: int
XL_FONT: int
XL_FONT_B3B4: int
XL_FORMAT: int
XL_FORMAT2: int
XL_FORMULA: int
XL_FORMULA3: int
XL_FORMULA4: int
XL_GCW: int
XL_HLINK: int
XL_QUICKTIP: int
XL_HORIZONTALPAGEBREAKS: int
XL_INDEX: int
XL_INTEGER: int
XL_IXFE: int
XL_LABEL: int
XL_LABEL_B2: int
XL_LABELRANGES: int
XL_LABELSST: int
XL_LEFTMARGIN: int
XL_TOPMARGIN: int
XL_RIGHTMARGIN: int
XL_BOTTOMMARGIN: int
XL_HEADER: int
XL_FOOTER: int
XL_HCENTER: int
XL_VCENTER: int
XL_MERGEDCELLS: int
XL_MSO_DRAWING: int
XL_MSO_DRAWING_GROUP: int
XL_MSO_DRAWING_SELECTION: int
XL_MULRK: int
XL_MULBLANK: int
XL_NAME: int
XL_NOTE: int
XL_NUMBER: int
XL_NUMBER_B2: int
XL_OBJ: int
XL_PAGESETUP: int
XL_PALETTE: int
XL_PANE: int
XL_PRINTGRIDLINES: int
XL_PRINTHEADERS: int
XL_RK: int
XL_ROW: int
XL_ROW_B2: int
XL_RSTRING: int
XL_SCL: int
XL_SHEETHDR: int
XL_SHEETPR: int
XL_SHEETSOFFSET: int
XL_SHRFMLA: int
XL_SST: int
XL_STANDARDWIDTH: int
XL_STRING: int
XL_STRING_B2: int
XL_STYLE: int
XL_SUPBOOK: int
XL_TABLEOP: int
XL_TABLEOP2: int
XL_TABLEOP_B2: int
XL_TXO: int
XL_UNCALCED: int
XL_UNKNOWN: int
XL_VERTICALPAGEBREAKS: int
XL_WINDOW2: int
XL_WINDOW2_B2: int
XL_WRITEACCESS: int
XL_WSBOOL = XL_SHEETPR
XL_XF: int
XL_XF2: int
XL_XF3: int
XL_XF4: int
boflen: dict[int, int]
bofcodes: tuple[int, int, int, int]
XL_FORMULA_OPCODES: tuple[int, int, int]

def is_cell_opcode(c: int) -> bool: ...
def upkbits(
    tgt_obj: HasAttrs, src: int, manifest: list[tuple[int, int, str]], local_setattr: Callable[[Any, str, Any], None] = ...
) -> None: ...
def upkbitsL(
    tgt_obj: HasAttrs,
    src: int,
    manifest: list[tuple[int, int, str]],
    local_setattr: Callable[[Any, str, Any], None] = ...,
    local_int: Callable[[Any], int] = ...,
) -> None: ...
def unpack_string(data: bytes, pos: int, encoding: str, lenlen: int = 1) -> str: ...
def unpack_string_update_pos(
    data: bytes, pos: int, encoding: str, lenlen: int = 1, known_len: int | None = None
) -> tuple[str, int]: ...
def unpack_unicode(data: bytes, pos: int, lenlen: int = 2) -> str: ...
def unpack_unicode_update_pos(data: bytes, pos: int, lenlen: int = 2, known_len: int | None = None) -> tuple[str, int]: ...
def unpack_cell_range_address_list_update_pos(
    output_list: list[tuple[int, int, int, int]], data: bytes, pos: int, biff_version: int, addr_size: int = 6
) -> int: ...

biff_rec_name_dict: dict[int, str]

def hex_char_dump(
    strg: bytes, ofs: int, dlen: int, base: int = 0, fout: TextIO = sys.stdout, unnumbered: bool = False
) -> None: ...
def biff_dump(
    mem: bytes, stream_offset: int, stream_len: int, base: int = 0, fout: TextIO = sys.stdout, unnumbered: bool = False
) -> None: ...
def biff_count_records(mem: bytes, stream_offset: int, stream_len: int, fout: TextIO = sys.stdout) -> None: ...

encoding_from_codepage: dict[int, str]
