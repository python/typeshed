from _typeshed import Self
from typing import Any

from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement
from ...util import memoized_property

class Insert(StandardInsert):
    stringify_dialect: str
    inherit_cache: bool
    @property
    def inserted(self): ...
    @memoized_property
    def inserted_alias(self): ...
    def on_duplicate_key_update(self: Self, *args, **kw) -> Self: ...

insert: Any

class OnDuplicateClause(ClauseElement):
    __visit_name__: str
    stringify_dialect: str
    inserted_alias: Any
    update: Any
    def __init__(self, inserted_alias, update) -> None: ...
