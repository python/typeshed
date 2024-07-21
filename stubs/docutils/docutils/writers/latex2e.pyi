from _typeshed import Incomplete
from collections.abc import Mapping
from typing import ClassVar

from docutils.utils import Reporter

class Babel:
    language_codes: ClassVar[Mapping[str, str]]
    warn_msg: ClassVar[str]
    active_chars: ClassVar[Mapping[str, str]]

    reporter: Reporter | None
    language: str
    otherlanguages: Mapping[str, str]

    def __init__(self, language_code: str, reporter: Reporter | None = None) -> None: ...
    def __call__(self) -> str: ...
    def language_name(self, language_code: str) -> str: ...
    def get_language(self) -> str: ...

def __getattr__(name: str) -> Incomplete: ...
