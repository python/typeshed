from typing import Any

from .utils import deprecate as deprecate

DEFAULTS: Any
DEPRECATED_SETTINGS: Any

def is_callable(value: Any): ...

class Settings:
    def __getattr__(self, name: Any): ...
    def get_setting(self, setting: Any): ...
    def change_setting(
        self, setting: Any, value: Any, enter: Any, **kwargs: Any
    ) -> None: ...

settings: Any
