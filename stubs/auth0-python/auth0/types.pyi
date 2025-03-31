from typing_extensions import TypeAlias
from typing import Any

TimeoutType: TypeAlias = float | tuple[float, float]
RequestData: TypeAlias = dict[str, Any] | list[Any]
