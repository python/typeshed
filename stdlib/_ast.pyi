import sys
from ast import (
    AST as AST,
    Add as Add,
    And as And,
    AnnAssign as AnnAssign,
    Assert as Assert,
    Assign as Assign,
    AsyncFor as AsyncFor,
    AsyncFunctionDef as AsyncFunctionDef,
    AsyncWith as AsyncWith,
    Attribute as Attribute,
    AugAssign as AugAssign,
    Await as Await,
    BinOp as BinOp,
    BitAnd as BitAnd,
    BitOr as BitOr,
    BitXor as BitXor,
    BoolOp as BoolOp,
    Break as Break,
    Call as Call,
    ClassDef as ClassDef,
    Compare as Compare,
    Constant as Constant,
    Continue as Continue,
    Del as Del,
    Delete as Delete,
    Dict as Dict,
    DictComp as DictComp,
    Div as Div,
    Eq as Eq,
    ExceptHandler as ExceptHandler,
    Expr as Expr,
    Expression as Expression,
    FloorDiv as FloorDiv,
    For as For,
    FormattedValue as FormattedValue,
    FunctionDef as FunctionDef,
    GeneratorExp as GeneratorExp,
    Global as Global,
    Gt as Gt,
    GtE as GtE,
    If as If,
    IfExp as IfExp,
    Import as Import,
    ImportFrom as ImportFrom,
    In as In,
    Interactive as Interactive,
    Invert as Invert,
    Is as Is,
    IsNot as IsNot,
    JoinedStr as JoinedStr,
    Lambda as Lambda,
    List as List,
    ListComp as ListComp,
    Load as Load,
    LShift as LShift,
    Lt as Lt,
    LtE as LtE,
    MatMult as MatMult,
    Mod as Mod,
    Module as Module,
    Mult as Mult,
    Name as Name,
    Nonlocal as Nonlocal,
    Not as Not,
    NotEq as NotEq,
    NotIn as NotIn,
    Or as Or,
    Pass as Pass,
    Pow as Pow,
    Raise as Raise,
    Return as Return,
    RShift as RShift,
    Set as Set,
    SetComp as SetComp,
    Slice as Slice,
    Starred as Starred,
    Store as Store,
    Sub as Sub,
    Subscript as Subscript,
    Try as Try,
    Tuple as Tuple,
    UAdd as UAdd,
    UnaryOp as UnaryOp,
    USub as USub,
    While as While,
    With as With,
    Yield as Yield,
    YieldFrom as YieldFrom,
    alias as alias,
    arg as arg,
    arguments as arguments,
    boolop as boolop,
    cmpop as cmpop,
    comprehension as comprehension,
    excepthandler as excepthandler,
    expr as expr,
    expr_context as expr_context,
    keyword as keyword,
    mod as mod,
    operator as operator,
    stmt as stmt,
    unaryop as unaryop,
    withitem as withitem,
)
from typing_extensions import Literal

if sys.version_info >= (3, 12):
    from ast import ParamSpec as ParamSpec, TypeVar as TypeVar, TypeVarTuple as TypeVarTuple, type_param as type_param

if sys.version_info >= (3, 11):
    from ast import TryStar as TryStar

if sys.version_info >= (3, 10):
    from ast import (
        MatchAs as MatchAs,
        MatchClass as MatchClass,
        MatchMapping as MatchMapping,
        MatchOr as MatchOr,
        MatchSequence as MatchSequence,
        MatchSingleton as MatchSingleton,
        MatchStar as MatchStar,
        MatchValue as MatchValue,
        match_case as match_case,
        pattern as pattern,
    )

if sys.version_info >= (3, 8):
    from ast import FunctionType as FunctionType, TypeIgnore as TypeIgnore, type_ignore as type_ignore

if sys.version_info < (3, 9):
    from ast import (
        AugLoad as AugLoad,
        AugStore as AugStore,
        ExtSlice as ExtSlice,
        Index as Index,
        Param as Param,
        Suite as Suite,
        slice as slice,
    )

if sys.version_info < (3, 8):
    from ast import Bytes as Bytes, Ellipsis as Ellipsis, NameConstant as NameConstant, Num as Num, Str as Str

PyCF_ONLY_AST: Literal[1024]
if sys.version_info >= (3, 8):
    PyCF_ALLOW_TOP_LEVEL_AWAIT: Literal[8192]
    PyCF_TYPE_COMMENTS: Literal[4096]
