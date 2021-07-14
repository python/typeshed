from typing import Any, Optional

from ..data import language_locale_dict as language_locale_dict, language_order as language_order
from .locale import Locale as Locale

LOCALE_SPLIT_PATTERN: Any

class LocaleDataLoader:
    def get_locale_map(
        self,
        languages: Optional[Any] = ...,
        locales: Optional[Any] = ...,
        region: Optional[Any] = ...,
        use_given_order: bool = ...,
        allow_conflicting_locales: bool = ...,
    ): ...
    def get_locales(
        self,
        languages: Optional[Any] = ...,
        locales: Optional[Any] = ...,
        region: Optional[Any] = ...,
        use_given_order: bool = ...,
        allow_conflicting_locales: bool = ...,
    ) -> None: ...
    def get_locale(self, shortname: Any): ...

default_loader: Any
