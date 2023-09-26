from __future__ import annotations

from typing_extensions import assert_type

x : list[int] = []
assert_type(list(reversed(x)), list[int])

iterator = iter(x)
assert_type(list(reversed(iterator)), list[int])

class LenAndGetItem:
    def __len__(self):
        return 0
    def __getitem__(self, item: int) -> int:
        raise KeyError

len_and_get_item = LenAndGetItem()
assert_type(list(reversed(len_and_get_item)), list[int])
