from typing import Any

ClassDef = Any  # from mypy.nodes
Expression = Any  # from mypy.nodes
MemberExpr = Any  # from mypy.nodes
NameExpr = Any  # from mypy.nodes
SymbolNode = Any  # from mypy.nodes
TypeInfo = Any  # from mypy.nodes
StrExpr = Any  # from mypy.nodes
SemanticAnalyzerPluginInterface = Any  # from mypy.plugin
UnboundType = Any  # from mypy.types

COLUMN: int
RELATIONSHIP: int
REGISTRY: int
COLUMN_PROPERTY: int
TYPEENGINE: int
MAPPED: int
DECLARATIVE_BASE: int
DECLARATIVE_META: int
MAPPED_DECORATOR: int
SYNONYM_PROPERTY: int
COMPOSITE_PROPERTY: int
DECLARED_ATTR: int
MAPPER_PROPERTY: int
AS_DECLARATIVE: int
AS_DECLARATIVE_BASE: int
DECLARATIVE_MIXIN: int
QUERY_EXPRESSION: int

def has_base_type_id(info: TypeInfo, type_id: int) -> bool: ...
def mro_has_id(mro: list[TypeInfo], type_id: int) -> bool: ...
def type_id_for_unbound_type(type_: UnboundType, cls: ClassDef, api: SemanticAnalyzerPluginInterface) -> int | None: ...
def type_id_for_callee(callee: Expression) -> int | None: ...
def type_id_for_named_node(node: NameExpr | MemberExpr | SymbolNode) -> int | None: ...
def type_id_for_fullname(fullname: str) -> int | None: ...
