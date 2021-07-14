from .parser import date_order_chart as date_order_chart
from .utils import registry as registry
from typing import Any, Optional

class Settings:
    def __init__(self, settings: Optional[Any] = ...) -> None: ...
    @classmethod
    def get_key(cls, settings: Optional[Any] = ...): ...
    def replace(self, mod_settings: Optional[Any] = ..., **kwds: Any): ...

settings: Any

def apply_settings(f: Any): ...

class SettingValidationError(ValueError): ...

def check_settings(settings: Any) -> None: ...
