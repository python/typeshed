from collections.abc import Callable
from typing import Any

from peewee import Expression, TextField

class JSONField(TextField[str]):
    def __init__(
        self,
        json_dumps: Callable[[object], str] | None = ...,
        json_loads: Callable[[str], object] | None = ...,
        **kwargs: Any,  # Passed to TextField.__init__
    ) -> None: ...
    def db_value(self, value: object) -> str | None: ...
    def python_value(self, value: str | None) -> Any: ...  # Decoded JSON: any JSON-compatible value
    def children(self) -> Expression: ...
    def length(self, path: str | None = None) -> Expression: ...
    def json_type(self) -> Expression: ...
