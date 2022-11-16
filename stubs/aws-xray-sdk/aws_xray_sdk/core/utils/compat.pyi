from typing import Any
from typing_extensions import Literal

PY2: Literal[False]
PY35: Literal[False]
annotation_value_types: Any
string_types = str

def is_classmethod(func): ...
def is_instance_method(parent_class, func_name, func): ...
