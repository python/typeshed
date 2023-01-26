from __future__ import annotations

import re
import typing as t
from typing_extensions import assert_type


def check_re_search(pattern: re.Pattern[t.AnyStr], string: t.AnyStr) -> re.Match[t.AnyStr]:
    """See issue #9591"""
    match = pattern.search(string)
    if match is None:
        raise ValueError(f"'{string!r}' does not match {pattern!r}")
    return match


def check_no_ReadableBuffer_false_negatives() -> None:
    b = bytearray(b"foo")  # ReadableBuffer

    string_pattern = re.compile("foo")
    string_pattern.search(b)  # type: ignore

    bytes_pattern = re.compile(b"foo")
    assert_type(bytes_pattern.search(b), t.Optional[t.Match[bytes]])
