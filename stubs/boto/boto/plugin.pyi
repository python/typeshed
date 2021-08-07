from typing import Any, Optional

class Plugin:
    capability: Any
    @classmethod
    def is_capable(cls, requested_capability): ...

def get_plugin(cls, requested_capability: Any | None = ...): ...
def load_plugins(config): ...
