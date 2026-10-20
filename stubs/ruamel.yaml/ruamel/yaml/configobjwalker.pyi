from collections.abc import Iterator
from typing_extensions import deprecated

from configobj import ConfigObj as _ConfigObj  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]  # ty:ignore[unresolved-import]  # pyrefly: ignore [missing-import]

@deprecated("configobj_walker has moved to ruamel.yaml.util")
def configobj_walker(cfg: _ConfigObj) -> Iterator[str]: ...
