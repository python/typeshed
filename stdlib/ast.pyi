import os
import sys
import typing_extensions
from _ast import (
    PyCF_ALLOW_TOP_LEVEL_AWAIT as PyCF_ALLOW_TOP_LEVEL_AWAIT,
    PyCF_ONLY_AST as PyCF_ONLY_AST,
    PyCF_TYPE_COMMENTS as PyCF_TYPE_COMMENTS,
)
from _typeshed import ReadableBuffer, Unused
from collections.abc import Iterator
from typing import Any, ClassVar, Literal, TypeVar as _TypeVar, overload
from typing_extensions import deprecated

_Identifier: typing_extensions.TypeAlias = str

# The various AST classes are implemented in C, and imported from _ast at runtime,
# on 3.9 and higer they consider themselves to live in the ast module,
# so we'll define the stubs in this file. This means that 3.8 will have the incorrect
# __module__ values instead, but the majority of python versions are better off this way.
class AST:
    if sys.version_info >= (3, 10):
        __match_args__ = ()
    _attributes: ClassVar[tuple[str, ...]]
    _fields: ClassVar[tuple[str, ...]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    # TODO: Not all nodes have all of the following attributes
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    type_comment: str | None

class mod(AST): ...

class Module(mod):
    if sys.version_info >= (3, 10):
        __match_args__ = ("body", "type_ignores")
    body: list[stmt]
    type_ignores: list[TypeIgnore]

class Interactive(mod):
    if sys.version_info >= (3, 10):
        __match_args__ = ("body",)
    body: list[stmt]

class Expression(mod):
    if sys.version_info >= (3, 10):
        __match_args__ = ("body",)
    body: expr

class FunctionType(mod):
    if sys.version_info >= (3, 10):
        __match_args__ = ("argtypes", "returns")
    argtypes: list[expr]
    returns: expr

class stmt(AST): ...

class FunctionDef(stmt):
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment")
    name: _Identifier
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    if sys.version_info >= (3, 12):
        type_params: list[type_param]

class AsyncFunctionDef(stmt):
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment")
    name: _Identifier
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    if sys.version_info >= (3, 12):
        type_params: list[type_param]

class ClassDef(stmt):
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "bases", "keywords", "body", "decorator_list", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "bases", "keywords", "body", "decorator_list")
    name: _Identifier
    bases: list[expr]
    keywords: list[keyword]
    body: list[stmt]
    decorator_list: list[expr]
    if sys.version_info >= (3, 12):
        type_params: list[type_param]

class Return(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr | None

class Delete(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("targets",)
    targets: list[expr]

class Assign(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("targets", "value", "type_comment")
    targets: list[expr]
    value: expr

if sys.version_info >= (3, 12):
    class TypeAlias(stmt):
        __match_args__ = ("name", "type_params", "value")
        name: Name
        type_params: list[type_param]
        value: expr

class AugAssign(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "op", "value")
    target: Name | Attribute | Subscript
    op: operator
    value: expr

class AnnAssign(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "annotation", "value", "simple")
    target: Name | Attribute | Subscript
    annotation: expr
    value: expr | None
    simple: int

class For(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "body", "orelse", "type_comment")
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]

class AsyncFor(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "body", "orelse", "type_comment")
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]

class While(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: list[stmt]
    orelse: list[stmt]

class If(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: list[stmt]
    orelse: list[stmt]

class With(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("items", "body", "type_comment")
    items: list[withitem]
    body: list[stmt]

class AsyncWith(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("items", "body", "type_comment")
    items: list[withitem]
    body: list[stmt]

if sys.version_info >= (3, 10):
    class Match(stmt):
        __match_args__ = ("subject", "cases")
        subject: expr
        cases: list[match_case]

class Raise(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("exc", "cause")
    exc: expr | None
    cause: expr | None

class Try(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("body", "handlers", "orelse", "finalbody")
    body: list[stmt]
    handlers: list[ExceptHandler]
    orelse: list[stmt]
    finalbody: list[stmt]

if sys.version_info >= (3, 11):
    class TryStar(stmt):
        __match_args__ = ("body", "handlers", "orelse", "finalbody")
        body: list[stmt]
        handlers: list[ExceptHandler]
        orelse: list[stmt]
        finalbody: list[stmt]

class Assert(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "msg")
    test: expr
    msg: expr | None

class Import(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[alias]

class ImportFrom(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("module", "names", "level")
    module: str | None
    names: list[alias]
    level: int

class Global(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[_Identifier]

class Nonlocal(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[_Identifier]

class Expr(stmt):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr

class Pass(stmt): ...
class Break(stmt): ...
class Continue(stmt): ...
class expr(AST): ...

class BoolOp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("op", "values")
    op: boolop
    values: list[expr]

class NamedExpr(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "value")
    target: Name
    value: expr

class BinOp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("left", "op", "right")
    left: expr
    op: operator
    right: expr

class UnaryOp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("op", "operand")
    op: unaryop
    operand: expr

class Lambda(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("args", "body")
    args: arguments
    body: expr

class IfExp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: expr
    orelse: expr

class Dict(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("keys", "values")
    keys: list[expr | None]
    values: list[expr]

class Set(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts",)
    elts: list[expr]

class ListComp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]

class SetComp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]

class DictComp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("key", "value", "generators")
    key: expr
    value: expr
    generators: list[comprehension]

class GeneratorExp(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]

class Await(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr

class Yield(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr | None

class YieldFrom(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr

class Compare(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("left", "ops", "comparators")
    left: expr
    ops: list[cmpop]
    comparators: list[expr]

class Call(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("func", "args", "keywords")
    func: expr
    args: list[expr]
    keywords: list[keyword]

class FormattedValue(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "conversion", "format_spec")
    value: expr
    conversion: int
    format_spec: expr | None

class JoinedStr(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("values",)
    values: list[expr]

class Constant(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "kind")
    value: Any  # None, str, bytes, bool, int, float, complex, Ellipsis
    kind: str | None
    # Aliases for value, for backwards compatibility
    s: Any
    n: int | float | complex

class Attribute(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "attr", "ctx")
    value: expr
    attr: _Identifier
    ctx: expr_context

class Subscript(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "slice", "ctx")
    value: expr
    if sys.version_info >= (3, 9):
        slice: expr
    else:
        slice: _Slice
    ctx: expr_context

class Starred(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "ctx")
    value: expr
    ctx: expr_context

class Name(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("id", "ctx")
    id: _Identifier
    ctx: expr_context

class List(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts", "ctx")
    elts: list[expr]
    ctx: expr_context

class Tuple(expr):
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts", "ctx")
    elts: list[expr]
    ctx: expr_context
    if sys.version_info >= (3, 9):
        dims: list[expr]

class slice(AST): ...  # deprecated and moved to ast.py for >= (3, 9)

if sys.version_info < (3, 9):
    # alias for use with variables named slice
    # that's just older versions of the Subscript class right now
    _Slice: typing_extensions.TypeAlias = slice

if sys.version_info >= (3, 9):
    class Slice(expr):
        if sys.version_info >= (3, 10):
            __match_args__ = ("lower", "upper", "step")
        lower: expr | None
        upper: expr | None
        step: expr | None

else:
    class Slice(slice):
        if sys.version_info >= (3, 10):
            __match_args__ = ("lower", "upper", "step")
        lower: expr | None
        upper: expr | None
        step: expr | None

class ExtSlice(slice):  # deprecated and moved to ast.py if sys.version_info >= (3, 9)
    dims: list[slice]

class Index(slice):  # deprecated and moved to ast.py if sys.version_info >= (3, 9)
    value: expr

class expr_context(AST): ...
class AugLoad(expr_context): ...  # deprecated and moved to ast.py if sys.version_info >= (3, 9)
class AugStore(expr_context): ...  # deprecated and moved to ast.py if sys.version_info >= (3, 9)
class Param(expr_context): ...  # deprecated and moved to ast.py if sys.version_info >= (3, 9)

class Suite(mod):  # deprecated and moved to ast.py if sys.version_info >= (3, 9)
    body: list[stmt]

class Load(expr_context): ...
class Store(expr_context): ...
class Del(expr_context): ...
class boolop(AST): ...
class And(boolop): ...
class Or(boolop): ...
class operator(AST): ...
class Add(operator): ...
class Sub(operator): ...
class Mult(operator): ...
class MatMult(operator): ...
class Div(operator): ...
class Mod(operator): ...
class Pow(operator): ...
class LShift(operator): ...
class RShift(operator): ...
class BitOr(operator): ...
class BitXor(operator): ...
class BitAnd(operator): ...
class FloorDiv(operator): ...
class unaryop(AST): ...
class Invert(unaryop): ...
class Not(unaryop): ...
class UAdd(unaryop): ...
class USub(unaryop): ...
class cmpop(AST): ...
class Eq(cmpop): ...
class NotEq(cmpop): ...
class Lt(cmpop): ...
class LtE(cmpop): ...
class Gt(cmpop): ...
class GtE(cmpop): ...
class Is(cmpop): ...
class IsNot(cmpop): ...
class In(cmpop): ...
class NotIn(cmpop): ...

class comprehension(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "ifs", "is_async")
    target: expr
    iter: expr
    ifs: list[expr]
    is_async: int

class excepthandler(AST): ...

class ExceptHandler(excepthandler):
    if sys.version_info >= (3, 10):
        __match_args__ = ("type", "name", "body")
    type: expr | None
    name: _Identifier | None
    body: list[stmt]

class arguments(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("posonlyargs", "args", "vararg", "kwonlyargs", "kw_defaults", "kwarg", "defaults")
    posonlyargs: list[arg]
    args: list[arg]
    vararg: arg | None
    kwonlyargs: list[arg]
    kw_defaults: list[expr | None]
    kwarg: arg | None
    defaults: list[expr]

class arg(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("arg", "annotation", "type_comment")
    arg: _Identifier
    annotation: expr | None

class keyword(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("arg", "value")
    arg: _Identifier | None
    value: expr

class alias(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("name", "asname")
    name: _Identifier
    asname: _Identifier | None

class withitem(AST):
    if sys.version_info >= (3, 10):
        __match_args__ = ("context_expr", "optional_vars")
    context_expr: expr
    optional_vars: expr | None

if sys.version_info >= (3, 10):
    class match_case(AST):
        __match_args__ = ("pattern", "guard", "body")
        pattern: _Pattern
        guard: expr | None
        body: list[stmt]

    class pattern(AST): ...
    # Without the alias, Pyright complains variables named pattern are recursively defined
    _Pattern: typing_extensions.TypeAlias = pattern

    class MatchValue(pattern):
        __match_args__ = ("value",)
        value: expr

    class MatchSingleton(pattern):
        __match_args__ = ("value",)
        value: Literal[True, False] | None

    class MatchSequence(pattern):
        __match_args__ = ("patterns",)
        patterns: list[pattern]

    class MatchMapping(pattern):
        __match_args__ = ("keys", "patterns", "rest")
        keys: list[expr]
        patterns: list[pattern]
        rest: _Identifier | None

    class MatchClass(pattern):
        __match_args__ = ("cls", "patterns", "kwd_attrs", "kwd_patterns")
        cls: expr
        patterns: list[pattern]
        kwd_attrs: list[_Identifier]
        kwd_patterns: list[pattern]

    class MatchStar(pattern):
        __match_args__ = ("name",)
        name: _Identifier | None

    class MatchAs(pattern):
        __match_args__ = ("pattern", "name")
        pattern: _Pattern | None
        name: _Identifier | None

    class MatchOr(pattern):
        __match_args__ = ("patterns",)
        patterns: list[pattern]

class type_ignore(AST): ...

class TypeIgnore(type_ignore):
    if sys.version_info >= (3, 10):
        __match_args__ = ("lineno", "tag")
    tag: str

if sys.version_info >= (3, 12):
    class type_param(AST): ...

    class TypeVar(type_param):
        __match_args__ = ("name", "bound")
        name: _Identifier
        bound: expr | None

    class ParamSpec(type_param):
        __match_args__ = ("name",)
        name: _Identifier

    class TypeVarTuple(type_param):
        __match_args__ = ("name",)
        name: _Identifier

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

# everything below here is defined in ast.py

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

def literal_eval(node_or_string: str | AST) -> Any: ...

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

def copy_location(new_node: _T, old_node: AST) -> _T: ...
def fix_missing_locations(node: _T) -> _T: ...
def increment_lineno(node: _T, n: int = 1) -> _T: ...
def iter_fields(node: AST) -> Iterator[tuple[str, Any]]: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def get_docstring(node: AsyncFunctionDef | FunctionDef | ClassDef | Module, clean: bool = True) -> str | None: ...
def get_source_segment(source: str, node: AST, *, padded: bool = False) -> str | None: ...
def walk(node: AST) -> Iterator[AST]: ...

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

if sys.version_info >= (3, 9):
    def unparse(ast_obj: AST) -> str: ...

if sys.version_info >= (3, 9):
    def main() -> None: ...

if sys.version_info >= (3, 14):
    def compare(left: AST, right: AST, /, *, compare_attributes: bool = False) -> bool: ...
