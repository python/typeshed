from collections.abc import Sequence
from typing import Any

from django.apps import AppConfig
from django.core.checks import CheckMessage

def check_reserved_field_names(app_configs: Sequence[AppConfig] | None, **kwargs: Any) -> list[CheckMessage]: ...

class PolymorphicConfig(AppConfig):
    name: str
    verbose_name: str
