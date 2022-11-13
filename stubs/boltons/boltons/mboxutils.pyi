# TODO: DONE!

import mailbox
from typing import NoReturn

DEFAULT_MAXMEM: int

class mbox_readonlydir(mailbox.mbox):
    maxmem: int
    def __init__(self, path: str, factory: type | None = ..., create: bool = ..., maxmem: int = ...) -> NoReturn: ...
    def flush(self) -> NoReturn: ...
