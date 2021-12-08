from typing import Any

class ResultRow:
    column_names: tuple[str, ...]
    column_values: tuple[Any, ...]
