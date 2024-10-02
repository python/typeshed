import os
import sys
from _ast import *
from _typeshed import ReadableBuffer, Unused
from collections.abc import Iterator
from typing import Any, Literal, TypeVar as _TypeVar, overload
from typing_extensions import deprecated

class _ABC(type):
    if sys.version_info >= (3, 9):
        def __init__(cls, *args: Unused) -> None: ...

if sys.version_info < (3, 14):
    @deprecated("Replaced by ast.Constant; removed in Python 3.14")
    class Num(Constant, metaclass=_ABC):
        value: int | float | complex

    @deprecated("Replaced by ast.Constant; removed in Python 3.14")
    class Str(Constant, metaclass=_ABC):
        value: str
        # Aliases for value, for backwards compatibility
        s: str

    @deprecated("Replaced by ast.Constant; removed in Python 3.14")
    class Bytes(Constant, metaclass=_ABC):
        value: bytes
        # Aliases for value, for backwards compatibility
        s: bytes

    @deprecated("Replaced by ast.Constant; removed in Python 3.14")
    class NameConstant(Constant, metaclass=_ABC): ...

    @deprecated("Replaced by ast.Constant; removed in Python 3.14")
    class Ellipsis(Constant, metaclass=_ABC): ...

if sys.version_info >= (3, 9):
    class slice(AST): ...
    class ExtSlice(slice): ...
    class Index(slice): ...
    class Suite(mod): ...
    class AugLoad(expr_context): ...
    class AugStore(expr_context): ...
    class Param(expr_context): ...

class NodeVisitor:
    def visit(self, node: AST) -> Any: ...
    def generic_visit(self, node: AST) -> Any: ...
    def visit_Module(self, node: Module) -> Any: ...
    def visit_Interactive(self, node: Interactive) -> Any: ...
    def visit_Expression(self, node: Expression) -> Any: ...
    def visit_FunctionDef(self, node: FunctionDef) -> Any: ...
    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> Any: ...
    def visit_ClassDef(self, node: ClassDef) -> Any: ...
    def visit_Return(self, node: Return) -> Any: ...
    def visit_Delete(self, node: Delete) -> Any: ...
    def visit_Assign(self, node: Assign) -> Any: ...
    def visit_AugAssign(self, node: AugAssign) -> Any: ...
    def visit_AnnAssign(self, node: AnnAssign) -> Any: ...
    def visit_For(self, node: For) -> Any: ...
    def visit_AsyncFor(self, node: AsyncFor) -> Any: ...
    def visit_While(self, node: While) -> Any: ...
    def visit_If(self, node: If) -> Any: ...
    def visit_With(self, node: With) -> Any: ...
    def visit_AsyncWith(self, node: AsyncWith) -> Any: ...
    def visit_Raise(self, node: Raise) -> Any: ...
    def visit_Try(self, node: Try) -> Any: ...
    def visit_Assert(self, node: Assert) -> Any: ...
    def visit_Import(self, node: Import) -> Any: ...
    def visit_ImportFrom(self, node: ImportFrom) -> Any: ...
    def visit_Global(self, node: Global) -> Any: ...
    def visit_Nonlocal(self, node: Nonlocal) -> Any: ...
    def visit_Expr(self, node: Expr) -> Any: ...
    def visit_Pass(self, node: Pass) -> Any: ...
    def visit_Break(self, node: Break) -> Any: ...
    def visit_Continue(self, node: Continue) -> Any: ...
    def visit_Slice(self, node: Slice) -> Any: ...
    def visit_BoolOp(self, node: BoolOp) -> Any: ...
    def visit_BinOp(self, node: BinOp) -> Any: ...
    def visit_UnaryOp(self, node: UnaryOp) -> Any: ...
    def visit_Lambda(self, node: Lambda) -> Any: ...
    def visit_IfExp(self, node: IfExp) -> Any: ...
    def visit_Dict(self, node: Dict) -> Any: ...
    def visit_Set(self, node: Set) -> Any: ...
    def visit_ListComp(self, node: ListComp) -> Any: ...
    def visit_SetComp(self, node: SetComp) -> Any: ...
    def visit_DictComp(self, node: DictComp) -> Any: ...
    def visit_GeneratorExp(self, node: GeneratorExp) -> Any: ...
    def visit_Await(self, node: Await) -> Any: ...
    def visit_Yield(self, node: Yield) -> Any: ...
    def visit_YieldFrom(self, node: YieldFrom) -> Any: ...
    def visit_Compare(self, node: Compare) -> Any: ...
    def visit_Call(self, node: Call) -> Any: ...
    def visit_FormattedValue(self, node: FormattedValue) -> Any: ...
    def visit_JoinedStr(self, node: JoinedStr) -> Any: ...
    def visit_Constant(self, node: Constant) -> Any: ...
    def visit_NamedExpr(self, node: NamedExpr) -> Any: ...
    def visit_TypeIgnore(self, node: TypeIgnore) -> Any: ...
    def visit_Attribute(self, node: Attribute) -> Any: ...
    def visit_Subscript(self, node: Subscript) -> Any: ...
    def visit_Starred(self, node: Starred) -> Any: ...
    def visit_Name(self, node: Name) -> Any: ...
    def visit_List(self, node: List) -> Any: ...
    def visit_Tuple(self, node: Tuple) -> Any: ...
    def visit_Del(self, node: Del) -> Any: ...
    def visit_Load(self, node: Load) -> Any: ...
    def visit_Store(self, node: Store) -> Any: ...
    def visit_And(self, node: And) -> Any: ...
    def visit_Or(self, node: Or) -> Any: ...
    def visit_Add(self, node: Add) -> Any: ...
    def visit_BitAnd(self, node: BitAnd) -> Any: ...
    def visit_BitOr(self, node: BitOr) -> Any: ...
    def visit_BitXor(self, node: BitXor) -> Any: ...
    def visit_Div(self, node: Div) -> Any: ...
    def visit_FloorDiv(self, node: FloorDiv) -> Any: ...
    def visit_LShift(self, node: LShift) -> Any: ...
    def visit_Mod(self, node: Mod) -> Any: ...
    def visit_Mult(self, node: Mult) -> Any: ...
    def visit_MatMult(self, node: MatMult) -> Any: ...
    def visit_Pow(self, node: Pow) -> Any: ...
    def visit_RShift(self, node: RShift) -> Any: ...
    def visit_Sub(self, node: Sub) -> Any: ...
    def visit_Invert(self, node: Invert) -> Any: ...
    def visit_Not(self, node: Not) -> Any: ...
    def visit_UAdd(self, node: UAdd) -> Any: ...
    def visit_USub(self, node: USub) -> Any: ...
    def visit_Eq(self, node: Eq) -> Any: ...
    def visit_Gt(self, node: Gt) -> Any: ...
    def visit_GtE(self, node: GtE) -> Any: ...
    def visit_In(self, node: In) -> Any: ...
    def visit_Is(self, node: Is) -> Any: ...
    def visit_IsNot(self, node: IsNot) -> Any: ...
    def visit_Lt(self, node: Lt) -> Any: ...
    def visit_LtE(self, node: LtE) -> Any: ...
    def visit_NotEq(self, node: NotEq) -> Any: ...
    def visit_NotIn(self, node: NotIn) -> Any: ...
    def visit_comprehension(self, node: comprehension) -> Any: ...
    def visit_ExceptHandler(self, node: ExceptHandler) -> Any: ...
    def visit_arguments(self, node: arguments) -> Any: ...
    def visit_arg(self, node: arg) -> Any: ...
    def visit_keyword(self, node: keyword) -> Any: ...
    def visit_alias(self, node: alias) -> Any: ...
    def visit_withitem(self, node: withitem) -> Any: ...
    if sys.version_info >= (3, 10):
        def visit_Match(self, node: Match) -> Any: ...
        def visit_match_case(self, node: match_case) -> Any: ...
        def visit_MatchValue(self, node: MatchValue) -> Any: ...
        def visit_MatchSequence(self, node: MatchSequence) -> Any: ...
        def visit_MatchSingleton(self, node: MatchSingleton) -> Any: ...
        def visit_MatchStar(self, node: MatchStar) -> Any: ...
        def visit_MatchMapping(self, node: MatchMapping) -> Any: ...
        def visit_MatchClass(self, node: MatchClass) -> Any: ...
        def visit_MatchAs(self, node: MatchAs) -> Any: ...
        def visit_MatchOr(self, node: MatchOr) -> Any: ...

    if sys.version_info >= (3, 11):
        def visit_TryStar(self, node: TryStar) -> Any: ...

    if sys.version_info >= (3, 12):
        def visit_TypeVar(self, node: TypeVar) -> Any: ...
        def visit_ParamSpec(self, node: ParamSpec) -> Any: ...
        def visit_TypeVarTuple(self, node: TypeVarTuple) -> Any: ...
        def visit_TypeAlias(self, node: TypeAlias) -> Any: ...

    # visit methods for deprecated nodes
    def visit_ExtSlice(self, node: ExtSlice) -> Any: ...
    def visit_Index(self, node: Index) -> Any: ...
    def visit_Suite(self, node: Suite) -> Any: ...
    def visit_AugLoad(self, node: AugLoad) -> Any: ...
    def visit_AugStore(self, node: AugStore) -> Any: ...
    def visit_Param(self, node: Param) -> Any: ...
    def visit_Num(self, node: Num) -> Any: ...
    def visit_Str(self, node: Str) -> Any: ...
    def visit_Bytes(self, node: Bytes) -> Any: ...
    def visit_NameConstant(self, node: NameConstant) -> Any: ...
    def visit_Ellipsis(self, node: Ellipsis) -> Any: ...

class NodeTransformer(NodeVisitor):
    def generic_visit(self, node: AST) -> AST: ...
    # TODO: Override the visit_* methods with better return types.
    #       The usual return type is AST | None, but Iterable[AST]
    #       is also allowed in some cases -- this needs to be mapped.

_T = _TypeVar("_T", bound=AST)

if sys.version_info >= (3, 13):
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any] = "<unknown>",
        mode: Literal["exec"] = "exec",
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> Module: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["eval"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> Expression: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["func_type"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> FunctionType: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["single"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> Interactive: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["eval"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> Expression: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["func_type"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> FunctionType: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["single"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> Interactive: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any] = "<unknown>",
        mode: str = "exec",
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
        optimize: Literal[-1, 0, 1, 2] = -1,
    ) -> AST: ...

else:
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any] = "<unknown>",
        mode: Literal["exec"] = "exec",
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> Module: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["eval"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> Expression: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["func_type"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> FunctionType: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any],
        mode: Literal["single"],
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> Interactive: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["eval"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> Expression: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["func_type"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> FunctionType: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        *,
        mode: Literal["single"],
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> Interactive: ...
    @overload
    def parse(
        source: str | ReadableBuffer,
        filename: str | ReadableBuffer | os.PathLike[Any] = "<unknown>",
        mode: str = "exec",
        *,
        type_comments: bool = False,
        feature_version: None | int | tuple[int, int] = None,
    ) -> AST: ...

if sys.version_info >= (3, 9):
    def unparse(ast_obj: AST) -> str: ...

def copy_location(new_node: _T, old_node: AST) -> _T: ...

if sys.version_info >= (3, 13):
    def dump(
        node: AST,
        annotate_fields: bool = True,
        include_attributes: bool = False,
        *,
        indent: int | str | None = None,
        show_empty: bool = False,
    ) -> str: ...

elif sys.version_info >= (3, 9):
    def dump(
        node: AST, annotate_fields: bool = True, include_attributes: bool = False, *, indent: int | str | None = None
    ) -> str: ...

else:
    def dump(node: AST, annotate_fields: bool = True, include_attributes: bool = False) -> str: ...

def fix_missing_locations(node: _T) -> _T: ...
def get_docstring(node: AsyncFunctionDef | FunctionDef | ClassDef | Module, clean: bool = True) -> str | None: ...
def increment_lineno(node: _T, n: int = 1) -> _T: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def iter_fields(node: AST) -> Iterator[tuple[str, Any]]: ...
def literal_eval(node_or_string: str | AST) -> Any: ...
def get_source_segment(source: str, node: AST, *, padded: bool = False) -> str | None: ...
def walk(node: AST) -> Iterator[AST]: ...

if sys.version_info >= (3, 9):
    def main() -> None: ...

if sys.version_info >= (3, 14):
    def compare(left: AST, right: AST, /, *, compare_attributes: bool = False) -> bool: ...
