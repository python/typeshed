from types import ModuleType
from typing import ClassVar, Final, Generic, Protocol, type_check_only
from typing_extensions import TypeVar

from docutils.utils import Reporter

__docformat__: Final = "reStructuredText"

@type_check_only
class LanguageModule(Protocol):
    __name__: str
    labels: dict[str, str]
    bibliographic_fields: dict[str, str]
    author_separators: list[str]

_ModuleT = TypeVar("_ModuleT", default=LanguageModule)
# The result of `__call__()`: the module type, or `_ModuleT | None` for importers without a fallback language.
_ResultT = TypeVar("_ResultT", default=_ModuleT)

# Not actually generic at runtime, but it does support subscription via `__class_getitem__`.
class LanguageImporter(Generic[_ModuleT, _ResultT]):
    packages: ClassVar[tuple[str, ...]]
    warn_msg: ClassVar[str]
    fallback: ClassVar[str | None]
    cache: dict[str, _ModuleT]
    def __init__(self) -> None: ...
    def import_from_packages(self, name: str, reporter: Reporter | None = None) -> _ModuleT | None: ...
    def check_content(self, module: _ModuleT | ModuleType) -> None: ...
    def __call__(self, language_code: str, reporter: Reporter | None = None) -> _ResultT: ...

get_language: LanguageImporter[LanguageModule]
