from typing import Any, NamedTuple

LC_CTYPE: Any
PLURALS: Any
DEFAULT_PLURAL: Any

class _PluralTuple(NamedTuple):
    num_plurals: int
    plural_expr: str
    @property
    def plural_forms(self) -> str: ...

def get_plural(locale=...): ...
