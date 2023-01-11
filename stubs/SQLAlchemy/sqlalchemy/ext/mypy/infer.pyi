from collections.abc import Sequence

# mypy_test can't find mypy import
from mypy.nodes import AssignmentStmt, Expression, RefExpr, TypeInfo, Var  # type: ignore[import]
from mypy.plugin import SemanticAnalyzerPluginInterface  # type: ignore[import]
from mypy.types import ProperType  # type: ignore[import]

def infer_type_from_right_hand_nameexpr(
    api: SemanticAnalyzerPluginInterface,
    stmt: AssignmentStmt,
    node: Var,
    left_hand_explicit_type: ProperType | None,
    infer_from_right_side: RefExpr,
) -> ProperType | None: ...
def infer_type_from_left_hand_type_only(
    api: SemanticAnalyzerPluginInterface, node: Var, left_hand_explicit_type: ProperType | None
) -> ProperType | None: ...
def extract_python_type_from_typeengine(
    api: SemanticAnalyzerPluginInterface, node: TypeInfo, type_args: Sequence[Expression]
) -> ProperType: ...
