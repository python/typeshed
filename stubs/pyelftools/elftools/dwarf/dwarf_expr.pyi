from _typeshed import Incomplete
from typing import NamedTuple

DW_OP_name2opcode: Incomplete
DW_OP_opcode2name: Incomplete

class DWARFExprOp(NamedTuple):
    op: Incomplete
    op_name: Incomplete
    args: Incomplete
    offset: Incomplete

class DWARFExprParser:
    def __init__(self, structs) -> None: ...
    def parse_expr(self, expr): ...
