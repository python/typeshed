# Stubs for rlcompleter

from typing import Optional

class Completer:
    def complete(self, text: str, state: int) -> Optional[str]: ...
