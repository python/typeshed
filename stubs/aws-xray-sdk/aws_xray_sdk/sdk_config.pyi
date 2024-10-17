from logging import Logger

log: Logger

class SDKConfig:
    XRAY_ENABLED_KEY: str
    DISABLED_ENTITY_NAME: str
    __SDK_ENABLED: bool | None

    @classmethod
    def __get_enabled_from_env(cls) -> bool: ...
    @classmethod
    def sdk_enabled(cls): ...
    @classmethod
    def set_sdk_enabled(cls, value: bool) -> None: ...
