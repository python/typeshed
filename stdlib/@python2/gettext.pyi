from typing import IO, Any, Container, Dict, List, Sequence, Type

def bindtextdomain(domain: str, localedir: str = ...) -> str: ...
def bind_textdomain_codeset(domain: str, codeset: str = ...) -> str: ...
def textdomain(domain: str = ...) -> str: ...
def gettext(message: str) -> str: ...
def lgettext(message: str) -> str: ...
def dgettext(domain: str, message: str) -> str: ...
def ldgettext(domain: str, message: str) -> str: ...
def ngettext(singular: str, plural: str, n: int) -> str: ...
def lngettext(singular: str, plural: str, n: int) -> str: ...
def dngettext(domain: str, singular: str, plural: str, n: int) -> str: ...
def ldngettext(domain: str, singular: str, plural: str, n: int) -> str: ...

class NullTranslations(object):
    def __init__(self, fp: IO[str] = ...) -> None: ...
    def _parse(self, fp: IO[str]) -> None: ...
    def add_fallback(self, fallback: NullTranslations) -> None: ...
    def gettext(self, message: str) -> str: ...
    def lgettext(self, message: str) -> str: ...
    def ugettext(self, message: str | unicode) -> unicode: ...
    def ngettext(self, singular: str, plural: str, n: int) -> str: ...
    def lngettext(self, singular: str, plural: str, n: int) -> str: ...
    def ungettext(self, singular: str | unicode, plural: str | unicode, n: int) -> unicode: ...
    def info(self) -> Dict[str, str]: ...
    def charset(self) -> str | None: ...
    def output_charset(self) -> str | None: ...
    def set_output_charset(self, charset: str | None) -> None: ...
    def install(self, unicode: bool = ..., names: Container[str] = ...) -> None: ...

class GNUTranslations(NullTranslations):
    LE_MAGIC: int
    BE_MAGIC: int

def find(
    domain: str, localedir: str | None = ..., languages: Sequence[str] | None = ..., all: Any = ...
) -> str | List[str] | None: ...
def translation(
    domain: str,
    localedir: str | None = ...,
    languages: Sequence[str] | None = ...,
    class_: Type[NullTranslations] | None = ...,
    fallback: bool = ...,
    codeset: str | None = ...,
) -> NullTranslations: ...
def install(
    domain: str, localedir: str | None = ..., unicode: bool = ..., codeset: str | None = ..., names: Container[str] = ...
) -> None: ...
