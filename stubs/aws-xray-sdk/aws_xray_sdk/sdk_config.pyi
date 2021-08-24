from typing import Any

log: Any

class SDKConfig:
    XRAY_ENABLED_KEY: str
    DISABLED_ENTITY_NAME: str
    @classmethod
    def sdk_enabled(cls): ...
    @classmethod
    def set_sdk_enabled(cls, value) -> None: ...
