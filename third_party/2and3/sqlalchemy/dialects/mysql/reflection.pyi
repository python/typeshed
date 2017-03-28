# Stubs for sqlalchemy.dialects.mysql.reflection (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ... import types as sqltypes
from .enumerated import _EnumeratedValues as _EnumeratedValues, SET as SET
from .types import DATETIME as DATETIME, TIME as TIME, TIMESTAMP as TIMESTAMP

class ReflectedState(object):
    columns = ...  # type: Any
    table_options = ...  # type: Any
    table_name = ...  # type: Any
    keys = ...  # type: Any
    constraints = ...  # type: Any
    def __init__(self) -> None: ...

class MySQLTableDefinitionParser(object):
    dialect = ...  # type: Any
    preparer = ...  # type: Any
    def __init__(self, dialect, preparer) -> None: ...
    def parse(self, show_create, charset): ...
