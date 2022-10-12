import mailbox
from _typeshed import Incomplete

DEFAULT_MAXMEM: Incomplete

class mbox_readonlydir(mailbox.mbox):
    maxmem: Incomplete
    def __init__(self, path, factory: Incomplete | None = ..., create: bool = ..., maxmem=...) -> None: ...
    def flush(self) -> None: ...
