import gettext
from typing import Any

class Format:
    locale: Any
    tzinfo: Any
    def __init__(self, locale, tzinfo: Any | None = ...) -> None: ...
    def date(self, date: Any | None = ..., format: str = ...): ...
    def datetime(self, datetime: Any | None = ..., format: str = ...): ...
    def time(self, time: Any | None = ..., format: str = ...): ...
    def timedelta(self, delta, granularity: str = ..., threshold: float = ..., format: str = ..., add_direction: bool = ...): ...
    def number(self, number): ...
    def decimal(self, number, format: Any | None = ...): ...
    def currency(self, number, currency): ...
    def percent(self, number, format: Any | None = ...): ...
    def scientific(self, number): ...

class LazyProxy:
    def __init__(self, func, *args, **kwargs) -> None: ...
    @property
    def value(self): ...
    def __contains__(self, key): ...
    def __nonzero__(self): ...
    def __dir__(self): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __unicode__(self): ...
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
    def __delattr__(self, name) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
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
    def __init__(self, fp: Any | None = ...): ...
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

class Translations(NullTranslations, gettext.GNUTranslations):  # argument disparities between base classes
    DEFAULT_DOMAIN: str
    domain: Any
    def __init__(self, fp: Any | None = ..., domain: Any | None = ...) -> None: ...
    ugettext: Any
    ungettext: Any
    @classmethod
    def load(cls, dirname: Any | None = ..., locales: Any | None = ..., domain: Any | None = ...): ...
    def add(self, translations, merge: bool = ...): ...
    def merge(self, translations): ...
