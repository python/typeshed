# Stubs for sqlalchemy.sql.crud (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from . import elements

REQUIRED = ...  # type: Any
ISINSERT = ...  # type: Any
ISUPDATE = ...  # type: Any
ISDELETE = ...  # type: Any

class _multiparam_column(elements.ColumnElement):
    key = ...  # type: Any
    original = ...  # type: Any
    default = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, original, index) -> None: ...
    def __eq__(self, other): ...
