from . import book
from .timemachine import *

__all__ = [
    "oBOOL",
    "oERR",
    "oNUM",
    "oREF",
    "oREL",
    "oSTRG",
    "oUNK",
    "decompile_formula",
    "dump_formula",
    "evaluate_name_formula",
    "okind_dict",
    "rangename3d",
    "rangename3drel",
    "cellname",
    "cellnameabs",
    "colname",
    "FMLA_TYPE_CELL",
    "FMLA_TYPE_SHARED",
    "FMLA_TYPE_ARRAY",
    "FMLA_TYPE_COND_FMT",
    "FMLA_TYPE_DATA_VAL",
    "FMLA_TYPE_NAME",
    "Operand",
    "Ref3D",
]

FMLA_TYPE_CELL: int
FMLA_TYPE_SHARED: int
FMLA_TYPE_ARRAY: int
FMLA_TYPE_COND_FMT: int
FMLA_TYPE_DATA_VAL: int
FMLA_TYPE_NAME: int
oBOOL: int
oERR: int
oNUM: int
oREF: int
oREL: int
oSTRG: int
oUNK: int
okind_dict: dict[int, str]

class FormulaError(Exception): ...

class Operand:
    value: float | str | None
    kind: int
    text: str
    rank: int
    def __init__(self, akind: int | None = None, avalue: float | str | None = None, arank: int = 0, atext: str = "?") -> None: ...

class Ref3D(tuple):
    coords: tuple[int, int, int, int, int, int]
    relflags: tuple[int, int, int, int, int, int]
    shtxlo: int
    shtxhi: int
    rowxlo: int
    rowxhi: int
    colxlo: int
    colxhi: int
    def __init__(self, atuple: tuple[int, int, int, int, int, int, int, int, int, int, int, int]) -> None: ...

def evaluate_name_formula(bk: book.Book, nobj: book.Name, namex: str, blah: int = 0, level: int = 0) -> None: ...
def decompile_formula(
    bk: book.Book,
    fmla: bytes,
    fmlalen: int,
    fmlatype: int | None = None,
    browx: int | None = None,
    bcolx: int | None = None,
    blah: int = 0,
    level: int = 0,
    r1c1: int = 0,
): ...
def dump_formula(bk: book.Book, data: bytes, fmlalen: int, bv: int, reldelta: int, blah: int = 0, isname: int = 0) -> None: ...
def cellname(rowx: int, colx: int) -> str: ...
def cellnameabs(rowx: int, colx: int, r1c1: int = 0) -> str: ...
def colname(colx: int) -> str: ...
def rangename3d(book: book.Book, ref3d: Ref3D) -> str: ...
def rangename3drel(book: book.Book, ref3d: Ref3D, browx: int | None = None, bcolx: int | None = None, r1c1: int = 0): ...
