from collections.abc import Callable
from typing import Any

from peewee import Expression, TextField

class JSONField(TextField[str]):
    def __init__(
        self,
        json_dumps: Callable[[Any], str] | None = ...,  # Takes any JSON-serializable value
        json_loads: Callable[[str], Any] | None = ...,  # Returns any decoded JSON value
        **kwargs: Any,  # Passed to TextField.__init__
    ) -> None: ...
    def db_value(self, value: Any) -> str | None: ...  # Takes any JSON-serializable value, or a Node
    def python_value(self, value: str | None) -> Any: ...  # Returns any decoded JSON value
    def children(self) -> Expression: ...
    def length(self, path: str | None = None) -> Expression: ...
    def json_type(self) -> Expression: ...
