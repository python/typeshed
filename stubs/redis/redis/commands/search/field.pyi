from typing import Any

class Field:
    NUMERIC: str
    TEXT: str
    WEIGHT: str
    GEO: str
    TAG: str
    SORTABLE: str
    NOINDEX: str
    AS: str
    name: Any
    args: Any
    args_suffix: Any
    as_name: Any
    def __init__(self, name, args=..., sortable: bool = ..., no_index: bool = ..., as_name: Any | None = ...) -> None: ...
    def append_arg(self, value) -> None: ...
    def redis_args(self): ...

class TextField(Field):
    NOSTEM: str
    PHONETIC: str
    def __init__(self, name, weight: float = ..., no_stem: bool = ..., phonetic_matcher: Any | None = ..., **kwargs) -> None: ...

class NumericField(Field):
    def __init__(self, name, **kwargs) -> None: ...

class GeoField(Field):
    def __init__(self, name, **kwargs) -> None: ...

class TagField(Field):
    SEPARATOR: str
    def __init__(self, name, separator: str = ..., **kwargs) -> None: ...
