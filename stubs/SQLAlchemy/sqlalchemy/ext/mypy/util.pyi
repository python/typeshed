from collections.abc import Iterable, Iterator
from typing import Any, TypeVar, overload
from typing_extensions import TypeAlias

CallExpr: TypeAlias = Any  # from mypy.nodes
Context: TypeAlias = Any  # from mypy.nodes
Expression: TypeAlias = Any  # from mypy.nodes
JsonDict: TypeAlias = Any  # from mypy.nodes
NameExpr: TypeAlias = Any  # from mypy.nodes
Statement: TypeAlias = Any  # from mypy.nodes
TypeInfo: TypeAlias = Any  # from mypy.nodes
ClassDefContext: TypeAlias = Any  # from mypy.plugin
DynamicClassDefContext: TypeAlias = Any  # from mypy.plugin
SemanticAnalyzerPluginInterface: TypeAlias = Any  # from mypy.plugin
Type: TypeAlias = Any  # from mypy.types

_TArgType = TypeVar("_TArgType", bound=CallExpr | NameExpr)

class SQLAlchemyAttribute:
    name: Any
    line: Any
    column: Any
    type: Any
    info: Any
    def __init__(self, name: str, line: int, column: int, typ: Type | None, info: TypeInfo) -> None: ...
    def serialize(self) -> JsonDict: ...
    def expand_typevar_from_subtype(self, sub_type: TypeInfo) -> None: ...
    @classmethod
    def deserialize(cls, info: TypeInfo, data: JsonDict, api: SemanticAnalyzerPluginInterface) -> SQLAlchemyAttribute: ...

def name_is_dunder(name): ...
def establish_as_sqlalchemy(info: TypeInfo) -> None: ...
def set_is_base(info: TypeInfo) -> None: ...
def get_is_base(info: TypeInfo) -> bool: ...
def has_declarative_base(info: TypeInfo) -> bool: ...
def set_has_table(info: TypeInfo) -> None: ...
def get_has_table(info: TypeInfo) -> bool: ...
def get_mapped_attributes(info: TypeInfo, api: SemanticAnalyzerPluginInterface) -> list[SQLAlchemyAttribute] | None: ...
def set_mapped_attributes(info: TypeInfo, attributes: list[SQLAlchemyAttribute]) -> None: ...
def fail(api: SemanticAnalyzerPluginInterface, msg: str, ctx: Context) -> None: ...
def add_global(ctx: ClassDefContext | DynamicClassDefContext, module: str, symbol_name: str, asname: str) -> None: ...
@overload
def get_callexpr_kwarg(callexpr: CallExpr, name: str, *, expr_types: None = ...) -> CallExpr | NameExpr | None: ...
@overload
def get_callexpr_kwarg(callexpr: CallExpr, name: str, *, expr_types: tuple[type[_TArgType], ...]) -> _TArgType | None: ...
def flatten_typechecking(stmts: Iterable[Statement]) -> Iterator[Statement]: ...
def unbound_to_instance(api: SemanticAnalyzerPluginInterface, typ: Type) -> Type: ...
def info_for_cls(cls, api: SemanticAnalyzerPluginInterface) -> TypeInfo | None: ...
def expr_to_mapped_constructor(expr: Expression) -> CallExpr: ...
