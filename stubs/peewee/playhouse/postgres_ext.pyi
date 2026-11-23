from typing import Any
from typing_extensions import TypeVar

from peewee import Expression, Field

_T = TypeVar("_T", default=Any)

class ArrayField(Field[list[_T]]):
    dimensions: int
    def __init__(
        self,
        field_class: type[Field[_T]] = ...,
        field_kwargs: dict[str, Any] | None = ...,
        dimensions: int = 1,
        convert_values: bool = False,
        *args: Any,  # Passed to Field.__init__
        **kwargs: Any,  # Passed to Field.__init__
    ) -> None: ...
    def contains(self, *items: _T) -> Expression: ...
    def contains_any(self, *items: _T) -> Expression: ...
    def contained_by(self, *items: _T) -> Expression: ...
