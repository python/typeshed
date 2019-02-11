# https://github.com/ijl/orjson/blob/master/orjson.pyi

from typing import Any, Callable, Optional, Union

def dumps(
    obj: Any, default: Optional[Callable[[Any], Any]], option: Optional[int]
) -> bytes: ...
def loads(obj: Union[bytes, str]) -> Any: ...

class JSONDecodeError(ValueError): ...
class JSONEncodeError(TypeError): ...

OPT_STRICT_INTEGER: int
OPT_NAIVE_UTC: int
