from typing import Any, Optional

class Plugin:
    capability = ...  # type: Any
    @classmethod
    def is_capable(cls, requested_capability): ...

def get_plugin(cls, requested_capability: Optional[Any] = ...): ...
def load_plugins(config): ...
