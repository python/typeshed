import ast
import sys
from collections import Counter
from collections.abc import Callable, Iterable, Iterator
from tokenize import TokenInfo
from typing import Any, ClassVar, Pattern, TypeVar, overload
from typing_extensions import Literal, ParamSpec

from pyflakes.messages import Message

_AnyFunction = Callable[..., Any]
_F = TypeVar("_F", bound=_AnyFunction)
_P = ParamSpec("_P")

PY2: bool
PY35_PLUS: bool
PY36_PLUS: bool
PY38_PLUS: bool
PYPY: bool

def getNodeType(node_class: type[ast.AST]) -> str: ...
def get_raise_argument(node: ast.Raise) -> ast.expr | None: ...
def getAlternatives(n: ast.If | ast.Try) -> list[ast.AST]: ...

FOR_TYPES: tuple[type[ast.For], type[ast.AsyncFor]]
LOOP_TYPES: tuple[type[ast.While], type[ast.For], type[ast.AsyncFor]]
FUNCTION_TYPES: tuple[type[ast.FunctionDef], type[ast.AsyncFunctionDef]]
ANNASSIGN_TYPES: tuple[ast.AnnAssign]
TYPE_COMMENT_RE: Pattern[str]
ASCII_NON_ALNUM: str
TYPE_IGNORE_RE: Pattern[str]
TYPE_FUNC_RE: Pattern[str]
MAPPING_KEY_RE: Pattern[str]
CONVERSION_FLAG_RE: Pattern[str]
WIDTH_RE: Pattern[str]
PRECISION_RE: Pattern[str]
LENGTH_RE: Pattern[str]
VALID_CONVERSIONS: frozenset[str]

_FormatType = tuple[str | None, str | None, str | None, str | None, str]
_PercentFormat = tuple[str, _FormatType | None]

def parse_percent_format(s: str) -> tuple[_PercentFormat, ...]: ...

class _FieldsOrder(dict[type[ast.AST], tuple[str, ...]]):
    def __missing__(self, node_class: type[ast.AST]) -> tuple[str, ...]: ...

counter = Counter  # Not strictly true, but close enough
_OmitType = str | tuple[str, ...] | None

def iter_child_nodes(node: ast.AST, omit: _OmitType = ..., _fields_order: _FieldsOrder = ...) -> Iterator[ast.AST]: ...
@overload
def convert_to_value(item: ast.Str) -> str: ...  # type: ignore[misc]
@overload
def convert_to_value(item: ast.Bytes) -> bytes: ...  # type: ignore[misc]
@overload
def convert_to_value(item: ast.Tuple) -> tuple[Any, ...]: ...  # type: ignore[misc]
@overload
def convert_to_value(item: ast.Name | ast.NameConstant) -> Any: ...
@overload
def convert_to_value(item: ast.AST) -> UnhandledKeyType: ...
def is_notimplemented_name_node(node: object) -> bool: ...

class Binding:
    name: str
    source: ast.AST | None
    used: Literal[False] | tuple[Any, ast.AST]
    def __init__(self, name: str, source: ast.AST | None) -> None: ...
    def redefines(self, other: Binding) -> bool: ...

class Definition(Binding): ...

class Builtin(Definition):
    def __init__(self, name: str) -> None: ...

class UnhandledKeyType: ...

class VariableKey:
    name: str
    def __init__(self, item: ast.Name) -> None: ...
    def __eq__(self, compare: object) -> bool: ...
    def __hash__(self) -> int: ...

class Importation(Definition):
    fullName: str
    redefined: list[Any]
    def __init__(self, name: str, source: ast.AST | None, full_name: str | None = ...) -> None: ...
    @property
    def source_statement(self) -> str: ...

class SubmoduleImportation(Importation):
    def __init__(self, name: str, source: ast.Import | None) -> None: ...

class ImportationFrom(Importation):
    module: str
    real_name: str
    def __init__(self, name: str, source: ast.AST, module: str, real_name: str | None = ...) -> None: ...

class StarImportation(Importation):
    def __init__(self, name: str, source: ast.AST) -> None: ...

class FutureImportation(ImportationFrom):
    used: tuple[Any, ast.AST]
    def __init__(self, name: str, source: ast.AST, scope) -> None: ...

class Argument(Binding): ...
class Assignment(Binding): ...

class Annotation(Binding):
    def redefines(self, other: Binding) -> Literal[False]: ...

class FunctionDefinition(Definition): ...
class ClassDefinition(Definition): ...

class ExportBinding(Binding):
    names: list[str]
    def __init__(self, name: str, source: ast.AST, scope: Scope) -> None: ...

class Scope(dict[str, Binding]):
    importStarred: bool

class ClassScope(Scope): ...

class FunctionScope(Scope):
    usesLocals: bool
    alwaysUsed: ClassVar[set[str]]
    globals: set[str]
    returnValue: Any
    isGenerator: bool
    def __init__(self) -> None: ...
    def unusedAssignments(self) -> Iterator[tuple[str, Binding]]: ...

class GeneratorScope(Scope): ...
class ModuleScope(Scope): ...
class DoctestScope(ModuleScope): ...

class DummyNode:
    lineno: int
    col_offset: int
    def __init__(self, lineno: int, col_offset: int) -> None: ...

class DetectClassScopedMagic:
    names: list[str]

def getNodeName(node: ast.AST) -> str: ...

TYPING_MODULES: frozenset[Literal["typing", "typing_extensions"]]

def is_typing_overload(value: Binding, scope_stack) -> bool: ...

class AnnotationState:
    NONE: ClassVar[Literal[0]]
    STRING: ClassVar[Literal[1]]
    BARE: ClassVar[Literal[2]]

def in_annotation(func: _F) -> _F: ...
def in_string_annotation(func: _F) -> _F: ...
def make_tokens(code: str | bytes) -> tuple[TokenInfo, ...]: ...

class Checker:
    nodeDepth: int
    offset: tuple[int, int] | None
    builtIns: set[str]
    deadScopes: list[Any]
    messages: list[Any]
    filename: str
    withDoctest: bool
    scopeStack: list[Scope]
    exceptHandlers: list[Any]
    root: ast.AST
    def __init__(
        self,
        tree: ast.AST,
        filename: str = ...,
        builtins: Iterable[str] | None = ...,
        withDoctest: bool = ...,
        file_tokens: tuple[Any, ...] = ...,
    ) -> None: ...
    def deferFunction(self, callable: _AnyFunction) -> None: ...
    def deferAssignment(self, callable: _AnyFunction) -> None: ...
    def runDeferred(self, deferred: _AnyFunction) -> None: ...
    @property
    def futuresAllowed(self) -> bool: ...
    @futuresAllowed.setter
    def futuresAllowed(self, value: Literal[False]) -> None: ...
    @property
    def annotationsFutureEnabled(self) -> bool: ...
    @annotationsFutureEnabled.setter
    def annotationsFutureEnabled(self, value: Literal[True]) -> None: ...
    @property
    def scope(self) -> Scope: ...
    def popScope(self) -> None: ...
    def checkDeadScopes(self) -> None: ...
    def pushScope(self, scopeClass: type[Scope] = ...) -> None: ...
    def report(self, messageClass: Callable[_P, Message], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def getParent(self, node: ast.AST) -> ast.AST: ...
    def getCommonAncestor(self, lnode: ast.AST, rnode: ast.AST, stop: ast.AST) -> ast.AST: ...
    def descendantOf(self, node: ast.AST, ancestors: ast.AST, stop: ast.AST) -> bool: ...
    def getScopeNode(self, node: ast.AST) -> ast.AST | None: ...
    def differentForks(self, lnode: ast.AST, rnode: ast.AST) -> bool: ...
    def addBinding(self, node: ast.AST, value: Binding) -> None: ...
    def getNodeHandler(self, node_class: type[ast.AST]): ...
    def handleNodeLoad(self, node: ast.AST) -> None: ...
    def handleNodeStore(self, node: ast.AST) -> None: ...
    def handleNodeDelete(self, node: ast.AST) -> None: ...
    def handleChildren(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def isLiteralTupleUnpacking(self, node: ast.AST) -> bool | None: ...
    def isDocstring(self, node: ast.AST) -> bool: ...
    def getDocstring(self, node: ast.AST) -> tuple[str, int] | tuple[None, None]: ...
    def handleNode(self, node: ast.AST | None, parent) -> None: ...
    def handleDoctests(self, node: ast.AST) -> None: ...
    def handleStringAnnotation(self, s: str, node: ast.AST, ref_lineno: int, ref_col_offset: int, err: type[Message]) -> None: ...
    def handleAnnotation(self, annotation: ast.AST, node: ast.AST) -> None: ...
    def ignore(self, node: ast.AST) -> None: ...
    def DELETE(self, node: ast.Delete, tree, omit: _OmitType = ...) -> None: ...
    def PRINT(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def FOR(self, node: ast.For, tree, omit: _OmitType = ...) -> None: ...
    def ASYNCFOR(self, node: ast.AsyncFor, tree, omit: _OmitType = ...) -> None: ...
    def WHILE(self, node: ast.While, tree, omit: _OmitType = ...) -> None: ...
    def WITH(self, node: ast.With, tree, omit: _OmitType = ...) -> None: ...
    def WITHITEM(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def ASYNCWITH(self, node: ast.AsyncWith, tree, omit: _OmitType = ...) -> None: ...
    def ASYNCWITHITEM(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def TRYFINALLY(self, node: ast.Try, tree, omit: _OmitType = ...) -> None: ...
    def EXEC(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def EXPR(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def ASSIGN(self, node: ast.Assign, tree, omit: _OmitType = ...) -> None: ...
    def PASS(self, node: ast.AST) -> None: ...
    def BOOLOP(self, node: ast.BoolOp, tree, omit: _OmitType = ...) -> None: ...
    def UNARYOP(self, node: ast.UnaryOp, tree, omit: _OmitType = ...) -> None: ...
    def SET(self, node: ast.Set, tree, omit: _OmitType = ...) -> None: ...
    def REPR(self, node: ast.AST, tree, omit: _OmitType = ...) -> None: ...
    def ATTRIBUTE(self, node: ast.Attribute, tree, omit: _OmitType = ...) -> None: ...
    def STARRED(self, node: ast.Starred, tree, omit: _OmitType = ...) -> None: ...
    def NAMEDCONSTANT(self, node: ast.NameConstant, tree, omit: _OmitType = ...) -> None: ...
    def NAMEDEXPR(self, node: ast.NamedExpr, tree, omit: _OmitType = ...) -> None: ...
    def SUBSCRIPT(self, node: ast.Subscript) -> None: ...
    def CALL(self, node: ast.Call) -> None: ...
    def BINOP(self, node: ast.BinOp) -> None: ...
    def STR(self, node: ast.Str) -> None: ...
    def CONSTANT(self, node: ast.Constant) -> None: ...

    if sys.version_info < (3, 8):
        def NUM(self, node: ast.Num) -> None: ...
        def BYTES(self, node: ast.Bytes) -> None: ...
        def ELLIPSIS(self, node: ast.Ellipsis) -> None: ...

    def SLICE(self, node: ast.Slice, tree, omit: _OmitType = ...) -> None: ...

    if sys.version_info < (3, 9):
        def EXTSLICE(self, node: ast.ExtSlice, tree, omit: _OmitType = ...) -> None: ...
        def INDEX(self, node: ast.Index, tree, omit: _OmitType = ...) -> None: ...

    def LOAD(self, node: ast.Load) -> None: ...
    def STORE(self, node: ast.Store) -> None: ...
    def DEL(self, node: ast.Del) -> None: ...

    if sys.version_info < (3, 9):
        def AUGLOAD(self, node: ast.AugLoad) -> None: ...
        def AUGSTORE(self, node: ast.Augstore) -> None: ...
        def PARAM(self, node: ast.Param) -> None: ...

    def AND(self, node: ast.And) -> None: ...
    def OR(self, node: ast.Or) -> None: ...
    def ADD(self, node: ast.Add) -> None: ...
    def SUB(self, node: ast.Sub) -> None: ...
    def MULT(self, node: ast.Mult) -> None: ...
    def DIV(self, node: ast.Div) -> None: ...
    def MOD(self, node: ast.Mod) -> None: ...
    def POW(self, node: ast.Pow) -> None: ...
    def LSHIFT(self, node: ast.LShift) -> None: ...
    def RSHIFT(self, node: ast.RShift) -> None: ...
    def BITOR(self, node: ast.BitOr) -> None: ...
    def BITXOR(self, node: ast.BitXor) -> None: ...
    def BITAND(self, node: ast.BitAnd) -> None: ...
    def FLOORDIV(self, node: ast.FloorDiv) -> None: ...
    def INVERT(self, node: ast.Invert) -> None: ...
    def NOT(self, node: ast.Not) -> None: ...
    def UADD(self, node: ast.UAdd) -> None: ...
    def USUB(self, node: ast.USub) -> None: ...
    def EQ(self, node: ast.Eq) -> None: ...
    def NOTEQ(self, node: ast.NotEq) -> None: ...
    def LT(self, node: ast.Lt) -> None: ...
    def LTE(self, node: ast.LtE) -> None: ...
    def GT(self, node: ast.Gt) -> None: ...
    def GTE(self, node: ast.GtE) -> None: ...
    def IS(self, node: ast.Is) -> None: ...
    def ISNOT(self, node: ast.IsNot) -> None: ...
    def IN(self, node: ast.In) -> None: ...
    def NOTIN(self, node: ast.NotIn) -> None: ...
    def MATMULT(self, node: ast.MatMult) -> None: ...
    def RAISE(self, node: ast.Raise) -> None: ...
    def COMPREHENSION(self, node: ast.comprehension, tree, omit: _OmitType = ...) -> None: ...
    def KEYWORD(self, node: ast.keyword, tree, omit: _OmitType = ...) -> None: ...
    def FORMATTEDVALUE(self, node: ast.FormattedValue, tree, omit: _OmitType = ...) -> None: ...
    def JOINEDSTR(self, node: ast.AST) -> None: ...
    def DICT(self, node: ast.Dict) -> None: ...
    def IF(self, node: ast.If) -> None: ...
    def IFEXPR(self, node: ast.If) -> None: ...
    def ASSERT(self, node: ast.Assert) -> None: ...
    def GLOBAL(self, node: ast.Global) -> None: ...
    def NONLOCAL(self, node: ast.Nonlocal) -> None: ...
    def GENERATOREXP(self, node: ast.GeneratorExp) -> None: ...
    def LISTCOMP(self, node: ast.ListComp) -> None: ...
    def DICTCOMP(self, node: ast.DictComp) -> None: ...
    def SETCOMP(self, node: ast.SetComp) -> None: ...
    def NAME(self, node: ast.Name) -> None: ...
    def CONTINUE(self, node: ast.Continue) -> None: ...
    def BREAK(self, node: ast.Break) -> None: ...
    def RETURN(self, node: ast.Return) -> None: ...
    def YIELD(self, node: ast.Yield) -> None: ...
    def AWAIT(self, node: ast.Await) -> None: ...
    def YIELDFROM(self, node: ast.YieldFrom) -> None: ...
    def FUNCTIONDEF(self, node: ast.FunctionDef) -> None: ...
    def ASYNCFUNCTIONDEF(self, node: ast.AsyncFunctionDef) -> None: ...
    def LAMBDA(self, node: ast.Lambda) -> None: ...
    def ARGUMENTS(self, node: ast.arguments) -> None: ...
    def ARG(self, node: ast.arg) -> None: ...
    def CLASSDEF(self, node: ast.ClassDef): ...
    def AUGASSIGN(self, node: ast.AugAssign) -> None: ...
    def TUPLE(self, node: ast.Tuple) -> None: ...
    def LIST(self, node: ast.List) -> None: ...
    def IMPORT(self, node: ast.Import) -> None: ...
    def IMPORTFROM(self, node: ast.ImportFrom) -> None: ...
    def TRY(self, node: ast.Try) -> None: ...
    def TRYEXCEPT(self, node: ast.Try) -> None: ...
    def EXCEPTHANDLER(self, node: ast.ExceptHandler) -> None: ...
    def ANNASSIGN(self, node: ast.AnnAssign) -> None: ...
    def COMPARE(self, node: ast.Compare) -> None: ...
    def MATCH(self, node: ast.Match, tree, omit: _OmitType = ...) -> None: ...
    def MATCH_CASE(self, node: ast.match_case, tree, omit: _OmitType = ...) -> None: ...
    def MATCHCLASS(self, node: ast.MatchClass, tree, omit: _OmitType = ...) -> None: ...
    def MATCHOR(self, node: ast.MatchOr, tree, omit: _OmitType = ...) -> None: ...
    def MATCHSEQUENCE(self, node: ast.MatchSequence, tree, omit: _OmitType = ...) -> None: ...
    def MATCHSINGLETON(self, node: ast.MatchSingleton, tree, omit: _OmitType = ...) -> None: ...
    def MATCHVALUE(self, node: ast.MatchValue, tree, omit: _OmitType = ...) -> None: ...
    def MATCHAS(self, node: ast.MatchAs) -> None: ...
    def MATCHMAPPING(self, node: ast.MatchMapping) -> None: ...
    def MATCHSTAR(self, node: ast.MatchStar) -> None: ...
