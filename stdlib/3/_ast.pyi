import sys
import typing
from typing import Any, Optional, ClassVar

PyCF_ONLY_AST = ...  # type: int

_identifier = str

class AST:
    _attributes: ClassVar[typing.Tuple[str, ...]]
    _fields: ClassVar[typing.Tuple[str, ...]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    # TODO: Not all nodes have all of the following attributes
    lineno: int
    col_offset: int
    if sys.version_info >= (3, 8):
        end_lineno: Optional[int]
        end_col_offset: Optional[int]
        type_comment: Optional[str]

class mod(AST):
    ...

if sys.version_info >= (3, 8):
    class type_ignore(AST): ...

    class TypeIgnore(type_ignore): ...

    class FunctionType(mod):
        argtypes: typing.List[expr]
        returns: expr

class Module(mod):
    body = ...  # type: typing.List[stmt]
    if sys.version_info >= (3, 7):
        docstring: Optional[str]
    if sys.version_info >= (3, 8):
        type_ignores: typing.List[TypeIgnore]

class Interactive(mod):
    body = ...  # type: typing.List[stmt]

class Expression(mod):
    body = ...  # type: expr

class Suite(mod):
    body = ...  # type: typing.List[stmt]


class stmt(AST): ...

class FunctionDef(stmt):
    name = ...  # type: _identifier
    args = ...  # type: arguments
    body = ...  # type: typing.List[stmt]
    decorator_list = ...  # type: typing.List[expr]
    returns = ...  # type: Optional[expr]
    if sys.version_info >= (3, 7):
        docstring: Optional[str]

class AsyncFunctionDef(stmt):
    name = ...  # type: _identifier
    args = ...  # type: arguments
    body = ...  # type: typing.List[stmt]
    decorator_list = ...  # type: typing.List[expr]
    returns = ...  # type: Optional[expr]
    if sys.version_info >= (3, 7):
        docstring: Optional[str]

class ClassDef(stmt):
    name = ...  # type: _identifier
    bases = ...  # type: typing.List[expr]
    keywords = ...  # type: typing.List[keyword]
    body = ...  # type: typing.List[stmt]
    decorator_list = ...  # type: typing.List[expr]
    if sys.version_info >= (3, 7):
        docstring: Optional[str]

class Return(stmt):
    value = ...  # type: Optional[expr]

class Delete(stmt):
    targets = ...  # type: typing.List[expr]

class Assign(stmt):
    targets = ...  # type: typing.List[expr]
    value = ...  # type: expr

class AugAssign(stmt):
    target = ...  # type: expr
    op = ...  # type: operator
    value = ...  # type: expr

if sys.version_info >= (3, 6):
    class AnnAssign(stmt):
        target = ...  # type: expr
        annotation = ...  # type: expr
        value = ...  # type: Optional[expr]
        simple = ...  # type: int

class For(stmt):
    target = ...  # type: expr
    iter = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class AsyncFor(stmt):
    target = ...  # type: expr
    iter = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class While(stmt):
    test = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class If(stmt):
    test = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class With(stmt):
    items = ...  # type: typing.List[withitem]
    body = ...  # type: typing.List[stmt]

class AsyncWith(stmt):
    items = ...  # type: typing.List[withitem]
    body = ...  # type: typing.List[stmt]

class Raise(stmt):
    exc = ...  # type: Optional[expr]
    cause = ...  # type: Optional[expr]

class Try(stmt):
    body = ...  # type: typing.List[stmt]
    handlers = ...  # type: typing.List[ExceptHandler]
    orelse = ...  # type: typing.List[stmt]
    finalbody = ...  # type: typing.List[stmt]

class Assert(stmt):
    test = ...  # type: expr
    msg = ...  # type: Optional[expr]

class Import(stmt):
    names = ...  # type: typing.List[alias]

class ImportFrom(stmt):
    module = ...  # type: Optional[_identifier]
    names = ...  # type: typing.List[alias]
    level = ...  # type: int

class Global(stmt):
    names = ...  # type: typing.List[_identifier]

class Nonlocal(stmt):
    names = ...  # type: typing.List[_identifier]

class Expr(stmt):
    value = ...  # type: expr

class Pass(stmt): ...
class Break(stmt): ...
class Continue(stmt): ...


class slice(AST):
    ...

_slice = slice  # this lets us type the variable named 'slice' below

class Slice(slice):
    lower = ...  # type: Optional[expr]
    upper = ...  # type: Optional[expr]
    step = ...  # type: Optional[expr]

class ExtSlice(slice):
    dims = ...  # type: typing.List[slice]

class Index(slice):
    value = ...  # type: expr


class expr(AST): ...

class BoolOp(expr):
    op = ...  # type: boolop
    values = ...  # type: typing.List[expr]

class BinOp(expr):
    left = ...  # type: expr
    op = ...  # type: operator
    right = ...  # type: expr

class UnaryOp(expr):
    op = ...  # type: unaryop
    operand = ...  # type: expr

class Lambda(expr):
    args = ...  # type: arguments
    body = ...  # type: expr

class IfExp(expr):
    test = ...  # type: expr
    body = ...  # type: expr
    orelse = ...  # type: expr

class Dict(expr):
    keys = ...  # type: typing.List[expr]
    values = ...  # type: typing.List[expr]

class Set(expr):
    elts = ...  # type: typing.List[expr]

class ListComp(expr):
    elt = ...  # type: expr
    generators = ...  # type: typing.List[comprehension]

class SetComp(expr):
    elt = ...  # type: expr
    generators = ...  # type: typing.List[comprehension]

class DictComp(expr):
    key = ...  # type: expr
    value = ...  # type: expr
    generators = ...  # type: typing.List[comprehension]

class GeneratorExp(expr):
    elt = ...  # type: expr
    generators = ...  # type: typing.List[comprehension]

class Await(expr):
    value = ...  # type: expr

class Yield(expr):
    value = ...  # type: Optional[expr]

class YieldFrom(expr):
    value = ...  # type: expr

class Compare(expr):
    left = ...  # type: expr
    ops = ...  # type: typing.List[cmpop]
    comparators = ...  # type: typing.List[expr]

class Call(expr):
    func = ...  # type: expr
    args = ...  # type: typing.List[expr]
    keywords = ...  # type: typing.List[keyword]

class Num(expr):  # Deprecated in 3.8; use Constant
    n = ...  # type: complex

class Str(expr):  # Deprecated in 3.8; use Constant
    s = ...  # type: str

if sys.version_info >= (3, 6):
    class FormattedValue(expr):
        value = ...  # type: expr
        conversion = ...  # type: Optional[int]
        format_spec = ...  # type: Optional[expr]

    class JoinedStr(expr):
        values = ...  # type: typing.List[expr]

class Bytes(expr):  # Deprecated in 3.8; use Constant
    s = ...  # type: bytes

class NameConstant(expr):
    value = ...  # type: Any

if sys.version_info >= (3, 8):
    class Constant(expr):
        value: Any  # None, str, bytes, bool, int, float, complex, Ellipsis
        kind: Optional[str]
        # Aliases for value, for backwards compatibility
        s: Any
        n: complex

    class NamedExpr(expr):
        target: expr
        value: expr

class Ellipsis(expr): ...

class Attribute(expr):
    value = ...  # type: expr
    attr = ...  # type: _identifier
    ctx = ...  # type: expr_context

class Subscript(expr):
    value = ...  # type: expr
    slice = ...  # type: _slice
    ctx = ...  # type: expr_context

class Starred(expr):
    value = ...  # type: expr
    ctx = ...  # type: expr_context

class Name(expr):
    id = ...  # type: _identifier
    ctx = ...  # type: expr_context

class List(expr):
    elts = ...  # type: typing.List[expr]
    ctx = ...  # type: expr_context

class Tuple(expr):
    elts = ...  # type: typing.List[expr]
    ctx = ...  # type: expr_context


class expr_context(AST):
    ...

class AugLoad(expr_context): ...
class AugStore(expr_context): ...
class Del(expr_context): ...
class Load(expr_context): ...
class Param(expr_context): ...
class Store(expr_context): ...


class boolop(AST):
    ...

class And(boolop): ...
class Or(boolop): ...

class operator(AST):
    ...

class Add(operator): ...
class BitAnd(operator): ...
class BitOr(operator): ...
class BitXor(operator): ...
class Div(operator): ...
class FloorDiv(operator): ...
class LShift(operator): ...
class Mod(operator): ...
class Mult(operator): ...
class MatMult(operator): ...
class Pow(operator): ...
class RShift(operator): ...
class Sub(operator): ...

class unaryop(AST):
    ...

class Invert(unaryop): ...
class Not(unaryop): ...
class UAdd(unaryop): ...
class USub(unaryop): ...

class cmpop(AST):
    ...

class Eq(cmpop): ...
class Gt(cmpop): ...
class GtE(cmpop): ...
class In(cmpop): ...
class Is(cmpop): ...
class IsNot(cmpop): ...
class Lt(cmpop): ...
class LtE(cmpop): ...
class NotEq(cmpop): ...
class NotIn(cmpop): ...


class comprehension(AST):
    target = ...  # type: expr
    iter = ...  # type: expr
    ifs = ...  # type: typing.List[expr]
    if sys.version_info >= (3, 6):
        is_async = ...  # type: int


class excepthandler(AST):
    ...

class ExceptHandler(excepthandler):
    type = ...  # type: Optional[expr]
    name = ...  # type: Optional[_identifier]
    body = ...  # type: typing.List[stmt]


class arguments(AST):
    args = ...  # type: typing.List[arg]
    vararg = ...  # type: Optional[arg]
    kwonlyargs = ...  # type: typing.List[arg]
    kw_defaults = ...  # type: typing.List[expr]
    kwarg = ...  # type: Optional[arg]
    defaults = ...  # type: typing.List[expr]

class arg(AST):
    arg = ...  # type: _identifier
    annotation = ...  # type: Optional[expr]

class keyword(AST):
    arg = ...  # type: Optional[_identifier]
    value = ...  # type: expr

class alias(AST):
    name = ...  # type: _identifier
    asname = ...  # type: Optional[_identifier]

class withitem(AST):
    context_expr = ...  # type: expr
    optional_vars = ...  # type: Optional[expr]
