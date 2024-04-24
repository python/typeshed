from __future__ import annotations

from typing_extensions import Literal, assert_type

# perhaps the `__len__` of these literals can be narrowed to return
# `typing.Literal[0]` in the future
assert_type("".__len__(), int)
assert_type(len(""), int)

assert_type(b"".__len__(), int)
assert_type(len(b""), int)

assert_type([].__len__(), int)
assert_type(len([]), int)

assert_type(().__len__(), int)
assert_type(len(()), int)

assert_type({}.__len__(), int)
assert_type(len({}), int)

assert_type(set().__len__(), int)
assert_type(len(set()), int)

assert_type(frozenset[object]().__len__(), int)
assert_type(len(frozenset[object]()), int)

assert_type(range(0).__len__(), int)
assert_type(len(range(0)), int)


class Point:
    def __len__(self) -> Literal[0]:
        return 0


# len() and __len__() return tupes should match invariably
assert_type(Point().__len__(), Literal[0])
assert_type(len(Point()), Literal[0])
