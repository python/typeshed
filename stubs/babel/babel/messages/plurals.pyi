from collections.abc import Mapping

LC_CTYPE: str
PLURALS: Mapping[str, tuple[int, str]]
DEFAULT_PLURAL: tuple[int, str]

class _PluralTuple(tuple[int, str]):
    @property
    def num_plurals(self) -> int: ...
    @property
    def plural_expr(self) -> str: ...
    @property
    def plural_forms(self) -> str: ...

def get_plural(locale: str = ...) -> _PluralTuple: ...
