from _typeshed import AnyPath
from typing import Any

from .exceptions import TrashPermissionError as TrashPermissionError

# The list should be list[AnyPath] but that doesn't work because invariance
def send2trash(paths: list[Any] | AnyPath) -> None: ...
