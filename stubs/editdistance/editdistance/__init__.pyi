from collections.abc import Hashable, Iterable

def eval(a: Iterable[Hashable], b: Iterable[Hashable]) -> int: ...
def distance(a: Iterable[Hashable], b: Iterable[Hashable]) -> int: ...
def eval_criterion(a: Iterable[Hashable], b: Iterable[Hashable], thr: int) -> bool: ...
def distance_le_than(a: Iterable[Hashable], b: Iterable[Hashable], thr: int) -> bool: ...
