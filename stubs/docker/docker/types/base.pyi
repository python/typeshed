from collections.abc import Mapping
from typing import Any

class DictType(dict[str, Any]):
    def __init__(self, init: Mapping[str, Any]) -> None: ...
