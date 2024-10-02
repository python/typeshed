import ast
import math
import re
import time
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NoReturn

eval_debug: int
strTypes: tuple[type[bytes], type[str]]
isPy39: bool
isPy313: bool
haveNameConstant: bool

class BadCode(ValueError): ...

augOps: dict[ast.operator, str]
__allowed_magic_methods__: frozenset[str]
__rl_unsafe__: frozenset[str]
__rl_unsafe_re__: re.Pattern[str]

def copy_locations(new_node, old_node) -> None: ...

class UntrustedAstTransformer(ast.NodeTransformer):
    names_seen: Incomplete
    nameIsAllowed: Incomplete
    def __init__(self, names_seen: Incomplete | None = None, nameIsAllowed: Incomplete | None = None) -> None: ...
    @property
    def tmpName(self): ...
    def error(self, node, msg) -> NoReturn: ...
    def guard_iter(self, node): ...
    def is_starred(self, ob): ...
    def gen_unpack_spec(self, tpl): ...
    def protect_unpack_sequence(self, target, value): ...
    def gen_unpack_wrapper(self, node, target, ctx: str = "store"): ...
    def gen_none_node(self): ...
    def gen_lambda(self, args, body): ...
    def gen_del_stmt(self, name_to_del): ...
    def transform_slice(self, slice_): ...
    def isAllowedName(self, node, name) -> None: ...
    def check_function_argument_names(self, node) -> None: ...
    def check_import_names(self, node): ...
    def gen_attr_check(self, node, attr_name): ...
    def visit_Constant(self, node): ...
    def visit_Name(self, node): ...
    def visit_Call(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_Subscript(self, node): ...
    def visit_Assign(self, node): ...
    def visit_AugAssign(self, node): ...
    # Bug in `reportlab`'s source code:
    def visit_While(node): ...  # type: ignore[override]
    def visit_ExceptHandler(self, node): ...
    def visit_With(self, node): ...
    def visit_FunctionDef(self, node): ...
    def visit_Lambda(self, node): ...
    def visit_ClassDef(self, node): ...
    def visit_Import(self, node): ...
    def visit_BinOp(self, node): ...
    visit_ImportFrom = visit_Import  # pyright: ignore[reportAssignmentType]
    visit_For = guard_iter
    visit_comprehension = guard_iter
    def generic_visit(self, node: ast.AST) -> None: ...  # type: ignore[override]
    def not_allowed(self, node: ast.AST) -> NoReturn: ...
    def visit_children(self, node): ...
    def visit(self, node): ...
    visit_Ellipsis = not_allowed
    visit_MatMult = not_allowed
    visit_Exec = not_allowed
    visit_Nonlocal = not_allowed
    visit_AsyncFunctionDef = not_allowed
    visit_Await = not_allowed
    visit_AsyncFor = not_allowed
    visit_AsyncWith = not_allowed
    visit_Print = not_allowed
    visit_Num = visit_children
    visit_Str = visit_children
    visit_Bytes = visit_children
    visit_List = visit_children
    visit_Tuple = visit_children
    visit_Set = visit_children
    visit_Dict = visit_children
    visit_FormattedValue = visit_children
    visit_JoinedStr = visit_children
    visit_NameConstant = visit_children
    visit_Load = visit_children
    visit_Store = visit_children
    visit_Del = visit_children
    visit_Starred = visit_children
    visit_Expression = visit_children
    visit_Expr = visit_children
    visit_UnaryOp = visit_children
    visit_UAdd = visit_children
    visit_USub = visit_children
    visit_Not = visit_children
    visit_Invert = visit_children
    visit_Add = visit_children
    visit_Sub = visit_children
    visit_Mult = visit_children
    visit_Div = visit_children
    visit_FloorDiv = visit_children
    visit_Pow = visit_children
    visit_Mod = visit_children
    visit_LShift = visit_children
    visit_RShift = visit_children
    visit_BitOr = visit_children
    visit_BitXor = visit_children
    visit_BitAnd = visit_children
    visit_BoolOp = visit_children
    visit_And = visit_children
    visit_Or = visit_children
    visit_Compare = visit_children
    visit_Eq = visit_children
    visit_NotEq = visit_children
    visit_Lt = visit_children
    visit_LtE = visit_children
    visit_Gt = visit_children
    visit_GtE = visit_children
    visit_Is = visit_children
    visit_IsNot = visit_children
    visit_In = visit_children
    visit_NotIn = visit_children
    visit_keyword = visit_children
    visit_IfExp = visit_children
    visit_Index = visit_children
    visit_Slice = visit_children
    visit_ExtSlice = visit_children
    visit_ListComp = visit_children
    visit_SetComp = visit_children
    visit_GeneratorExp = visit_children
    visit_DictComp = visit_children
    visit_Raise = visit_children
    visit_Assert = visit_children
    visit_Delete = visit_children
    visit_Pass = visit_children
    visit_alias = visit_children
    visit_If = visit_children
    visit_Break = visit_children
    visit_Continue = visit_children
    visit_Try = visit_children
    visit_TryFinally = visit_children
    visit_TryExcept = visit_children
    visit_withitem = visit_children
    visit_arguments = visit_children
    visit_arg = visit_children
    visit_Return = visit_children
    visit_Yield = visit_children
    visit_YieldFrom = visit_children
    visit_Global = visit_children
    visit_Module = visit_children
    visit_Param = visit_children

def astFormat(node): ...

class __rl_SafeIter__:
    __rl_iter__: Incomplete
    __rl_owner__: Incomplete
    def __init__(self, it, owner) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

__rl_safe_builtins__: Incomplete

def safer_globals(g: Incomplete | None = None): ...

math_log10 = math.log10
__rl_undef__: Incomplete

class __RL_SAFE_ENV__:
    __time_time__ = time.time
    __weakref_ref__: Incomplete
    __slicetype__: Incomplete
    timeout: Incomplete
    allowed_magic_methods: Incomplete
    __rl_gen_range__: Incomplete
    __rl_real_iter__: Incomplete
    real_bi: Incomplete
    bi_replace: Incomplete
    __rl_builtins__: Incomplete
    def __init__(
        self,
        timeout: Incomplete | None = None,
        allowed_magic_methods: Incomplete | None = None,
        allowed_magic_names: Incomplete | None = None,
    ) -> None: ...
    def __rl_type__(self, *args): ...
    def __rl_check__(self) -> None: ...
    def __rl_sd__(self, obj): ...
    def __rl_getiter__(self, it): ...
    def __rl_max__(self, arg, *args, **kwds): ...
    def __rl_min__(self, arg, *args, **kwds): ...
    def __rl_sum__(self, sequence, start: int = 0): ...
    def __rl_enumerate__(self, seq): ...
    def __rl_zip__(self, *args): ...
    def __rl_hasattr__(self, obj, name): ...
    def __rl_filter__(self, f, seq): ...
    def __rl_map__(self, f, seq): ...
    def __rl_any__(self, seq): ...
    def __rl_all__(self, seq): ...
    def __rl_sorted__(self, seq, **kwds): ...
    def __rl_reversed__(self, seq): ...
    def __rl_range__(self, start, *args): ...
    def __rl_set__(self, it): ...
    def __rl_frozenset__(self, it=()): ...
    def __rl_iter_unpack_sequence__(self, it, spec, _getiter_) -> Generator[Incomplete, None, None]: ...
    def __rl_unpack_sequence__(self, it, spec, _getiter_): ...
    def __rl_is_allowed_name__(self, name, crash: bool = True) -> bool: ...
    def __rl_getattr__(self, obj, a, *args): ...
    def __rl_getitem__(self, obj, a): ...
    __rl_tmax__: int
    __rl_max_len__: int
    __rl_max_pow_digits__: int
    def __rl_add__(self, a, b): ...
    def __rl_mult__(self, a, b): ...
    def __rl_pow__(self, a, b): ...
    def __rl_augAssign__(self, op, v, i): ...
    def __rl_apply__(self, func, args, kwds): ...
    def __rl_args_iter__(self, *args): ...
    def __rl_list__(self, it): ...
    def __rl_compile__(
        self,
        src,
        fname: str = "<string>",
        mode: str = "eval",
        flags: int = 0,
        inherit: bool = True,
        visit: Incomplete | None = None,
    ): ...
    __rl_limit__: Incomplete
    def __rl_safe_eval__(
        self,
        expr,
        g,
        l,
        mode,
        timeout: Incomplete | None = None,
        allowed_magic_methods: Incomplete | None = None,
        __frame_depth__: int = 3,
        allowed_magic_names: Incomplete | None = None,
    ): ...

class __rl_safe_eval__:
    mode: str
    env: Incomplete
    def __init__(self) -> None: ...
    def __call__(
        self,
        expr,
        g: Incomplete | None = None,
        l: Incomplete | None = None,
        timeout: Incomplete | None = None,
        allowed_magic_methods: Incomplete | None = None,
        allowed_magic_names: Incomplete | None = None,
    ): ...

class __rl_safe_exec__(__rl_safe_eval__):
    mode: str

def rl_extended_literal_eval(expr, safe_callables: Incomplete | None = None, safe_names: Incomplete | None = None): ...

rl_safe_exec: __rl_safe_exec__
rl_safe_eval: __rl_safe_eval__

def __fix_set__(value, default=...): ...
def rl_less_safe_eval(expr, NS): ...
