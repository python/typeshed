# mypy: disable-error-code=assert-type

from __future__ import annotations

from collections.abc import Iterator, Sequence
from itertools import groupby
from typing_extensions import assert_type


def check_union_input(items: Sequence[str] | Sequence[int]) -> None:
    for _, group in groupby(items):
        assert_type(group, Iterator[str] | Iterator[int])
