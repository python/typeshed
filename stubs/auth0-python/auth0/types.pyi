from typing import Any, TypeAlias

TimeoutType: TypeAlias = float | tuple[float, float]
RequestData: TypeAlias = dict[str, Any] | list[Any]
