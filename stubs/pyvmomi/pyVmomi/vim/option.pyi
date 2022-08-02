from typing import Any
from _typeshed import Incomplete

def __getattr__(name: str) -> Incomplete: ...

class OptionManager:
    def QueryOptions(self, name: str) -> list[OptionValue]: ...

class OptionValue:
    value: Any
    key: str
