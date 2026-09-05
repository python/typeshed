from collections.abc import Iterator
from typing_extensions import deprecated

from configobj import (  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]  # ty:ignore[unresolved-import]  # pyrefly: ignore [missing-import]
    ConfigObj as _ConfigObj,
)

@deprecated("configobj_walker has moved to ruamel.yaml.util")
def configobj_walker(cfg: _ConfigObj, /) -> Iterator[str]: ...
