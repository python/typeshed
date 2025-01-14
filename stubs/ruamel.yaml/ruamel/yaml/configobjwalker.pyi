from collections.abc import Iterator
from typing_extensions import deprecated

from configobj import ConfigObj  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

@deprecated("configobj_walker has moved to ruamel.yaml.util")
def configobj_walker(cfg: ConfigObj, /) -> Iterator[str]: ...
