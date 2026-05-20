from _typeshed import Incomplete
from enum import IntEnum

class ConfigResourceType(IntEnum):
    BROKER = 4
    TOPIC = 2

class ConfigResource:
    resource_type: Incomplete
    name: Incomplete
    configs: Incomplete
    def __init__(self, resource_type, name, configs=None) -> None: ...
