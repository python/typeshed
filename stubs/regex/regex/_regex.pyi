from typing import Any

class Pattern:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Match:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Scanner:
    def __getattr__(self, name: str) -> Any: ...  # incomplete

class Splitter:
    def __getattr__(self, name: str) -> Any: ...  # incomplete
