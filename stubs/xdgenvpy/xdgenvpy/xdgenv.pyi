class XDG:
    def __init__(self) -> None: ...
    @property
    def XDG_DATA_HOME(self) -> str: ...
    @property
    def XDG_CONFIG_HOME(self) -> str: ...
    @property
    def XDG_CACHE_HOME(self) -> str: ...
    @property
    def XDG_RUNTIME_DIR(self) -> str: ...
    @property
    def XDG_DATA_DIRS(self) -> tuple[str, ...]: ...
    @property
    def XDG_CONFIG_DIRS(self) -> tuple[str, ...]: ...

class XDGPackage(XDG):
    def __init__(self, package_name: str) -> None: ...
    @property
    def XDG_DATA_HOME(self) -> str: ...
    @property
    def XDG_CONFIG_HOME(self) -> str: ...
    @property
    def XDG_CACHE_HOME(self) -> str: ...
    @property
    def XDG_RUNTIME_DIR(self) -> str: ...

class XDGPedanticPackage(XDGPackage):
    @property
    def XDG_DATA_HOME(self) -> str: ...
    @property
    def XDG_CONFIG_HOME(self) -> str: ...
    @property
    def XDG_CACHE_HOME(self) -> str: ...
    @property
    def XDG_RUNTIME_DIR(self) -> str: ...
