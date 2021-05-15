import sys
from typing import Any, Dict, Optional, Union

_Text = str

class Completer:
    def __init__(self, namespace: Optional[Dict[str, Any]] = ...) -> None: ...
    def complete(self, text: _Text, state: int) -> Optional[str]: ...
