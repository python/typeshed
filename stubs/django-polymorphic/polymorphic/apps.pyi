from _typeshed import Unused
from collections.abc import Sequence
from typing import Final

from django.apps import AppConfig
from django.core.checks import CheckMessage

def check_reserved_field_names(app_configs: Sequence[AppConfig] | None, **kwargs: Unused) -> list[CheckMessage]: ...

class PolymorphicConfig(AppConfig):
    name: Final = "polymorphic"
    verbose_name: str = "Django Polymorphic"
