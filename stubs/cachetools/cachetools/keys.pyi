from collections.abc import Hashable


def hashkey(*args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
def typedkey(*args: Hashable, **kwargs: Hashable) -> tuple[Hashable, ...]: ...
