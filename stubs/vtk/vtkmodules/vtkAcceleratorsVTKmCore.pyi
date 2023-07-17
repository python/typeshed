from typing import Callable, TypeVar, Union

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
_Pointer = TypeVar("_Pointer")
Template = TypeVar("Template")
