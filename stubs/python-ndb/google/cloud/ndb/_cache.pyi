from typing import Any, Dict

class ContextCache(Dict[Any, Any]):
    def get_and_validate(self, key: Any): ...
