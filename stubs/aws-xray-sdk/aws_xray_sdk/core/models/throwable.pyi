from _typeshed import Incomplete
from logging import Logger

log: Logger

class Throwable:
    id: Incomplete
    message: Incomplete
    type: Incomplete
    remote: Incomplete
    stack: Incomplete
    def __init__(self, exception: Exception, stack, remote: bool = False) -> None: ...
    def to_dict(self) -> dict: ...
