from functools import singledispatch
from typing import Any

@singledispatch
def to_json(obj: Any) -> Any: ...
