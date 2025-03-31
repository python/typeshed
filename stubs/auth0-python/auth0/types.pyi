from typing import Any
from typing_extensions import TypeAlias

TimeoutType: TypeAlias = float | tuple[float, float]
RequestData: TypeAlias = dict[str, Any] | list[Any]
