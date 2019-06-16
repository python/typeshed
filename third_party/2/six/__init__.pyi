# Stubs for six (Python 2.7)

from __future__ import print_function

import types
import typing
import unittest

# Exports
from __builtin__ import unichr as unichr
from functools import wraps as wraps
from StringIO import StringIO as BytesIO
from typing import (
    Any,
    AnyStr,
    Callable,
    Dict,
    ItemsView,
    Iterable,
    KeysView,
    Mapping,
    NoReturn,
    Optional,
    Pattern,
    Text,
    Tuple,
    Type,
    TypeVar,
    Union,
    ValuesView,
    overload,
)

from . import moves

_T = TypeVar("_T")
_K = TypeVar("_K")
_V = TypeVar("_V")

# TODO make constant, then move this stub to 2and3
# https://github.com/python/typeshed/issues/17
PY2 = True
PY3 = False
PY34 = False

string_types = (str, unicode)
integer_types = (int, long)
class_types = (type, types.ClassType)
text_type = unicode
binary_type = str

MAXSIZE: int

# def add_move
# def remove_move

def advance_iterator(it: typing.Iterator[_T]) -> _T: ...

next = advance_iterator

def callable(obj: object) -> bool: ...
def get_unbound_function(unbound: types.MethodType) -> types.FunctionType: ...
def create_bound_method(func: types.FunctionType, obj: object) -> types.MethodType: ...
def create_unbound_method(func: types.FunctionType, cls: Union[type, types.ClassType]) -> types.MethodType: ...

class Iterator:
    def next(self) -> Any: ...

def get_method_function(meth: types.MethodType) -> types.FunctionType: ...
def get_method_self(meth: types.MethodType) -> Optional[object]: ...
def get_function_closure(fun: types.FunctionType) -> Optional[Tuple[types._Cell, ...]]: ...
def get_function_code(fun: types.FunctionType) -> types.CodeType: ...
def get_function_defaults(fun: types.FunctionType) -> Optional[Tuple[Any, ...]]: ...
def get_function_globals(fun: types.FunctionType) -> Dict[str, Any]: ...
def iterkeys(d: Mapping[_K, _V]) -> typing.Iterator[_K]: ...
def itervalues(d: Mapping[_K, _V]) -> typing.Iterator[_V]: ...
def iteritems(d: Mapping[_K, _V]) -> typing.Iterator[Tuple[_K, _V]]: ...

# def iterlists

def viewkeys(d: Mapping[_K, _V]) -> KeysView[_K]: ...
def viewvalues(d: Mapping[_K, _V]) -> ValuesView[_V]: ...
def viewitems(d: Mapping[_K, _V]) -> ItemsView[_K, _V]: ...
def b(s: str) -> binary_type: ...
def u(s: str) -> text_type: ...

int2byte = chr

def byte2int(bs: binary_type) -> int: ...
def indexbytes(buf: binary_type, i: int) -> int: ...
def iterbytes(buf: binary_type) -> typing.Iterator[int]: ...
def assertCountEqual(self: unittest.TestCase, first: Iterable[_T], second: Iterable[_T], msg: str = ...) -> None: ...
@overload
def assertRaisesRegex(self: unittest.TestCase, msg: str = ...) -> Any: ...
@overload
def assertRaisesRegex(self: unittest.TestCase, callable_obj: Callable[..., Any], *args: Any, **kwargs: Any) -> Any: ...
def assertRegex(
    self: unittest.TestCase, text: AnyStr, expected_regex: Union[AnyStr, Pattern[AnyStr]], msg: str = ...
) -> None: ...
def reraise(
    tp: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[types.TracebackType] = ...
) -> NoReturn: ...
def exec_(_code_: Union[unicode, types.CodeType], _globs_: Dict[str, Any] = ..., _locs_: Dict[str, Any] = ...): ...
def raise_from(value: Union[BaseException, Type[BaseException]], from_value: Optional[BaseException]) -> NoReturn: ...

print_ = print

def with_metaclass(meta: type, *bases: type) -> type: ...
def add_metaclass(metaclass: type) -> Callable[[_T], _T]: ...
def ensure_binary(s: Union[bytes, Text], encoding: str = ..., errors: str = ...) -> bytes: ...
def ensure_str(s: Union[bytes, Text], encoding: str = ..., errors: str = ...) -> str: ...
def ensure_text(s: Union[bytes, Text], encoding: str = ..., errors: str = ...) -> Text: ...
def python_2_unicode_compatible(klass: _T) -> _T: ...
