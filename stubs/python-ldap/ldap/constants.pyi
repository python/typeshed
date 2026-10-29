from typing import Any

class Constant:
    name: Any
    requirements: Any
    doc: Any
    def __init__(self, name: str, optional: bool = False, requirements: Any = ..., doc: Any = ...) -> None: ...

class Error(Constant):
    c_template: str

class Int(Constant):
    c_template: str

class TLSInt(Int):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Feature(Constant):
    c_template: Any
    c_feature: Any
    def __init__(self, name: str, c_feature: Any, **kwargs: Any) -> None: ...

class Str(Constant):
    c_template: str

API_2004: str
CONSTANTS: Any

def print_header() -> None: ...
