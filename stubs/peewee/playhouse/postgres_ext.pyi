from typing import Any

from peewee import Expression, Field

class ArrayField(Field[list[Any]]):
    dimensions: int
    def __init__(
        self,
        field_class: type[Field[Any]] = ...,
        field_kwargs: dict[str, Any] | None = ...,
        dimensions: int = 1,
        convert_values: bool = False,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def contains(self, *items: Any) -> Expression: ...
    def contains_any(self, *items: Any) -> Expression: ...
    def contained_by(self, *items: Any) -> Expression: ...
