from typing import ClassVar, Final, Protocol, type_check_only

from docutils.languages import LanguageImporter

__docformat__: Final = "reStructuredText"

@type_check_only
class RSTLanguageModule(Protocol):
    __name__: str
    directives: dict[str, str]
    roles: dict[str, str]

# There is no fallback, so `None` is returned for unknown languages.
class RstLanguageImporter(LanguageImporter[RSTLanguageModule, RSTLanguageModule | None]):
    fallback: ClassVar[None]

get_language: RstLanguageImporter
