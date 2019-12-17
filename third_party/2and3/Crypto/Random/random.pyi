from typing import Any, List, Optional, Sequence, TypeVar

_T = TypeVar('_T')

class StrongRandom:
    def __init__(self, rng: Optional[Any] = ..., randfunc: Optional[Any] = ...) -> None: ...
    def getrandbits(self, k: int) -> int: ...
    def randrange(self, *args: int) -> int: ...
    def randint(self, a: int, b: int) -> int: ...
    def choice(self, seq: Sequence[_T]) -> _T: ...
    def shuffle(self, x: Sequence[_T]): ...
    def sample(self, population: Sequence[_T], k: int) -> List[_T]: ...

def getrandbits(self, k: int) -> int: ...
def randrange(self, *args: int) -> int: ...
def randint(self, a: int, b: int) -> int: ...
def choice(self, seq: Sequence[_T]) -> _T: ...
def shuffle(self, x: Sequence[_T]): ...
def sample(self, population: Sequence[_T], k: int) -> List[_T]: ...
