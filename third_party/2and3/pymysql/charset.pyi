# Stubs for pymysql.charset (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

MBLENGTH = ...  # type: Any

class Charset:
    is_default = ...  # type: Any
    def __init__(self, id, name, collation, is_default): ...

class Charsets:
    def __init__(self): ...
    def add(self, c): ...
    def by_id(self, id): ...
    def by_name(self, name): ...

def charset_by_name(name): ...
def charset_by_id(id): ...