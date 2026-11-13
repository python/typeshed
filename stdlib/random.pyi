import _random
import sys
from _typeshed import FloatInt, SupportsLenAndGetItem
from collections.abc import Callable, Iterable, MutableSequence, Sequence, Set as AbstractSet
from fractions import Fraction
from typing import Any, ClassVar, TypeVar, overload
from typing_extensions import Never, deprecated

__all__ = [
    "Random",
    "seed",
    "random",
    "uniform",
    "randint",
    "choice",
    "sample",
    "randrange",
    "shuffle",
    "normalvariate",
    "lognormvariate",
    "expovariate",
    "vonmisesvariate",
    "gammavariate",
    "triangular",
    "gauss",
    "betavariate",
    "paretovariate",
    "weibullvariate",
    "getstate",
    "setstate",
    "getrandbits",
    "choices",
    "SystemRandom",
    "randbytes",
]

if sys.version_info >= (3, 12):
    __all__ += ["binomialvariate"]

_T = TypeVar("_T")

class Random(_random.Random):
    VERSION: ClassVar[int]
    def __init__(self, x: float | int | str | bytes | bytearray | None = None) -> None: ...
    def seed(self, a: float | int | str | bytes | bytearray | None = None, version: int = 2) -> None: ...  # type: ignore[override]
    def getstate(self) -> tuple[Any, ...]: ...
    def setstate(self, state: tuple[Any, ...]) -> None: ...
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int: ...
    def randint(self, a: int, b: int) -> int: ...
    def randbytes(self, n: int) -> bytes: ...
    def choice(self, seq: SupportsLenAndGetItem[_T]) -> _T: ...
    def choices(
        self,
        population: SupportsLenAndGetItem[_T],
        weights: Sequence[FloatInt | Fraction] | None = None,
        *,
        cum_weights: Sequence[FloatInt | Fraction] | None = None,
        k: int = 1,
    ) -> list[_T]: ...
    if sys.version_info >= (3, 11):
        def shuffle(self, x: MutableSequence[Any]) -> None: ...
    else:
        @overload
        def shuffle(self, x: MutableSequence[Any]) -> None: ...
        @overload
        @deprecated("The `random` parameter is deprecated since Python 3.9; removed in Python 3.11.")
        def shuffle(self, x: MutableSequence[Any], random: Callable[[], float] | None = None) -> None: ...

    if sys.version_info >= (3, 11):
        def sample(self, population: Sequence[_T], k: int, *, counts: Iterable[int] | None = None) -> list[_T]: ...
    else:
        def sample(
            self, population: Sequence[_T] | AbstractSet[_T], k: int, *, counts: Iterable[int] | None = None
        ) -> list[_T]: ...

    def uniform(self, a: FloatInt, b: FloatInt) -> float: ...
    def triangular(self, low: FloatInt = 0.0, high: FloatInt = 1.0, mode: FloatInt | None = None) -> float: ...
    if sys.version_info >= (3, 12):
        def binomialvariate(self, n: int = 1, p: FloatInt = 0.5) -> int: ...

    def betavariate(self, alpha: FloatInt, beta: FloatInt) -> float: ...
    if sys.version_info >= (3, 12):
        def expovariate(self, lambd: FloatInt = 1.0) -> float: ...
    else:
        def expovariate(self, lambd: FloatInt) -> float: ...

    def gammavariate(self, alpha: FloatInt, beta: FloatInt) -> float: ...
    if sys.version_info >= (3, 11):
        def gauss(self, mu: FloatInt = 0.0, sigma: FloatInt = 1.0) -> float: ...
        def normalvariate(self, mu: FloatInt = 0.0, sigma: FloatInt = 1.0) -> float: ...
    else:
        def gauss(self, mu: FloatInt, sigma: FloatInt) -> float: ...
        def normalvariate(self, mu: FloatInt, sigma: FloatInt) -> float: ...

    def lognormvariate(self, mu: FloatInt, sigma: FloatInt) -> float: ...
    def vonmisesvariate(self, mu: FloatInt, kappa: FloatInt) -> float: ...
    def paretovariate(self, alpha: FloatInt) -> float: ...
    def weibullvariate(self, alpha: FloatInt, beta: FloatInt) -> float: ...

# SystemRandom is not implemented for all OS's; good on Windows & Linux
class SystemRandom(Random):
    def getrandbits(self, k: int) -> int: ...  # k can be passed by keyword
    def getstate(self, *args: Any, **kwds: Any) -> Never: ...
    def setstate(self, *args: Any, **kwds: Any) -> Never: ...

_inst: Random
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
choices = _inst.choices
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
if sys.version_info >= (3, 12):
    binomialvariate = _inst.binomialvariate
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
getrandbits = _inst.getrandbits
randbytes = _inst.randbytes
