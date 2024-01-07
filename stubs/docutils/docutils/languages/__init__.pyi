from typing import ClassVar, Protocol

from docutils.utils import Reporter, normalize_language_tag

__all__ = ["get_language", "normalize_language_tag", "LanguageImporter"]

class _LanguageModule(Protocol):
    labels: dict[str, str]
    author_separators: list[str]
    bibliographic_fields: list[str]

class LanguageImporter:
    packages: ClassVar[tuple[str, ...]]
    warn_msg: ClassVar[str]
    fallback: ClassVar[str]

    cache: dict[str, _LanguageModule]

    def __call__(self, language_code: str, reporter: Reporter | None = None) -> _LanguageModule: ...
    def import_from_packages(self, name: str, reporter: Reporter | None = None) -> _LanguageModule: ...
    def check_content(self, module: _LanguageModule) -> None: ...

get_language: LanguageImporter
