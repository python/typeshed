from _typeshed import Incomplete
from collections.abc import Callable
from enum import Enum
from typing import Generic, TypeVar
from typing_extensions import ParamSpec

from . import elements, roles
from .base import Options
from .operators import ColumnOperators

_T = TypeVar("_T")
_L = TypeVar("_L", None, int, bool, str, bytes, Enum)  # Any valid Literal type
_P = ParamSpec("_P")

class LambdaOptions(Options):
    enable_tracking: bool
    track_closure_variables: bool
    track_on: Incomplete
    global_track_bound_values: bool
    track_bound_values: bool
    lambda_cache: Incomplete

def lambda_stmt(
    lmb,
    enable_tracking: bool = True,
    track_closure_variables: bool = True,
    track_on: Incomplete | None = None,
    global_track_bound_values: bool = True,
    track_bound_values: bool = True,
    lambda_cache: Incomplete | None = None,
): ...

class LambdaElement(elements.ClauseElement):
    __visit_name__: str
    parent_lambda: Incomplete
    fn: Incomplete
    role: Incomplete
    tracker_key: Incomplete
    opts: Incomplete
    def __init__(self, fn, role, opts=..., apply_propagate_attrs: Incomplete | None = None) -> None: ...
    def __getattr__(self, key: str): ...

class DeferredLambdaElement(LambdaElement):
    lambda_args: Incomplete
    def __init__(self, fn, role, opts=..., lambda_args=()) -> None: ...

class StatementLambdaElement(roles.AllowsLambdaRole, LambdaElement):
    def __add__(self, other): ...
    def add_criteria(
        self,
        other,
        enable_tracking: bool = True,
        track_on: Incomplete | None = None,
        track_closure_variables: bool = True,
        track_bound_values: bool = True,
    ): ...
    def spoil(self): ...

class NullLambdaStatement(roles.AllowsLambdaRole, elements.ClauseElement):
    __visit_name__: str
    def __init__(self, statement) -> None: ...
    def __getattr__(self, key: str): ...
    def __add__(self, other): ...
    def add_criteria(self, other, **kw): ...

class LinkedLambdaElement(StatementLambdaElement):
    role: Incomplete
    opts: Incomplete
    fn: Incomplete
    parent_lambda: Incomplete
    tracker_key: Incomplete
    def __init__(self, fn, parent_lambda, opts) -> None: ...

class AnalyzedCode:
    @classmethod
    def get(cls, fn, lambda_element, lambda_kw, **kw): ...
    track_bound_values: Incomplete
    track_closure_variables: Incomplete
    bindparam_trackers: Incomplete
    closure_trackers: Incomplete
    build_py_wrappers: Incomplete
    def __init__(self, fn, lambda_element, opts) -> None: ...

class NonAnalyzedFunction:
    closure_bindparams: Incomplete
    bindparam_trackers: Incomplete
    expr: Incomplete
    def __init__(self, expr) -> None: ...
    @property
    def expected_expr(self): ...

class AnalyzedFunction:
    analyzed_code: Incomplete
    fn: Incomplete
    closure_pywrappers: Incomplete
    tracker_instrumented_fn: Incomplete
    expr: Incomplete
    bindparam_trackers: Incomplete
    expected_expr: Incomplete
    is_sequence: Incomplete
    propagate_attrs: Incomplete
    closure_bindparams: Incomplete
    def __init__(self, analyzed_code, lambda_element, apply_propagate_attrs, fn) -> None: ...

class PyWrapper(ColumnOperators[_T], Generic[_T]):
    fn: Incomplete
    track_bound_values: Incomplete
    def __init__(
        self,
        fn,
        name,
        to_evaluate,
        closure_index: Incomplete | None = None,
        getter: Incomplete | None = None,
        track_bound_values: bool = True,
    ) -> None: ...
    def __call__(self, *arg, **kw): ...
    def operate(self, op: Callable[_P, _T], *other: _P.args, **kwargs: _P.kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
    def reverse_operate(self, op: Callable[..., _T], other, **kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
    def __clause_element__(self): ...  # Field not always present.
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __getattribute__(self, key: str): ...
    def __iter__(self): ...
    # "Dictionary keys / list indexes inside of a cached lambda must be Python literals only"
    def __getitem__(self, key: Callable[..., _L]) -> _L: ...  # type: ignore[override]  # Custom __getitem__

def insp(lmb): ...
