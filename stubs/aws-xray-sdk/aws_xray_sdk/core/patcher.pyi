from collections.abc import Iterable
from logging import Logger

log: Logger
SUPPORTED_MODULES: tuple
NO_DOUBLE_PATCH: tuple
_PATCHED_MODULES: set

def patch_all(double_patch: bool = False) -> None: ...
def patch(modules_to_patch: Iterable[str], raise_errors: bool = True, ignore_module_patterns: str | None = None) -> None: ...
