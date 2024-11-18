from __future__ import annotations
# pyright: reportUnnecessaryTypeIgnoreComment=true

from functools import cache
from collections.abc import Callable
from typing import (
    final,
    assert_type,
    TYPE_CHECKING,
    overload,
    override,
    Any,
    Self,
    TypeVar,
    ParamSpec,
    Generic,
)
from dataclasses import dataclass

P = ParamSpec("P")
R = TypeVar("R")

@cache
def cached_fn(arg: int, arg2: str) -> int:
    return arg

@dataclass
class MemberVarCached(Generic[P, R]):
    member_callable: Callable[P, R]

@cache
def cached_fn_takes_t(arg: MemberVarCached[..., Any], arg2: str) -> int:
    return 1


vc = MemberVarCached(cached_fn)
vc.member_callable(1, "")
assert_type(vc.member_callable(1, ""), int)

vc_t = MemberVarCached(cached_fn_takes_t)
vc_t.member_callable(vc_t, "")

if TYPE_CHECKING:
    # type errors - correct
    vc_t.member_callable("") # type: ignore[call-arg,arg-type] # pyright: ignore[reportCallIssue]
    vc.member_callable(1, 1) # type: ignore[arg-type] # pyright: ignore[reportArgumentType]
    vc.member_callable(1)  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
    vc.member_callable("1") # type: ignore[call-arg,arg-type] # pyright: ignore[reportCallIssue]

class CFnCls:
    @cache
    def fn(self, arg: int) -> int:
        print("method fn called")
        return arg

    @cache
    def fn_bad_self_name(this_t, arg: int) -> int:
        print("method fn called")
        return arg

    @classmethod
    @cache
    def cls_fn(cls, arg: int) -> int:
        print("class fn called")
        return arg

    @classmethod
    @cache
    def cls_fn_bad_name(my_class_type, arg: int) -> int:
        print("class fn called")
        return arg

    @classmethod
    @cache
    def cls_fn_positional_only(__cls, arg: int) -> int:
        print("class fn called")
        return arg

    @classmethod
    @cache
    def cls_fn_explicit_positional_only(_cls, arg: int, /) -> int:
        print("class fn called")
        return arg


    @staticmethod
    @cache
    def st_fn(arg: int) -> int:
        print("static fn called")
        return arg

    @staticmethod
    @cache
    def st_fn_clst_arg(arg: type[CFnCls]) -> int:
        print("static fn called")
        return 1

    @staticmethod
    @cache
    def st_fn_strt_arg(arg: type[str]) -> int:
        print("static fn called")
        return 1

    @staticmethod
    @cache
    def st_fn_self_t_arg(arg: CFnCls) -> int:
        print("static fn called")
        return 1

    @property
    @cache
    def prp_fn(self) -> int:
        print("property fn called")
        return 1

class CFnSubCls(CFnCls):
    pass

cfn_inst = CFnCls()
cfn_inst.fn(1)
cfn_inst.fn.__wrapped__(cfn_inst, 1)
cfn_inst.prp_fn
CFnCls.fn.__wrapped__(CFnCls(), 1)
CFnCls.st_fn(1)
CFnCls.st_fn.__wrapped__(1)
CFnCls.cls_fn(1)
CFnCls.cls_fn.__wrapped__(CFnCls, 1)
cfn_inst.fn(1)
CFnCls.st_fn(1)
CFnCls.cls_fn(1)
CFnCls.cls_fn_bad_name(1)
CFnCls.cls_fn_positional_only(1)
CFnCls().cls_fn_positional_only(1)
CFnCls.cls_fn_explicit_positional_only(1)
CFnCls().cls_fn_explicit_positional_only(1)

# incorrect type error. If a static method
# takes the type of the enclosing class as
# the first argument there's a false positive.
CFnCls.st_fn_clst_arg(CFnCls)
CFnSubCls.st_fn_clst_arg(CFnSubCls)
# If a static method takes an instance of the
# enclosing class as its first argument,
# there's an error if accessed via an instance.
CFnSubCls.st_fn_self_t_arg(CFnSubCls())
CFnSubCls().st_fn_self_t_arg(CFnSubCls())
# but a different type is fine
CFnCls.st_fn_strt_arg(str)

assert_type(cfn_inst.fn(1), int)
assert_type(CFnCls.st_fn(1), int)
assert_type(CFnCls.cls_fn(1), int)
assert_type(cfn_inst.prp_fn, int)
CFnCls().fn.cache_clear()
CFnCls.fn.cache_clear()
CFnCls.st_fn.cache_clear()
CFnCls.cls_fn.cache_clear()
if TYPE_CHECKING:
    # type errors - correct
    CFnCls().fn(1, 1) # type: ignore[call-arg,misc] # pyright: ignore[reportCallIssue]
    CFnCls().fn.__wrapped__(CFnCls(), 1, 1) # type: ignore[call-arg] # pyright: ignore[reportCallIssue]
    CFnCls.fn(arg=1) # type: ignore[call-arg] # pyright: ignore[reportCallIssue]
    CFnCls.st_fn(1, 1) # type: ignore[call-arg,arg-type,misc] # pyright: ignore[reportCallIssue]
    CFnCls.cls_fn(1, 1) # type: ignore[arg-type,call-arg] # pyright: ignore[reportCallIssue]
    CFnCls.cls_fn_positional_only(CFnCls, 1) # type: ignore[arg-type,call-arg] # pyright: ignore[reportCallIssue]
    CFnCls().cls_fn_positional_only(CFnCls, 1) # type: ignore[call-arg,arg-type,misc] # pyright: ignore[reportCallIssue]
    CFnCls.cls_fn_explicit_positional_only(CFnCls, 1) # type: ignore[arg-type,call-arg] # pyright: ignore[reportCallIssue]
    CFnCls().cls_fn_explicit_positional_only(CFnCls, 1) # type: ignore[call-arg,arg-type,misc] # pyright: ignore[reportCallIssue]

@cache
def fn(arg: int) -> int:
    return arg

@cache
def df_fn(arg: int, darg: str = "default"):
    print("default fn called")
    return darg
df_fn(1)

fn(1)
assert_type(fn(1), int)
if TYPE_CHECKING:
    # type error - correct
    fn(1, 2) # type: ignore[call-arg] # pyright: ignore[reportCallIssue]
fn.cache_clear()

@overload
@cache
def fn_overload(arg: int) -> int:
    ...
@overload
@cache
def fn_overload(arg: str) -> str:
    return arg

@cache
def fn_overload(arg: int | str) -> int | str:
    return arg

fn_overload(1)
fn_overload("1")
# behavior varies between type checkers.
assert_type(fn_overload(1), int)
assert_type(fn_overload("1"), str)
fn_overload.cache_clear()
if TYPE_CHECKING:
    # type error - correct
    fn_overload(frozenset({1,2})) # type: ignore[call-overload] # pyright: ignore[reportArgumentType]


class Unhashable:
    @override
    def __eq__(self, value: object) -> bool:
        return False

@cache
def no_cache(arg: Unhashable, arg2: int) -> None:
    pass

if TYPE_CHECKING:
    # This is not correctly rejected.
    no_cache(Unhashable(), 2) # type: ignore[arg-type] # pyright: ignore[reportArgumentType]

class MemberVarBound(Generic[P, R]):
    @cache
    def equals(self, other: Self) -> bool:
        return False
    member_fn: Callable[P, R]

def set_member(lhs: MemberVarBound[..., Any], rhs: MemberVarBound[..., Any]) -> None:
    lhs.member_fn = rhs.equals
    lhs.member_fn(rhs)

    if TYPE_CHECKING:
        lhs.member_fn() # type: ignore[call-arg] # pyright: ignore[reportCallIssue]

from abc import ABCMeta, abstractmethod

class CustomABC(metaclass=ABCMeta):

    @abstractmethod
    def foo(self, arg: int) -> int:
        ...

@final
class ABCConcrete(CustomABC):
    @override
    def foo(self, arg: int) -> int:
        return 1

    @cache
    def abc_fn(self, arg: str) -> str:
        return arg

    @classmethod
    @cache
    def abc_cm(cls, arg: str) -> str:
        return arg

ABCConcrete().abc_fn("1")
ABCConcrete.abc_fn(ABCConcrete(), "1")
ABCConcrete.abc_cm("")
