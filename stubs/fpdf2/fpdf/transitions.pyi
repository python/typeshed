from abc import ABC, abstractmethod
from typing import Literal

class Transition(ABC):
    @abstractmethod
    def serialize(self) -> str: ...

class SplitTransition(Transition):
    dimension: Literal["H", "V"]
    direction: Literal["I", "O"]
    def __init__(self, dimension: Literal["H", "V"], direction: Literal["I", "O"]) -> None: ...
    def serialize(self) -> str: ...

class BlindsTransition(Transition):
    dimension: Literal["H", "V"]
    def __init__(self, dimension: Literal["H", "V"]) -> None: ...
    def serialize(self) -> str: ...

class BoxTransition(Transition):
    direction: Literal["I", "O"]
    def __init__(self, direction: Literal["I", "O"]) -> None: ...
    def serialize(self) -> str: ...

class WipeTransition(Transition):
    direction: Literal[0, 90, 180, 270]
    def __init__(self, direction: Literal[0, 90, 180, 270]) -> None: ...
    def serialize(self) -> str: ...

class DissolveTransition(Transition):
    def serialize(self) -> str: ...

class GlitterTransition(Transition):
    direction: Literal[0, 270, 315]
    def __init__(self, direction: Literal[0, 270, 315]) -> None: ...
    def serialize(self) -> str: ...

class FlyTransition(Transition):
    dimension: Literal["H", "V"]
    direction: Literal[0, 270] | None
    def __init__(self, dimension: Literal["H", "V"], direction: Literal[0, 270] | None = None) -> None: ...
    def serialize(self) -> str: ...

class PushTransition(Transition):
    direction: Literal[0, 270]
    def __init__(self, direction: Literal[0, 270]) -> None: ...
    def serialize(self) -> str: ...

class CoverTransition(Transition):
    direction: Literal[0, 270]
    def __init__(self, direction: Literal[0, 270]) -> None: ...
    def serialize(self) -> str: ...

class UncoverTransition(Transition):
    direction: Literal[0, 270]
    def __init__(self, direction: Literal[0, 270]) -> None: ...
    def serialize(self) -> str: ...

class FadeTransition(Transition):
    def serialize(self) -> str: ...
