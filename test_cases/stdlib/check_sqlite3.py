from __future__ import annotations

import sqlite3


# https://github.com/python/typeshed/issues/11558

class MyConnection(sqlite3.Connection):
    pass

# Default return-type is Connection.
con1: sqlite3.Connection = sqlite3.connect(":memory:")
con1.close()

# Providing an alternate factory changes the return-type.
con2: MyConnection = sqlite3.connect(":memory:", factory=MyConnection)
con2.close()

# Provides a true positive error. When checking the connect() function,
# mypy should report an arg-type error for the factory argument.
try:
    con3: MyConnection = sqlite3.connect(":memory:", factory=None)  # type: ignore
    con3.close()
except TypeError:
    pass  # Expected behavior.
else:
    raise RuntimeError("Expected TypeError, factory is not optional.")

# While factory is not optional in the connect() function, it *is* optional
# for the Connection class itself.
con4: sqlite3.Connection = sqlite3.Connection(":memory:", factory=None)
con4.close()

# Ideally, this should pass but I'm not sure where to make this change.
#con5: MyConnection = sqlite3.Connection(":memory:", factory=MyConnection)
#con5.close()
