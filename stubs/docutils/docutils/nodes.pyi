from typing import Any

from docutils.transforms import Transformer

class Node:
    parent: Node | None
    source: str | None
    line: int | None
    document: document | None
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

class Element(Node):
    def __init__(self, rawsource: str = ..., *children: Node, **attributes): ...
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

class Structural: ...
class Root: ...

class document(Root, Structural, Element):
    transformer: Transformer
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

def __getattr__(name: str) -> Any: ...  # incomplete
