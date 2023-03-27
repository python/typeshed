import gettext
from _typeshed import Incomplete
from datetime import date as _date, datetime as _datetime, time as _time, timedelta as _timedelta
from decimal import Decimal
from typing import Any
from typing_extensions import Literal

from babel.core import Locale
from pytz import BaseTzInfo

from .dates import _PredefinedTimeFormat

class Format:
    locale: Locale
    tzinfo: BaseTzInfo | None
    def __init__(self, locale: Locale | str, tzinfo: BaseTzInfo | None = None) -> None: ...
    def date(self, date: _date | None = None, format: _PredefinedTimeFormat | str = 'medium') -> str: ...
    def datetime(self, datetime: _date | None = None, format: _PredefinedTimeFormat | str = 'medium') -> str: ...
    def time(self, time: _time | _datetime | None = None, format: _PredefinedTimeFormat | str = 'medium') -> str: ...
    def timedelta(
        self,
        delta: _timedelta | int,
        granularity: Literal["year", "month", "week", "day", "hour", "minute", "second"] = 'second',
        threshold: float = 0.85,
        format: _PredefinedTimeFormat = 'long',
        add_direction: bool = False,
    ) -> str: ...
    def number(self, number: float | Decimal | str) -> str: ...
    def decimal(self, number: float | Decimal | str, format: str | None = None) -> str: ...
    def currency(self, number: float | Decimal | str, currency: str) -> str: ...
    def percent(self, number: float | Decimal | str, format: str | None = None) -> str: ...
    def scientific(self, number: float | Decimal | str) -> str: ...

class LazyProxy:
    def __init__(self, func, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    def __contains__(self, key): ...
    def __bool__(self) -> bool: ...
    def __dir__(self): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __call__(self, *args, **kwargs): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __delattr__(self, name: str) -> None: ...
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __copy__(self) -> LazyProxy: ...
    def __deepcopy__(self, memo: Any) -> LazyProxy: ...

class NullTranslations(gettext.NullTranslations):
    DEFAULT_DOMAIN: Any
    plural: Any
    files: Any
    domain: Any
    def __init__(self, fp: Incomplete | None = None): ...
    def dgettext(self, domain, message): ...
    def ldgettext(self, domain, message): ...
    def udgettext(self, domain, message): ...
    dugettext: Any
    def dngettext(self, domain, singular, plural, num): ...
    def ldngettext(self, domain, singular, plural, num): ...
    def udngettext(self, domain, singular, plural, num): ...
    dungettext: Any
    CONTEXT_ENCODING: str
    def pgettext(self, context, message): ...
    def lpgettext(self, context, message): ...
    def npgettext(self, context, singular, plural, num): ...
    def lnpgettext(self, context, singular, plural, num): ...
    def upgettext(self, context, message): ...
    def unpgettext(self, context, singular, plural, num): ...
    def dpgettext(self, domain, context, message): ...
    def udpgettext(self, domain, context, message): ...
    dupgettext: Any
    def ldpgettext(self, domain, context, message): ...
    def dnpgettext(self, domain, context, singular, plural, num): ...
    def udnpgettext(self, domain, context, singular, plural, num): ...
    dunpgettext: Any
    def ldnpgettext(self, domain, context, singular, plural, num): ...
    ugettext: Any
    ungettext: Any

class Translations(NullTranslations, gettext.GNUTranslations):
    DEFAULT_DOMAIN: str
    domain: Any
    def __init__(self, fp: Incomplete | None = None, domain: Incomplete | None = None) -> None: ...
    ugettext: Any
    ungettext: Any
    @classmethod
    def load(cls, dirname: Incomplete | None = None, locales: Incomplete | None = None, domain: Incomplete | None = None): ...
    def add(self, translations, merge: bool = True): ...
    def merge(self, translations): ...
