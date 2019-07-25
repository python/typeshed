# Stubs for gettext (Python 3.4)

from typing import overload, Any, IO, Optional, Sequence, Type, TypeVar

class NullTranslations:
    def __init__(self, fp: IO[str] = ...) -> None: ...
    def _parse(self, fp: IO[str]) -> None: ...
    def add_fallback(self, fallback: NullTranslations) -> None: ...
    def gettext(self, message: str) -> str: ...
    def lgettext(self, message: str) -> str: ...
    def ngettext(self, singular: str, plural: str, n: int) -> str: ...
    def lngettext(self, singular: str, plural: str, n: int) -> str: ...
    def info(self) -> Any: ...
    def charset(self) -> Any: ...
    def output_charset(self) -> Any: ...
    def set_output_charset(self, charset: str) -> None: ...
    def install(self, names: Optional[Container[str]] = ...) -> None: ...

class GNUTranslations(NullTranslations):
    LE_MAGIC: int
    BE_MAGIC: int

def find(domain: str, localedir: Optional[str] = ..., languages: Optional[Sequence[str]] = ...,
         all: bool = ...) -> Any: ...

_T = TypeVar('_T')
@overload
def translation(domain: str, localedir: Optional[str] = ..., languages: Optional[Sequence[str]] = ...,
                *, fallback: bool = ..., codeset: Optional[str] = ...) -> NullTranslations: ...
@overload
def translation(domain: str, localedir: Optional[str] = ..., languages: Optional[Sequence[str]] = ...,
                class_: Type[_T] = ..., fallback: bool = ..., codeset: Optional[str] = ...) -> _T: ...

def install(domain: str, localedir: Optional[str] = ..., codeset: Optional[str] = ...,
            names: Optional[Sequence[str]] = ...) -> None: ...

def textdomain(domain: Optional[str] = ...) -> str: ...
def bindtextdomain(domain: str, localedir: Optional[str] = ...) -> str: ...
def bind_textdomain_codeset(domain: str, codeset: Optional[str] = ...) -> str: ...
def dgettext(domain: str, message: str) -> str: ...
def ldgettext(domain: str, message: str) -> str: ...
def dngettext(domain: str, singular: str, plural: str, n: int) -> str: ...
def ldngettext(domain: str, singular: str, plural: str, n: int) -> str: ...
def gettext(message: str) -> str: ...
def lgettext(message: str) -> str: ...
def ngettext(singular: str, plural: str, n: int) -> str: ...
def lngettext(singular: str, plural: str, n: int) -> str: ...

Catalog = translation
