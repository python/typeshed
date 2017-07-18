# Stubs for unittest.mock

import sys
from typing import Any, Optional

if sys.version_info >= (3, 3):
    FILTER_DIR = ...  # type: Any

    class _slotted: ...

    class _SentinelObject:
        name = ...  # type: Any
        def __init__(self, name: Any) -> None: ...

    class _Sentinel:
        def __init__(self) -> None: ...
        def __getattr__(self, name: str) -> Any: ...

    sentinel = ...  # type: Any
    DEFAULT = ...  # type: Any

    class _CallList(list):
        def __contains__(self, value: Any) -> bool: ...

    class _MockIter:
        obj = ...  # type: Any
        def __init__(self, obj: Any) -> None: ...
        def __iter__(self) -> Any: ...
        def __next__(self) -> Any: ...

    class Base:
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class NonCallableMock(Any): # type: ignore
        def __new__(cls, *args: Any, **kw: Any) -> Any: ...
        def __init__(self, spec: Optional[Any] = None, wraps: Optional[Any] = None, name: Optional[Any] = None, spec_set: Optional[Any] = None, parent: Optional[Any] = None, _spec_state: Optional[Any] = None, _new_name: Any ='', _new_parent: Optional[Any] = None, _spec_as_instance: Any = False, _eat_self: Optional[Any] = None, unsafe: Any = False, **kwargs: Any) -> None: ...
        def attach_mock(self, mock: Any, attribute: Any) -> Any: ...
        def mock_add_spec(self, spec: Any, spec_set: Any = False) -> Any: ...
        return_value = ...  # type: Any
        __class__ = ...  # type: type
        called = ...  # type: Any
        call_count = ...  # type: Any
        call_args = ...  # type: Any
        call_args_list = ...  # type: Any
        mock_calls = ...  # type: Any
        side_effect = ...  # type: Any
        method_calls = ...  # type: Any
        def reset_mock(self, visited: Optional[bool] = None) -> None: ...
        def configure_mock(self, **kwargs: Any) -> None: ...
        def __getattr__(self, name: Any) -> Any: ...
        def __dir__(self) -> Any: ...
        def __setattr__(self, name: Any, value: Any) -> None: ...
        def __delattr__(self, name: Any) -> None: ...
        def assert_not_called(_mock_self) -> None: ...
        def assert_called_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
        def assert_called_once_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
        def assert_has_calls(self, calls: Any, any_order: bool = False) -> None: ...
        def assert_any_call(self, *args: Any, **kwargs: Any) -> None: ...

    class CallableMixin(Base):
        side_effect = ...  # type: Any
        def __init__(self, spec: Optional[Any] = None, side_effect: Optional[Any] = None, return_value: Any = ..., wraps: Optional[Any] = None, name: Optional[Any] = None, spec_set: Optional[Any] = None, parent: Optional[Any] = None, _spec_state: Optional[Any] = None, _new_name: Any = '', _new_parent: Optional[Any] = None, **kwargs: Any) -> None: ...
        def __call__(_mock_self, *args: Any, **kwargs: Any) -> Any: ...

    class Mock(CallableMixin, NonCallableMock):
        def __init__(self, spec: Any = ..., spec_set: Any = ..., side_effect: Any = ..., return_value: Any = ..., wraps: Any = ..., name: Any = ..., **kwargs: Any) -> None: ...

    class _patch:
        attribute_name = ...  # type: Any
        getter = ...  # type: Any
        attribute = ...  # type: Any
        new = ...  # type: Any
        new_callable = ...  # type: Any
        spec = ...  # type: Any
        create = ...  # type: Any
        has_local = ...  # type: Any
        spec_set = ...  # type: Any
        autospec = ...  # type: Any
        kwargs = ...  # type: Any
        additional_patchers = ...  # type: Any
        def __init__(self, getter: Any, attribute: Any, new: Any, spec: Any, create: Any, spec_set: Any, autospec: Any, new_callable: Any, kwargs: Any) -> None: ...
        def copy(self) -> Any: ...
        def __call__(self, func: Any) -> Any: ...
        def decorate_class(self, klass: Any) -> Any: ...
        def decorate_callable(self, func: Any) -> Any: ...
        def get_original(self) -> Any: ...
        target = ...  # type: Any
        temp_original = ...  # type: Any
        is_local = ...  # type: Any
        def __enter__(self) -> Any: ...
        def __exit__(self, *exc_info: Any) -> Any: ...
        def start(self) -> Any: ...
        def stop(self) -> Any: ...

    class _patcher:
        def __call__(self, target: Any, new: Optional[Any] = None, spec: Optional[Any] = None, create: Any = False, spec_set: Optional[Any] = None, autospec: Optional[Any] = None, new_callable: Optional[Any] = None, **kwargs: Any) -> Any: ...
        def object(self, target: Any, attribute: str, new: Optional[Any] = None, spec: Optional[Any] = None, create: Any = False, spec_set: Optional[Any] = None, autospec: Optional[Any] = None, new_callable: Optional[Any] = None, **kwargs: Any) -> _patch: ...

    patch = ...  # type: _patcher

    class _patch_dict:
        in_dict = ...  # type: Any
        values = ...  # type: Any
        clear = ...  # type: Any
        def __init__(self, in_dict: Any, values: Any = ..., clear: Any = False, **kwargs: Any) -> None: ...
        def __call__(self, f: Any) -> Any: ...
        def decorate_class(self, klass: Any) -> Any: ...
        def __enter__(self) -> Any: ...
        def __exit__(self, *args: Any) -> Any: ...
        start = ...  # type: Any
        stop = ...  # type: Any

    class MagicMixin:
        def __init__(self, *args: Any, **kw: Any) -> None: ...

    class NonCallableMagicMock(MagicMixin, NonCallableMock):
        def __init__(self) -> None: ...
        def mock_add_spec(self, spec: Any, spec_set: Any = False) -> Any: ...

    class MagicMock(MagicMixin, Mock):
        def __init__(self, spec: Any = ..., spec_set: Any = ..., side_effect: Any = ..., return_value: Any = ..., wraps: Any = ..., name: Any = ..., **kwargs: Any) -> None: ...
        def mock_add_spec(self, spec: Any, spec_set: Any = False) -> Any: ...

    class MagicProxy:
        name = ...  # type: Any
        parent = ...  # type: Any
        def __init__(self, name: Any, parent: Any) -> None: ...
        def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
        def create_mock(self) -> Any: ...
        def __get__(self, obj: Any, _type: Optional[Any] = None) -> Any: ...

    class _ANY:
        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...

    ANY = ...  # type: Any

    class _Call(tuple):
        def __new__(cls, value: Any = ..., name: Optional[Any] = None, parent: Optional[Any] = None, two: bool = False, from_kall: bool = True) -> Any: ...
        name = ...  # type: Any
        parent = ...  # type: Any
        from_kall = ...  # type: Any
        def __init__(self, value: Any = ..., name: Optional[Any] = None, parent: Optional[Any] = None, two: bool = False, from_kall: bool = True) -> None: ...
        def __eq__(self, other: Any) -> bool: ...
        __ne__ = ...  # type: Any
        def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
        def __getattr__(self, attr: Any) -> Any: ...
        def count(self, *args: Any, **kwargs: Any) -> Any: ...
        def index(self, *args: Any, **kwargs: Any) -> Any: ...
        def call_list(self) -> Any: ...

    call = ...  # type: Any

    def create_autospec(spec: Any, spec_set: Any = False, instance: Any = False, _parent: Optional[Any] = None, _name: Optional[Any] = None, **kwargs: Any) -> Any: ...

    class _SpecState:
        spec = ...  # type: Any
        ids = ...  # type: Any
        spec_set = ...  # type: Any
        parent = ...  # type: Any
        instance = ...  # type: Any
        name = ...  # type: Any
        def __init__(self, spec: Any, spec_set: Any = False, parent: Optional[Any] = None, name: Optional[Any] = None, ids: Optional[Any] = None, instance: Any = False) -> None: ...

    def mock_open(mock: Optional[Any] = None, read_data: Any = '') -> Any: ...

    class PropertyMock(Mock):
        def __get__(self, obj: Any, obj_type: Any) -> Any: ...
        def __set__(self, obj: Any, val: Any) -> Any: ...
