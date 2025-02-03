from collections.abc import Iterable

from networkx.utils.backends import _dispatchable

@_dispatchable
def join_trees(rooted_trees: Iterable, *, label_attribute: str = None, first_label: int | None = 0): ...
