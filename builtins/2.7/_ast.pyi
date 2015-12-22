from typing import Any
from typing import Tuple as TypingTuple

__version__ = ...  # type: int

PyCF_ONLY_AST = ...  # type: int

class AST(object):
    _attributes = ...  # type: TypingTuple[str]
    _fields = ...  # type: TypingTuple[str]
    def __init__(self, *args, **kwargs) -> None: pass

class alias(AST):
    pass

class arguments(AST):
    pass

class boolop(AST):
    pass

class cmpop(AST):
    pass

class comprehension(AST):
    pass

class excepthandler(AST):
    pass

class expr(AST):
    pass

class expr_context(AST):
    pass

class keyword(AST):
    pass

class mod(AST):
    pass

class operator(AST):
    pass

class slice(AST):
    pass

class stmt(AST):
    pass

class unaryop(AST):
    pass


class Add(operator):
    def __init__(self) -> None:
        pass

class And(boolop):
    def __init__(self) -> None:
        pass

class Assert(stmt):
    test = ...  # type: Any
    msg = ...  # type: Any
    def __init__(self, test = ..., msg = ...) -> None:
        pass

class Assign(stmt):
    targets = ...  # type: Any
    value = ...  # type: Any
    def __init__(self, targets = ..., value = ...) -> None:
        pass

class Attribute(expr):
    value = ...  # type: Any
    attr = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, value = ..., attr = ..., ctx = ...) -> None:
        pass

class AugAssign(stmt):
    target = ...  # type: Any
    op = ...  # type: Any
    value = ...  # type: Any
    def __init__(self, target = ..., op = ..., value = ...) -> None:
        pass

class AugLoad(expr_context):
    def __init__(self) -> None:
        pass

class AugStore(expr_context):
    def __init__(self) -> None:
        pass

class BinOp(expr):
    left = ...  # type: Any
    op = ...  # type: Any
    right = ...  # type: Any
    def __init__(self, left = ..., op = ..., right = ...) -> None:
        pass

class BitAnd(operator):
    def __init__(self) -> None:
        pass

class BitOr(operator):
    def __init__(self) -> None:
        pass

class BitXor(operator):
    def __init__(self) -> None:
        pass

class BoolOp(expr):
    op = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, op = ..., values = ...) -> None:
        pass

class Break(stmt):
    def __init__(self) -> None:
        pass

class Call(expr):
    func = ...  # type: Any
    args = ...  # type: Any
    keywords = ...  # type: Any
    starargs = ...  # type: Any
    kwargs = ...  # type: Any
    def __init__(self, func = ..., args = ..., keywords = ..., starargs = ..., kwargs = ...) -> None:
        pass

class ClassDef(stmt):
    name = ...  # type: Any
    bases = ...  # type: Any
    body = ...  # type: Any
    decorator_list = ...  # type: Any
    def __init__(self, name = ..., bases = ..., body = ..., decorator_list = ...) -> None:
        pass

class Compare(expr):
    left = ...  # type: Any
    ops = ...  # type: Any
    comparators = ...  # type: Any
    def __init__(self, left = ..., ops = ..., comparators = ...) -> None:
        pass

class Continue(stmt):
    def __init__(self) -> None:
        pass

class Del(expr_context):
    def __init__(self) -> None:
        pass

class Delete(stmt):
    targets = ...  # type: Any
    def __init__(self, targets = ...) -> None:
        pass

class Dict(expr):
    keys = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, keys = ..., values = ...) -> None:
        pass

class DictComp(expr):
    key = ...  # type: Any
    value = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, key = ..., value = ..., generators = ...) -> None:
        pass

class Div(operator):
    def __init__(self) -> None:
        pass

class Ellipsis(slice):
    def __init__(self) -> None:
        pass

class Eq(cmpop):
    def __init__(self) -> None:
        pass

class ExceptHandler(excepthandler):
    type = ...  # type: Any
    name = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, type = ..., name = ..., body = ...) -> None:
        pass

class Exec(stmt):
    body = ...  # type: Any
    globals = ...  # type: Any
    locals = ...  # type: Any
    def __init__(self, body = ..., globals = ..., locals = ...) -> None:
        pass

class Expr(stmt):
    value = ...  # type: Any
    def __init__(self, value = ...) -> None:
        pass

class Expression(mod):
    body = ...  # type: Any
    def __init__(self, body = ...) -> None:
        pass

class ExtSlice(slice):
    dims = ...  # type: Any
    def __init__(self, dims = ...) -> None:
        pass

class FloorDiv(operator):
    def __init__(self) -> None:
        pass

class For(stmt):
    target = ...  # type: Any
    iter = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, target = ..., iter = ..., body = ..., orelse = ...) -> None:
        pass

class FunctionDef(stmt):
    name = ...  # type: Any
    args = ...  # type: Any
    body = ...  # type: Any
    decorator_list = ...  # type: Any
    def __init__(self, name = ..., args = ..., body = ..., decorator_list = ...) -> None:
        pass

class GeneratorExp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...) -> None:
        pass

class Global(stmt):
    names = ...  # type: Any
    def __init__(self, names = ...) -> None:
        pass

class Gt(cmpop):
    def __init__(self) -> None:
        pass

class GtE(cmpop):
    def __init__(self) -> None:
        pass

class If(stmt):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...) -> None:
        pass

class IfExp(expr):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...) -> None:
        pass

class Import(stmt):
    names = ...  # type: Any
    def __init__(self, names = ...) -> None:
        pass

class ImportFrom(stmt):
    module = ...  # type: Any
    names = ...  # type: Any
    level = ...  # type: Any
    def __init__(self, module = ..., names = ..., level = ...) -> None:
        pass

class In(cmpop):
    def __init__(self) -> None:
        pass

class Index(slice):
    value = ...  # type: Any
    def __init__(self, value = ...) -> None:
        pass

class Interactive(mod):
    body = ...  # type: Any
    def __init__(self, body = ...) -> None:
        pass

class Invert(unaryop):
    def __init__(self) -> None:
        pass

class Is(cmpop):
    def __init__(self) -> None:
        pass

class IsNot(cmpop):
    def __init__(self) -> None:
        pass

class LShift(operator):
    def __init__(self) -> None:
        pass

class Lambda(expr):
    args = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, args = ..., body = ...) -> None:
        pass

class List(expr):
    elts = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, elts = ..., ctx = ...) -> None:
        pass

class ListComp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...) -> None:
        pass

class Load(expr_context):
    def __init__(self) -> None:
        pass

class Lt(cmpop):
    def __init__(self) -> None:
        pass

class LtE(cmpop):
    def __init__(self) -> None:
        pass

class Mod(operator):
    def __init__(self) -> None:
        pass

class Module(mod):
    body = ...  # type: Any
    def __init__(self, body = ...) -> None:
        pass

class Mult(operator):
    def __init__(self) -> None:
        pass

class Name(expr):
    id = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, id = ..., ctx = ...) -> None:
        pass

class Not(unaryop):
    def __init__(self) -> None:
        pass

class NotEq(cmpop):
    def __init__(self) -> None:
        pass

class NotIn(cmpop):
    def __init__(self) -> None:
        pass

class Num(expr):
    n = ...  # type: Any
    def __init__(self, n = ...) -> None:
        pass

class Or(boolop):
    def __init__(self) -> None:
        pass

class Param(expr_context):
    def __init__(self) -> None:
        pass

class Pass(stmt):
    def __init__(self) -> None:
        pass

class Pow(operator):
    def __init__(self) -> None:
        pass

class Print(stmt):
    dest = ...  # type: Any
    values = ...  # type: Any
    nl = ...  # type: Any
    def __init__(self, dest = ..., values = ..., nl = ...) -> None:
        pass

class RShift(operator):
    def __init__(self) -> None:
        pass

class Raise(stmt):
    type = ...  # type: Any
    inst = ...  # type: Any
    tback = ...  # type: Any
    def __init__(self, type = ..., inst = ..., tback = ...) -> None:
        pass

class Repr(expr):
    value = ...  # type: Any
    def __init__(self, value = ...) -> None:
        pass

class Return(stmt):
    value = ...  # type: Any
    def __init__(self, value = ...) -> None:
        pass

class Set(expr):
    elts = ...  # type: Any
    def __init__(self, elts = ...) -> None:
        pass

class SetComp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...) -> None:
        pass

class Slice(slice):
    lower = ...  # type: Any
    upper = ...  # type: Any
    step = ...  # type: Any
    def __init__(self, lower = ..., upper = ..., step = ...) -> None:
        pass

class Store(expr_context):
    def __init__(self) -> None:
        pass

class Str(expr):
    s = ...  # type: Any
    def __init__(self, s = ...) -> None:
        pass

class Sub(operator):
    def __init__(self) -> None:
        pass

class Subscript(expr):
    value = ...  # type: Any
    slice = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, value = ..., slice = ..., ctx = ...) -> None:
        pass

class Suite(mod):
    body = ...  # type: Any
    def __init__(self, body = ...) -> None:
        pass

class TryExcept(stmt):
    body = ...  # type: Any
    handlers = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, body = ..., handlers = ..., orelse = ...) -> None:
        pass

class TryFinally(stmt):
    body = ...  # type: Any
    finalbody = ...  # type: Any
    def __init__(self, body = ..., finalbody = ...) -> None:
        pass

class Tuple(expr):
    elts = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, elts = ..., ctx = ...) -> None:
        pass

class UAdd(unaryop):
    def __init__(self) -> None:
        pass

class USub(unaryop):
    def __init__(self) -> None:
        pass

class UnaryOp(expr):
    op = ...  # type: Any
    operand = ...  # type: Any
    def __init__(self, op = ..., operand = ...) -> None:
        pass

class While(stmt):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...) -> None:
        pass

class With(stmt):
    context_expr = ...  # type: Any
    optional_vars = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, context_expr = ..., optional_vars = ..., body = ...) -> None:
        pass

class Yield(expr):
    value = ...  # type: Any
    def __init__(self, value = ...) -> None:
        pass
