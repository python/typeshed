from typing import ClassVar, Final, Protocol

from docutils.languages import LanguageImporter

__docformat__: Final = "reStructuredText"

class _RstLanguageModule(Protocol):
    directives: dict[str, str]
    roles: dict[str, str]

class RstLanguageImporter(LanguageImporter):
    fallback: ClassVar[None]  # type: ignore[override]
    def check_content(self, module: _RstLanguageModule) -> None: ...  # type: ignore[override]

get_language: RstLanguageImporter
