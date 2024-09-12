from collections.abc import Iterator
from typing_extensions import deprecated

from configobj import ConfigObj

@deprecated("configobj_walker has moved to ruamel.yaml.util")
def configobj_walker(cfg: ConfigObj, /) -> Iterator[str]: ...
