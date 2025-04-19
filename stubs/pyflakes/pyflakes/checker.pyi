import ast
import sys
from _typeshed import StrOrLiteralStr, Unused
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from contextlib import contextmanager
from re import Pattern
from typing import Any, ClassVar, Final, Literal, TypeVar, overload
from typing_extensions import Never, ParamSpec, TypeAlias

from pyflakes.messages import Message

_AnyFunction: TypeAlias = Callable[..., Any]
_F = TypeVar("_F", bound=_AnyFunction)
_P = ParamSpec("_P")

PYPY: Final[bool]
builtin_vars: Final[list[str]]

def parse_format_string(
    format_string: StrOrLiteralStr,
) -> Iterable[tuple[StrOrLiteralStr, StrOrLiteralStr | None, StrOrLiteralStr | None, StrOrLiteralStr | None]]: ...

if sys.version_info >= (3, 10):
    def getAlternatives(n: ast.If | ast.Try | ast.Match) -> list[ast.AST]: ...

else:
    def getAlternatives(n: ast.If | ast.Try) -> list[ast.AST]: ...

FOR_TYPES: Final[tuple[type[ast.For], type[ast.AsyncFor]]]
MAPPING_KEY_RE: Final[Pattern[str]]
CONVERSION_FLAG_RE: Final[Pattern[str]]
WIDTH_RE: Final[Pattern[str]]
PRECISION_RE: Final[Pattern[str]]
LENGTH_RE: Final[Pattern[str]]
VALID_CONVERSIONS: frozenset[str]

_FormatType: TypeAlias = tuple[str | None, str | None, str | None, str | None, str]
_PercentFormat: TypeAlias = tuple[str, _FormatType | None]

def parse_percent_format(s: str) -> tuple[_PercentFormat, ...]: ...

class _FieldsOrder(dict[type[ast.AST], tuple[str, ...]]):
    def __missing__(self, node_class: type[ast.AST]) -> tuple[str, ...]: ...

_OmitType: TypeAlias = str | tuple[str, ...] | None

def iter_child_nodes(node: ast.AST, omit: _OmitType = None, _fields_order: _FieldsOrder = ...) -> Iterator[ast.AST]: ...
@overload
def convert_to_value(item: ast.Constant) -> Any: ...  # type: ignore[overload-overlap]  # See ast.Constant.value for possible return types
@overload
def convert_to_value(item: ast.Tuple) -> tuple[Any, ...]: ...  # type: ignore[overload-overlap]  # Tuple items depend on their ast type
@overload
def convert_to_value(item: ast.Name) -> VariableKey: ...  # type: ignore[overload-overlap]
@overload
def convert_to_value(item: ast.AST) -> UnhandledKeyType: ...
def is_notimplemented_name_node(node: ast.AST) -> bool: ...

class Binding:
    name: str
    source: ast.AST | None
    used: Literal[False] | tuple[Scope, ast.AST]
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
    redefined: list[ast.AST]
    def __init__(self, name: str, source: ast.AST | None, full_name: str | None = None) -> None: ...
    @property
    def source_statement(self) -> str: ...

class SubmoduleImportation(Importation):
    def __init__(self, name: str, source: ast.Import | None) -> None: ...

class ImportationFrom(Importation):
    module: str
    real_name: str
    def __init__(self, name: str, source: ast.AST, module: str, real_name: str | None = None) -> None: ...

class StarImportation(Importation):
    def __init__(self, name: str, source: ast.AST) -> None: ...

class FutureImportation(ImportationFrom):
    used: tuple[Scope, ast.AST]
    def __init__(self, name: str, source: ast.AST, scope: Scope) -> None: ...

class Argument(Binding): ...
class Assignment(Binding): ...
class NamedExprAssignment(Assignment): ...

class Annotation(Binding):
    def redefines(self, other: Binding) -> Literal[False]: ...

class FunctionDefinition(Definition): ...
class ClassDefinition(Definition): ...

class ExportBinding(Binding):
    names: list[str]
    def __init__(self, name: str, source: ast.AST, scope: Scope) -> None: ...

class Scope(dict[str, Binding]):
    importStarred: bool

class ClassScope(Scope):
    def __init__(self) -> None: ...

class FunctionScope(Scope):
    usesLocals: bool
    alwaysUsed: ClassVar[set[str]]
    globals: set[str]
    returnValue: ast.expr | None
    isGenerator: bool
    def __init__(self) -> None: ...
    def unused_assignments(self) -> Iterator[tuple[str, Binding]]: ...
    def unused_annotations(self) -> Iterator[tuple[str, Annotation]]: ...

class TypeScope(Scope): ...
class GeneratorScope(Scope): ...
class ModuleScope(Scope): ...
class DoctestScope(ModuleScope): ...

class DetectClassScopedMagic:
    names: list[str]

def getNodeName(node: ast.AST) -> str: ...

TYPING_MODULES: frozenset[Literal["typing", "typing_extensions"]]

def is_typing_overload(value: Binding, scope_stack: Sequence[Scope]) -> bool: ...

class AnnotationState:
    NONE: ClassVar[Literal[0]]
    STRING: ClassVar[Literal[1]]
    BARE: ClassVar[Literal[2]]

def in_annotation(func: _F) -> _F: ...
def in_string_annotation(func: _F) -> _F: ...

if sys.version_info >= (3, 10):
    _Match: TypeAlias = ast.Match
    _MatchCase: TypeAlias = ast.match_case
    _MatchValue: TypeAlias = ast.MatchValue
    _MatchSingleton: TypeAlias = ast.MatchSingleton
    _MatchSequence: TypeAlias = ast.MatchSequence
    _MatchStar: TypeAlias = ast.MatchStar
    _MatchMapping: TypeAlias = ast.MatchMapping
    _MatchClass: TypeAlias = ast.MatchClass
    _MatchAs: TypeAlias = ast.MatchAs
    _MatchOr: TypeAlias = ast.MatchOr
else:
    # The methods using these should never be called on Python < 3.10.
    _Match: TypeAlias = Never
    _MatchCase: TypeAlias = Never
    _MatchValue: TypeAlias = Never
    _MatchSingleton: TypeAlias = Never
    _MatchSequence: TypeAlias = Never
    _MatchStar: TypeAlias = Never
    _MatchMapping: TypeAlias = Never
    _MatchClass: TypeAlias = Never
    _MatchAs: TypeAlias = Never
    _MatchOr: TypeAlias = Never

if sys.version_info >= (3, 12):
    _TypeVar: TypeAlias = ast.TypeVar
    _ParamSpec: TypeAlias = ast.ParamSpec
    _TypeVarTuple: TypeAlias = ast.TypeVarTuple
    _TypeAlias: TypeAlias = ast.TypeAlias
else:
    # The methods using these should never be called on Python < 3.12.
    _TypeVar: TypeAlias = Never
    _ParamSpec: TypeAlias = Never
    _TypeVarTuple: TypeAlias = Never
    _TypeAlias: TypeAlias = Never

class Checker:
    nodeDepth: int
    offset: tuple[int, int] | None
    builtIns: set[str]
    deadScopes: list[Scope]
    messages: list[Message]
    filename: str
    withDoctest: bool
    scopeStack: list[Scope]
    exceptHandlers: list[tuple[()] | str]
    root: ast.AST
    def __init__(
        self,
        tree: ast.AST,
        filename: str = "(none)",
        builtins: Iterable[str] | None = None,
        withDoctest: bool = False,
        file_tokens: Unused = (),
    ) -> None: ...
    def deferFunction(self, callable: _AnyFunction) -> None: ...
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
    @contextmanager
    def in_scope(self, cls: Callable[[], Scope]) -> Generator[None]: ...
    def checkDeadScopes(self) -> None: ...
    def report(self, messageClass: Callable[_P, Message], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def getParent(self, node: ast.AST) -> ast.AST: ...
    def getCommonAncestor(self, lnode: ast.AST, rnode: ast.AST, stop: ast.AST) -> ast.AST: ...
    def descendantOf(self, node: ast.AST, ancestors: ast.AST, stop: ast.AST) -> bool: ...
    def getScopeNode(self, node: ast.AST) -> ast.AST | None: ...
    def differentForks(self, lnode: ast.AST, rnode: ast.AST) -> bool: ...
    def addBinding(self, node: ast.AST, value: Binding) -> None: ...
    def getNodeHandler(self, node_class: type[ast.AST]) -> Callable[[ast.AST], None]: ...
    def handleNodeLoad(self, node: ast.AST, parent: ast.AST | None) -> None: ...
    def handleNodeStore(self, node: ast.AST) -> None: ...
    def handleNodeDelete(self, node: ast.AST) -> None: ...
    def handleChildren(self, tree: ast.AST, omit: _OmitType = None) -> None: ...
    def isLiteralTupleUnpacking(self, node: ast.AST) -> bool | None: ...
    def isDocstring(self, node: ast.AST) -> bool: ...
    def getDocstring(self, node: ast.AST) -> tuple[str, int] | tuple[None, None]: ...
    def handleNode(self, node: ast.AST | None, parent: ast.AST | None) -> None: ...
    def handleDoctests(self, node: ast.AST) -> None: ...
    def handleStringAnnotation(self, s: str, node: ast.AST, ref_lineno: int, ref_col_offset: int, err: type[Message]) -> None: ...
    def handle_annotation_always_deferred(self, annotation: ast.AST, parent: ast.AST) -> None: ...
    def handleAnnotation(self, annotation: ast.AST, node: ast.AST) -> None: ...
    def ignore(self, node: ast.AST) -> None: ...
    def DELETE(self, tree: ast.Delete, omit: _OmitType = None) -> None: ...
    def FOR(self, tree: ast.For, omit: _OmitType = None) -> None: ...
    def ASYNCFOR(self, tree: ast.AsyncFor, omit: _OmitType = None) -> None: ...
    def WHILE(self, tree: ast.While, omit: _OmitType = None) -> None: ...
    def WITH(self, tree: ast.With, omit: _OmitType = None) -> None: ...
    def WITHITEM(self, tree: ast.AST, omit: _OmitType = None) -> None: ...
    def ASYNCWITH(self, tree: ast.AsyncWith, omit: _OmitType = None) -> None: ...
    def EXPR(self, tree: ast.AST, omit: _OmitType = None) -> None: ...
    def ASSIGN(self, tree: ast.Assign, omit: _OmitType = None) -> None: ...
    def PASS(self, node: ast.AST) -> None: ...
    def BOOLOP(self, tree: ast.BoolOp, omit: _OmitType = None) -> None: ...
    def UNARYOP(self, tree: ast.UnaryOp, omit: _OmitType = None) -> None: ...
    def SET(self, tree: ast.Set, omit: _OmitType = None) -> None: ...
    def ATTRIBUTE(self, tree: ast.Attribute, omit: _OmitType = None) -> None: ...
    def STARRED(self, tree: ast.Starred, omit: _OmitType = None) -> None: ...
    def NAMECONSTANT(self, tree: ast.NameConstant, omit: _OmitType = None) -> None: ...
    def NAMEDEXPR(self, tree: ast.NamedExpr, omit: _OmitType = None) -> None: ...
    def SUBSCRIPT(self, node: ast.Subscript) -> None: ...
    def CALL(self, node: ast.Call) -> None: ...
    def BINOP(self, node: ast.BinOp) -> None: ...
    def CONSTANT(self, node: ast.Constant) -> None: ...
    def SLICE(self, tree: ast.Slice, omit: _OmitType = None) -> None: ...
    def EXTSLICE(self, tree: ast.ExtSlice, omit: _OmitType = None) -> None: ...
    def INDEX(self, tree: ast.Index, omit: _OmitType = None) -> None: ...
    def LOAD(self, node: ast.Load) -> None: ...
    def STORE(self, node: ast.Store) -> None: ...
    def DEL(self, node: ast.Del) -> None: ...
    def AUGLOAD(self, node: ast.AugLoad) -> None: ...
    def AUGSTORE(self, node: ast.AugStore) -> None: ...
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
    def COMPREHENSION(self, tree: ast.comprehension, omit: _OmitType = None) -> None: ...
    def KEYWORD(self, tree: ast.keyword, omit: _OmitType = None) -> None: ...
    def FORMATTEDVALUE(self, tree: ast.FormattedValue, omit: _OmitType = None) -> None: ...
    def JOINEDSTR(self, node: ast.AST) -> None: ...
    def DICT(self, node: ast.Dict) -> None: ...
    def IF(self, node: ast.If) -> None: ...
    def IFEXP(self, node: ast.If) -> None: ...
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
    def CLASSDEF(self, node: ast.ClassDef) -> None: ...
    def AUGASSIGN(self, node: ast.AugAssign) -> None: ...
    def TUPLE(self, node: ast.Tuple) -> None: ...
    def LIST(self, node: ast.List) -> None: ...
    def IMPORT(self, node: ast.Import) -> None: ...
    def IMPORTFROM(self, node: ast.ImportFrom) -> None: ...
    def TRY(self, node: ast.Try) -> None: ...
    if sys.version_info >= (3, 11):
        def TRYSTAR(self, node: ast.TryStar) -> None: ...
    else:
        def TRYSTAR(self, node: ast.Try) -> None: ...

    def EXCEPTHANDLER(self, node: ast.ExceptHandler) -> None: ...
    def ANNASSIGN(self, node: ast.AnnAssign) -> None: ...
    def COMPARE(self, node: ast.Compare) -> None: ...
    def MATCH(self, tree: _Match, omit: _OmitType = None) -> None: ...
    def MATCH_CASE(self, tree: _MatchCase, omit: _OmitType = None) -> None: ...
    def MATCHCLASS(self, tree: _MatchClass, omit: _OmitType = None) -> None: ...
    def MATCHOR(self, tree: _MatchOr, omit: _OmitType = None) -> None: ...
    def MATCHSEQUENCE(self, tree: _MatchSequence, omit: _OmitType = None) -> None: ...
    def MATCHSINGLETON(self, tree: _MatchSingleton, omit: _OmitType = None) -> None: ...
    def MATCHVALUE(self, tree: _MatchValue, omit: _OmitType = None) -> None: ...
    def MATCHAS(self, node: _MatchAs) -> None: ...
    def MATCHMAPPING(self, node: _MatchMapping) -> None: ...
    def MATCHSTAR(self, node: _MatchStar) -> None: ...
    def TYPEVAR(self, node: _TypeVar) -> None: ...
    def PARAMSPEC(self, node: _ParamSpec) -> None: ...
    def TYPEVARTUPLE(self, node: _TypeVarTuple) -> None: ...
    def TYPEALIAS(self, node: _TypeAlias) -> None: ...
