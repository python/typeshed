from collections.abc import Callable
from types import NotImplementedType
from typing import Any
from typing_extensions import assert_type


def check_not_implemented_type() -> None:
    union_with_callable: Callable[[], None] | NotImplementedType
    if callable(union_with_callable):
        assert_type(union_with_callable, Callable[[], None])

    class _Class:
        def __call__(self, *args: Any, **kwds: Any) -> Any:
            pass

    union_with_class: _Class | NotImplementedType
    if callable(union_with_class):
        assert_type(union_with_class, _Class)
    if isinstance(union_with_class, NotImplementedType):
        assert_type(union_with_class, NotImplementedType)
    if not isinstance(union_with_class, NotImplementedType):
        assert_type(union_with_class, _Class)
