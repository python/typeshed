from logging import Logger
from abc import ABCMeta

logger: Logger

class VaultApiBase(metaclass=ABCMeta):
    def __init__(self, adapter) -> None: ...
