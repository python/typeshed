from _typeshed import AnyPath
from typing import Any

from .exceptions import TrashPermissionError as TrashPermissionError

# The list should be list[AnyPath] but that doesn't work because invariance
def send2trash(paths: list[Any] | AnyPath) -> None: ...

# Marked as incomplete because there are platform-specific plat_foo modules
def __getattr__(name: str) -> Any: ...  # incomplete
