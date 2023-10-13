from typing import Any
from typing_extensions import Literal

annotation_value_types: Any

def is_classmethod(func): ...
def is_instance_method(parent_class, func_name, func): ...
