from __future__ import annotations

from functools import cache, cached_property, lru_cache, update_wrapper, wraps
from typing import Callable, ParamSpec, TypeVar
from typing_extensions import assert_type

P = ParamSpec("P")
T_co = TypeVar("T_co", covariant=True)

#
# Tests for @wraps
#


def my_decorator(func: Callable[P, T_co]) -> Callable[P, T_co]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T_co:
        print(args)
        return func(*args, **kwargs)

    # verify that the wrapped function has all these attributes
    wrapper.__annotations__ = func.__annotations__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    wrapper.__name__ = func.__name__
    wrapper.__qualname__ = func.__qualname__
    return wrapper


def check_wraps_function() -> None:
    def wrapped(x: int) -> None: ...
    @wraps(wrapped)
    def identical_wrapper(x: int) -> None: ...
    @wraps(wrapped)
    def other_signature_wrapper(x: str, y: float) -> None: ...
    @wraps(wrapped)
    def no_args_wrapper() -> None: ...
    @wraps(wrapped)
    def keyword_only_wrapper(*, x: int) -> None: ...

    identical_wrapper(3)
    identical_wrapper(x=3)
    other_signature_wrapper("parrot", 42.0)
    no_args_wrapper()
    keyword_only_wrapper(x=3)


def check_update_wrapper() -> None:
    def wrapped(x: int) -> None: ...
    def wrapper(*, text: str) -> int:
        return len(text)

    updated = update_wrapper(wrapper, wrapped)
    assert_type(updated(text="parrot"), int)
    assert_type(updated.__wrapped__(3), None)


def check_wraps_method() -> None:
    class Wrapped:
        def wrapped(self, x: int) -> None: ...
        @wraps(wrapped)
        def wrapper(self, x: int) -> None: ...

    class Wrapper:
        @wraps(Wrapped.wrapped)
        def method(self, x: int) -> None: ...

    @wraps(Wrapped.wrapped)
    def func_wrapper(x: int) -> None: ...

    assert_type(Wrapped.wrapper(Wrapped(), x=3), None)
    assert_type(Wrapped().wrapper(3), None)
    assert_type(Wrapped().wrapper(x=3), None)
    assert_type(Wrapper().method(3), None)
    func_wrapper(3)
    func_wrapper(x=3)


#
# Tests for @cache
#


@cache
def check_cache(x: int) -> int:
    return x * 2


assert_type(check_cache(3), int)
# Type checkers should check the argument type, but this is currently not
# possible. See https://github.com/python/typeshed/issues/6347 and
# https://github.com/python/typeshed/issues/11280.
# check_cached("invalid")  # xtype: ignore

assert_type(check_cache.cache_info().misses, int)


#
# Tests for @lru_cache
#


@lru_cache
def check_lru_cache(x: int) -> int:
    return x * 2


@lru_cache(maxsize=32)
def check_lru_cache_with_maxsize(x: int) -> int:
    return x * 2


assert_type(check_lru_cache(3), int)
assert_type(check_lru_cache_with_maxsize(3), int)
# Type checkers should check the argument type, but this is currently not
# possible. See https://github.com/python/typeshed/issues/6347 and
# https://github.com/python/typeshed/issues/11280.
# check_lru_cache("invalid")  # xtype: ignore
# check_lru_cache_with_maxsize("invalid")  # xtype: ignore

assert_type(check_lru_cache.cache_info().misses, int)
assert_type(check_lru_cache_with_maxsize.cache_info().misses, int)


#
# Tests for @cached_property
#


class A:
    def __init__(self, x: int):
        self.x = x

    @cached_property
    def x(self) -> int:
        return 0


assert_type(A(x=1).x, int)


class B:
    @cached_property
    def x(self) -> int:
        return 0


def check_cached_property_settable(x: int) -> None:
    b = B()
    assert_type(b.x, int)
    b.x = x
    assert_type(b.x, int)


# https://github.com/python/typeshed/issues/10048
class Parent: ...


class Child(Parent): ...


class X:
    @cached_property
    def some(self) -> Parent:
        return Parent()


class Y(X):
    @cached_property
    def some(self) -> Child:  # safe override
        return Child()


class CachedParent:
    @cache
    def method(self) -> Parent:
        return Parent()


class CachedChild(CachedParent):
    @cache
    def method(self) -> Child:
        return Child()
