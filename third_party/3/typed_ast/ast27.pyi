import typing
from typing import Any, Optional, Union, TypeVar, Generic, Iterator

T = TypeVar("T")
class NodeVisitor(Generic[T]):
    __doc__ = ...  # type: str
    def visit(self, node: AST) -> T: ...
    def generic_visit(self, node: AST) -> None: ...

class NodeTransformer(NodeVisitor, Generic[T]):
    __doc__ = ...  # type: str
    def generic_visit(self, node: AST) -> None: ...

def parse(source: Union[str, bytes], filename: Union[str, bytes] = ..., mode: str = ...) -> AST: ...
def copy_location(new_node: AST, old_node: AST) -> AST: ...
def dump(node: AST, annotate_fields: bool = ..., include_attributes: bool = ...) -> str: ...
def fix_missing_locations(node: AST) -> AST: ...
def get_docstring(node: AST, clean: bool = ...) -> str: ...
def increment_lineno(node: AST, n: int = ...) -> AST: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def iter_fields(node: AST) -> Iterator[typing.Tuple[str, Any]]: ...
def literal_eval(node_or_string: Union[str, AST]) -> Any: ...
def walk(node: AST) -> Iterator[AST]: ...

PyCF_ONLY_AST = ... # type: int

# ast classes

identifier = str

class AST:
    _attributes = ... # type: typing.Tuple[str, ...]
    _fields = ... # type: typing.Tuple[str, ...]
    def __init__(self, *args, **kwargs): ...
    def __delattr__(self, name): ...
    def __reduce__(self): ...
    def __setattr__(self, name, value): ...

class mod(AST):
    pass

class Module(mod):
    body = ...  # type: typing.List[stmt]
    type_ignores = ...  # type: typing.List[TypeIgnore]

class Interactive(mod):
    body = ...  # type: typing.List[stmt]

class Expression(mod):
    body = ...  # type: expr

class FunctionType(mod):
    argtypes = ...  # type: typing.List[expr]
    returns = ...  # type: expr

class Suite(mod):
    body = ...  # type: typing.List[stmt]


class stmt(AST):
    lineno = ...  # type: int
    col_offset = ...  # type: int

class FunctionDef(stmt):
    name = ...  # type: identifier
    args = ...  # type: arguments
    body = ...  # type: typing.List[stmt]
    decorator_list = ...  # type: typing.List[expr]
    type_comment = ...  # type: Optional[str]

class ClassDef(stmt):
    name = ...  # type: identifier
    bases = ...  # type: typing.List[expr]
    body = ...  # type: typing.List[stmt]
    decorator_list = ...  # type: typing.List[expr]

class Return(stmt):
    value = ...  # type: Optional[expr]

class Delete(stmt):
    targets = ...  # type: typing.List[expr]

class Assign(stmt):
    targets = ...  # type: typing.List[expr]
    value = ...  # type: expr
    type_comment = ...  # type: Optional[str]

class AugAssign(stmt):
    target = ...  # type: expr
    op = ...  # type: operator
    value = ...  # type: expr

class Print(stmt):
    dest = ...  # type: Optional[expr]
    values = ...  # type: typing.List[expr]
    nl = ...  # type: bool

class For(stmt):
    target = ...  # type: expr
    iter = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]
    type_comment = ...  # type: Optional[str]

class While(stmt):
    test = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class If(stmt):
    test = ...  # type: expr
    body = ...  # type: typing.List[stmt]
    orelse = ...  # type: typing.List[stmt]

class With(stmt):
    context_expr = ...  # type: expr
    optional_vars = ...  # type: Optional[expr]
    body = ...  # type: typing.List[stmt]
    type_comment = ...  # type: Optional[str]

class Raise(stmt):
    type = ...  # type: Optional[expr]
    inst = ...  # type: Optional[expr]
    tback = ...  # type: Optional[expr]

class TryExcept(stmt):
    body = ...  # type: typing.List[stmt]
    handlers = ...  # type: typing.List[ExceptHandler]
    orelse = ...  # type: typing.List[stmt]

class TryFinally(stmt):
    body = ...  # type: typing.List[stmt]
    finalbody = ...  # type: typing.List[stmt]

class Assert(stmt):
    test = ...  # type: expr
    msg = ...  # type: Optional[expr]

class Import(stmt):
    names = ...  # type: typing.List[alias]

class ImportFrom(stmt):
    module = ...  # type: Optional[identifier]
    names = ...  # type: typing.List[alias]
    level = ...  # type: Optional[int]

class Exec(stmt):
    body = ...  # type: expr
    globals = ...  # type: Optional[expr]
    locals = ...  # type: Optional[expr]

class Global(stmt):
    names = ...  # type: typing.List[identifier]

class Expr(stmt):
    value = ...  # type: expr

class Pass(stmt): pass
class Break(stmt): pass
class Continue(stmt): pass


class slice(AST):
    pass

_slice = slice  # this lets us type the variable named 'slice' below

class Slice(slice):
    lower = ...  # type: Optional[expr]
    upper = ...  # type: Optional[expr]
    step = ...  # type: Optional[expr]

class ExtSlice(slice):
    dims = ...  # type: typing.List[slice]

class Index(slice):
    value = ...  # type: expr

class Ellipsis(slice): pass


class expr(AST):
    lineno = ...  # type: int
    col_offset = ...  # type: int

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

class Yield(expr):
    value = ...  # type: Optional[expr]

class Compare(expr):
    left = ...  # type: expr
    ops = ...  # type: typing.List[cmpop]
    comparators = ...  # type: typing.List[expr]

class Call(expr):
    func = ...  # type: expr
    args = ...  # type: typing.List[expr]
    keywords = ...  # type: typing.List[keyword]
    starargs = ...  # type: Optional[expr]
    kwargs = ...  # type: Optional[expr]

class Repr(expr):
    value = ...  # type: expr

class Num(expr):
    n = ...  # type: Union[int, float]

class Str(expr):
    s = ...  # type: str

class Attribute(expr):
    value = ...  # type: expr
    attr = ...  # type: identifier
    ctx = ...  # type: expr_context

class Subscript(expr):
    value = ...  # type: expr
    slice = ...  # type: _slice
    ctx = ...  # type: expr_context

class Name(expr):
    id = ...  # type: identifier
    ctx = ...  # type: expr_context

class List(expr):
    elts = ...  # type: typing.List[expr]
    ctx = ...  # type: expr_context

class Tuple(expr):
    elts = ...  # type: typing.List[expr]
    ctx = ...  # type: expr_context


class expr_context(AST):
    pass

class AugLoad(expr_context): pass
class AugStore(expr_context): pass
class Del(expr_context): pass
class Load(expr_context): pass
class Param(expr_context): pass
class Store(expr_context): pass


class boolop(AST):
    pass

class And(boolop): pass
class Or(boolop): pass

class operator(AST):
    pass

class Add(operator): pass
class BitAnd(operator): pass
class BitOr(operator): pass
class BitXor(operator): pass
class Div(operator): pass
class FloorDiv(operator): pass
class LShift(operator): pass
class Mod(operator): pass
class Mult(operator): pass
class Pow(operator): pass
class RShift(operator): pass
class Sub(operator): pass

class unaryop(AST):
    pass

class Invert(unaryop): pass
class Not(unaryop): pass
class UAdd(unaryop): pass
class USub(unaryop): pass

class cmpop(AST):
    pass

class Eq(cmpop): pass
class Gt(cmpop): pass
class GtE(cmpop): pass
class In(cmpop): pass
class Is(cmpop): pass
class IsNot(cmpop): pass
class Lt(cmpop): pass
class LtE(cmpop): pass
class NotEq(cmpop): pass
class NotIn(cmpop): pass


class comprehension(AST):
    target = ...  # type: expr
    iter = ...  # type: expr
    ifs = ...  # type: typing.List[expr]


class ExceptHandler(AST):
    type = ...  # type: Optional[expr]
    name = ...  # type: Optional[expr]
    body = ...  # type: typing.List[stmt]
    lineno = ...  # type: int
    col_offset = ...  # type: int


class arguments(AST):
    args = ...  # type: typing.List[expr]
    vararg = ...  # type: Optional[identifier]
    kwarg = ...  # type: Optional[identifier]
    defaults = ...  # type: typing.List[expr]

class keyword(AST):
    arg = ...  # type: identifier
    value = ...  # type: expr

class alias(AST):
    name = ...  # type: identifier
    asname = ...  # type: Optional[identifier]


class TypeIgnore(AST):
    lineno = ...  # type: int
