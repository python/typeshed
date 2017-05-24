from typing import Any

poll = ...  # type: Any
select = ...  # type: Any

def is_connection_dropped(conn): ...
def create_connection(address, timeout=..., source_address=..., socket_options=...): ...
