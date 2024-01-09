from typing import Any

from django.core.exceptions import FieldError

class FieldLookupError(FieldError):
    def __init__(self, model_field: Any, lookup_expr: Any) -> None: ...
