from typing import Any

class Search:
    class IsNodeBuilder:
        name: Any
        def __init__(self, name) -> None: ...
        def __eq__(self, value): ...
        def is_equal(self, value): ...

    class EqualityNodeBuilder(IsNodeBuilder):
        def __ne__(self, value): ...
        def is_not_equal(self, value): ...

    class KeyValueNodeBuilder:
        name: Any
        def __init__(self, name) -> None: ...
        def __eq__(self, value): ...
        def is_equal(self, value): ...
        def __ne__(self, value): ...
        def is_not_equal(self, value): ...

    class PartialMatchNodeBuilder(EqualityNodeBuilder):
        def starts_with(self, value): ...
        def ends_with(self, value): ...

    class EndsWithNodeBuilder:
        name: Any
        def __init__(self, name) -> None: ...
        def ends_with(self, value): ...

    class TextNodeBuilder(PartialMatchNodeBuilder):
        def contains(self, value): ...

    class Node:
        name: Any
        dict: Any
        def __init__(self, name, dict) -> None: ...
        def to_param(self): ...

    class MultipleValueNodeBuilder:
        name: Any
        whitelist: Any
        def __init__(self, name, whitelist=[]) -> None: ...
        def in_list(self, *values): ...
        def __eq__(self, value): ...

    class MultipleValueOrTextNodeBuilder(TextNodeBuilder, MultipleValueNodeBuilder):
        def __init__(self, name, whitelist=[]) -> None: ...

    class RangeNodeBuilder:
        name: Any
        def __init__(self, name) -> None: ...
        def __eq__(self, value): ...
        def is_equal(self, value): ...
        def __ge__(self, min): ...
        def greater_than_or_equal_to(self, min): ...
        def __le__(self, max): ...
        def less_than_or_equal_to(self, max): ...
        def between(self, min, max): ...
