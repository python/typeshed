from typing import Any, Tuple

PyCF_ONLY_AST = ...  # type: int

class AST(object):
    _attributes = ...  # type: Tuple[str]
    _fields = ...  # type: Tuple[str]
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
    def __init__(self):
        pass

class And(boolop):
    def __init__(self):
        pass

class Assert(stmt):
    test = ...  # type: Any
    msg = ...  # type: Any
    def __init__(self, test = ..., msg = ...):
        pass

class Assign(stmt):
    targets = ...  # type: Any
    value = ...  # type: Any
    def __init__(self, targets = ..., value = ...):
        pass

class Attribute(expr):
    value = ...  # type: Any
    attr = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, value = ..., attr = ..., ctx = ...):
        pass

class AugAssign(stmt):
    target = ...  # type: Any
    op = ...  # type: Any
    value = ...  # type: Any
    def __init__(self, target = ..., op = ..., value = ...):
        pass

class AugLoad(expr_context):
    def __init__(self):
        pass

class AugStore(expr_context):
    def __init__(self):
        pass

class BinOp(expr):
    left = ...  # type: Any
    op = ...  # type: Any
    right = ...  # type: Any
    def __init__(self, left = ..., op = ..., right = ...):
        pass

class BitAnd(operator):
    def __init__(self):
        pass

class BitOr(operator):
    def __init__(self):
        pass

class BitXor(operator):
    def __init__(self):
        pass

class BoolOp(expr):
    op = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, op = ..., values = ...):
        pass

class Break(stmt):
    def __init__(self):
        pass

class Call(expr):
    func = ...  # type: Any
    args = ...  # type: Any
    keywords = ...  # type: Any
    starargs = ...  # type: Any
    kwargs = ...  # type: Any
    def __init__(self, func = ..., args = ..., keywords = ..., starargs = ..., kwargs = ...):
        pass

class ClassDef(stmt):
    name = ...  # type: Any
    bases = ...  # type: Any
    body = ...  # type: Any
    decorator_list = ...  # type: Any
    def __init__(self, name = ..., bases = ..., body = ..., decorator_list = ...):
        pass

class Compare(expr):
    left = ...  # type: Any
    ops = ...  # type: Any
    comparators = ...  # type: Any
    def __init__(self, left = ..., ops = ..., comparators = ...):
        pass

class Continue(stmt):
    def __init__(self):
        pass

class Del(expr_context):
    def __init__(self):
        pass

class Delete(stmt):
    targets = ...  # type: Any
    def __init__(self, targets = ...):
        pass

class Dict(expr):
    keys = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, keys = ..., values = ...):
        pass

class DictComp(expr):
    key = ...  # type: Any
    value = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, key = ..., value = ..., generators = ...):
        pass

class Div(operator):
    def __init__(self):
        pass

class Ellipsis(slice):
    def __init__(self):
        pass

class Eq(cmpop):
    def __init__(self):
        pass

class ExceptHandler(excepthandler):
    type = ...  # type: Any
    name = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, type = ..., name = ..., body = ...):
        pass

class Exec(stmt):
    body = ...  # type: Any
    globals = ...  # type: Any
    locals = ...  # type: Any
    def __init__(self, body = ..., globals = ..., locals = ...):
        pass

class Expr(stmt):
    value = ...  # type: Any
    def __init__(self, value = ...):
        pass

class Expression(mod):
    body = ...  # type: Any
    def __init__(self, body = ...):
        pass

class ExtSlice(slice):
    dims = ...  # type: Any
    def __init__(self, dims = ...):
        pass

class FloorDiv(operator):
    def __init__(self):
        pass

class For(stmt):
    target = ...  # type: Any
    iter = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, target = ..., iter = ..., body = ..., orelse = ...):
        pass

class FunctionDef(stmt):
    name = ...  # type: Any
    args = ...  # type: Any
    body = ...  # type: Any
    decorator_list = ...  # type: Any
    def __init__(self, name = ..., args = ..., body = ..., decorator_list = ...):
        pass

class GeneratorExp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...):
        pass

class Global(stmt):
    names = ...  # type: Any
    def __init__(self, names = ...):
        pass

class Gt(cmpop):
    def __init__(self):
        pass

class GtE(cmpop):
    def __init__(self):
        pass

class If(stmt):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...):
        pass

class IfExp(expr):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...):
        pass

class Import(stmt):
    names = ...  # type: Any
    def __init__(self, names = ...):
        pass

class ImportFrom(stmt):
    module = ...  # type: Any
    names = ...  # type: Any
    level = ...  # type: Any
    def __init__(self, module = ..., names = ..., level = ...):
        pass

class In(cmpop):
    def __init__(self):
        pass

class Index(slice):
    value = ...  # type: Any
    def __init__(self, value = ...):
        pass

class Interactive(mod):
    body = ...  # type: Any
    def __init__(self, body = ...):
        pass

class Invert(unaryop):
    def __init__(self):
        pass

class Is(cmpop):
    def __init__(self):
        pass

class IsNot(cmpop):
    def __init__(self):
        pass

class LShift(operator):
    def __init__(self):
        pass

class Lambda(expr):
    args = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, args = ..., body = ...):
        pass

class List(expr):
    elts = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, elts = ..., ctx = ...):
        pass

class ListComp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...):
        pass

class Load(expr_context):
    def __init__(self):
        pass

class Lt(cmpop):
    def __init__(self):
        pass

class LtE(cmpop):
    def __init__(self):
        pass

class Mod(operator):
    def __init__(self):
        pass

class Module(mod):
    body = ...  # type: Any
    def __init__(self, body = ...):
        pass

class Mult(operator):
    def __init__(self):
        pass

class Name(expr):
    id = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, id = ..., ctx = ...):
        pass

class Not(unaryop):
    def __init__(self):
        pass

class NotEq(cmpop):
    def __init__(self):
        pass

class NotIn(cmpop):
    def __init__(self):
        pass

class Num(expr):
    n = ...  # type: Any
    def __init__(self, n = ...):
        pass

class Or(boolop):
    def __init__(self):
        pass

class Param(expr_context):
    def __init__(self):
        pass

class Pass(stmt):
    def __init__(self):
        pass

class Pow(operator):
    def __init__(self):
        pass

class Print(stmt):
    dest = ...  # type: Any
    values = ...  # type: Any
    nl = ...  # type: Any
    def __init__(self, dest = ..., values = ..., nl = ...):
        pass

class RShift(operator):
    def __init__(self):
        pass

class Raise(stmt):
    type = ...  # type: Any
    inst = ...  # type: Any
    tback = ...  # type: Any
    def __init__(self, type = ..., inst = ..., tback = ...):
        pass

class Repr(expr):
    value = ...  # type: Any
    def __init__(self, value = ...):
        pass

class Return(stmt):
    value = ...  # type: Any
    def __init__(self, value = ...):
        pass

class Set(expr):
    elts = ...  # type: Any
    def __init__(self, elts = ...):
        pass

class SetComp(expr):
    elt = ...  # type: Any
    generators = ...  # type: Any
    def __init__(self, elt = ..., generators = ...):
        pass

class Slice(slice):
    lower = ...  # type: Any
    upper = ...  # type: Any
    step = ...  # type: Any
    def __init__(self, lower = ..., upper = ..., step = ...):
        pass

class Store(expr_context):
    def __init__(self):
        pass

class Str(expr):
    s = ...  # type: Any
    def __init__(self, s = ...):
        pass

class Sub(operator):
    def __init__(self):
        pass

class Subscript(expr):
    value = ...  # type: Any
    slice = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, value = ..., slice = ..., ctx = ...):
        pass

class Suite(mod):
    body = ...  # type: Any
    def __init__(self, body = ...):
        pass

class TryExcept(stmt):
    body = ...  # type: Any
    handlers = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, body = ..., handlers = ..., orelse = ...):
        pass

class TryFinally(stmt):
    body = ...  # type: Any
    finalbody = ...  # type: Any
    def __init__(self, body = ..., finalbody = ...):
        pass

class Tuple(expr):
    elts = ...  # type: Any
    ctx = ...  # type: Any
    def __init__(self, elts = ..., ctx = ...):
        pass

class UAdd(unaryop):
    def __init__(self):
        pass

class USub(unaryop):
    def __init__(self):
        pass

class UnaryOp(expr):
    op = ...  # type: Any
    operand = ...  # type: Any
    def __init__(self, op = ..., operand = ...):
        pass

class While(stmt):
    test = ...  # type: Any
    body = ...  # type: Any
    orelse = ...  # type: Any
    def __init__(self, test = ..., body = ..., orelse = ...):
        pass

class With(stmt):
    context_expr = ...  # type: Any
    optional_vars = ...  # type: Any
    body = ...  # type: Any
    def __init__(self, context_expr = ..., optional_vars = ..., body = ...):
        pass

class Yield(expr):
    value = ...  # type: Any
    def __init__(self, value = ...):
        pass
