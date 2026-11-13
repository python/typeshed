from typing import Any, TypeAlias

_H2Connection: TypeAlias = Any  # h2.connection.H2Connection

def server_connection_class() -> type[_H2Connection]: ...
