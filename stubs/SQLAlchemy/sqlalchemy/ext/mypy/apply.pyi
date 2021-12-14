from mypy.nodes import AssignmentStmt, NameExpr, StrExpr
from mypy.plugin import SemanticAnalyzerPluginInterface
from mypy.types import ProperType

from . import util

def apply_mypy_mapped_attr(
    cls, api: SemanticAnalyzerPluginInterface, item: NameExpr | StrExpr, attributes: list[util.SQLAlchemyAttribute]
) -> None: ...
def re_apply_declarative_assignments(
    cls, api: SemanticAnalyzerPluginInterface, attributes: list[util.SQLAlchemyAttribute]
) -> None: ...
def apply_type_to_mapped_statement(
    api: SemanticAnalyzerPluginInterface,
    stmt: AssignmentStmt,
    lvalue: NameExpr,
    left_hand_explicit_type: ProperType | None,
    python_type_for_type: ProperType | None,
) -> None: ...
def add_additional_orm_attributes(
    cls, api: SemanticAnalyzerPluginInterface, attributes: list[util.SQLAlchemyAttribute]
) -> None: ...
