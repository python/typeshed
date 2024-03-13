from _typeshed import Incomplete
from abc import ABCMeta

logger: Incomplete

class VaultApiBase(metaclass=ABCMeta):
    def __init__(self, adapter) -> None: ...
