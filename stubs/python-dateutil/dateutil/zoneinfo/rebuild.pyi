from _typeshed import StrOrBytesPath
from collections.abc import Iterable
from typing import Any

def rebuild(
    filename: StrOrBytesPath, tag=None, format: str = "gz", zonegroups: Iterable[str] = [], metadata: dict[str, Any] | None = None
) -> None: ...
