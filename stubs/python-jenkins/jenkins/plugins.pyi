from typing import Any

class Plugin(dict[str, Any]):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...

class PluginVersion(str):
    def __init__(self, version: str) -> None: ...
    def __le__(self, version: str | PluginVersion) -> bool: ...
    def __lt__(self, version: str | PluginVersion) -> bool: ...
    def __ge__(self, version: str | PluginVersion) -> bool: ...
    def __gt__(self, version: str | PluginVersion) -> bool: ...
    def __eq__(self, version: str | PluginVersion) -> bool: ...
    def __ne__(self, version: str | PluginVersion) -> bool: ...
