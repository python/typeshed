# Stubs for sqlalchemy.sql.naming (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .schema import Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, PrimaryKeyConstraint as PrimaryKeyConstraint, UniqueConstraint as UniqueConstraint, CheckConstraint as CheckConstraint, Index as Index, Table as Table, Column as Column
from .elements import _truncated_label as _truncated_label, _defer_name as _defer_name, _defer_none_name as _defer_none_name, conv as conv

class ConventionDict:
    const = ...  # type: Any
    table = ...  # type: Any
    convention = ...  # type: Any
    def __init__(self, const, table, convention) -> None: ...
    def __getitem__(self, key): ...
