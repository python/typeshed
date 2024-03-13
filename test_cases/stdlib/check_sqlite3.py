from __future__ import annotations

import sqlite3
from contextlib import closing
from typing_extensions import assert_type

# https://github.com/python/typeshed/issues/11558


class MyConnection(sqlite3.Connection):
    pass


# Default return-type is Connection.
with closing(sqlite3.connect(":memory:")) as con1:
    assert_type(con1, sqlite3.Connection)

# Providing an alternate factory changes the return-type.
with closing(sqlite3.connect(":memory:", factory=MyConnection)) as con2:
    assert_type(con2, MyConnection)

# Provides a true positive error. When checking the connect() function,
# mypy should report an arg-type error for the factory argument.
with sqlite3.connect(":memory:", factory=None) as con3:  # type: ignore
    pass

# While factory is not optional in the connect() function, it *is* optional
# for the Connection class itself.
with closing(sqlite3.Connection(":memory:", factory=None)) as con4:
    assert_type(con4, sqlite3.Connection)

# Ideally, this should pass but I'm not sure where to make this change.
# with closing(sqlite3.Connection(":memory:", factory=MyConnection)) as con5:
#    assert_type(con5, MyConnection)
