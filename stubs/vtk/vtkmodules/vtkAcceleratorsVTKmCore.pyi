from typing import Callable, TypeVar, Union

Callback = Union[Callable[..., None], None]
_Buffer = TypeVar("_Buffer")
_Pointer = TypeVar("_Pointer")
Template = TypeVar("Template")
