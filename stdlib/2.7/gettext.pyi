# TODO(MichalPokorny): better types

from typing import Any, IO, List, Optional, Union

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

class Translations(object):
    def _parse(self, fp: IO[str]) -> None: ...
    def add_fallback(self, fallback: Any) -> None: ...
    def gettext(self, message: str) -> str: ...
    def lgettext(self, message: str) -> str: ...
    def ugettext(self, message: str) -> unicode: ...
    def ngettext(self, singular: str, plural: str, n: int) -> str: ...
    def lngettext(self, singular: str, plural: str, n: int) -> str: ...
    def ungettext(self, singular: str, plural: str, n: int) -> str: ...
    def info(self) -> Any: ...
    def charset(self) -> Any: ...
    def output_charset(self) -> Any: ...
    def set_output_charset(self, charset: Any) -> None: ...
    def install(self, unicode: bool = ..., names: Any = ...) -> None: ...

class NullTranslations(Translations): ...
class GNUTranslations(Translations): ...

def find(domain: str, localedir: str = ..., languages: List[str] = ...,
         all: Any = ...) -> Optional[Union[str, List[str]]]: ...

def translation(domain: str, localedir: str = ..., languages: List[str] = ...,
                class_: Any = ..., fallback: Any = ..., codeset: Any = ...) -> Translations: ...
def install(domain: str, localedir: str = ..., unicode: Any = ..., codeset: Any = ...,
            names: Any = ...) -> None: ...
