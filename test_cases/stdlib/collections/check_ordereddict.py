"""
Tests for `ordereddict.popitem` created under @dataclasses.dataclass.
"""

from __future__ import annotations

import dataclasses
from collections import OrderedDict
from typing_extensions import assert_type


def test_ordereddict_popitem(od: OrderedDict[int, int]) -> None:
    assert_type(od.popitem(), tuple[int, int])
    assert_type(od.popitem(True), tuple[int, int])
    assert_type(od.popitem(False), tuple[int, int])
    assert_type(od.popitem(last=True), tuple[int, int])
    assert_type(od.popitem(last=False), tuple[int, int])


def test_ordereddict_popitem_in_object(od: OrderedDict[int, int]) -> None:
    class object:
        d: dict[int, int]

    o = object()
    o.d = od

    assert_type(o.d.popitem(), tuple[int, int])
    assert_type(o.d.popitem(True), tuple[int, int])
    assert_type(o.d.popitem(False), tuple[int, int])
    assert_type(o.d.popitem(last=True), tuple[int, int])
    assert_type(o.d.popitem(last=False), tuple[int, int])


def test_ordereddict_popitem_in_dataclass(od: OrderedDict[int, int]) -> None:
    @dataclasses.dataclass
    class dataclassObject(object):
        d: dict[int, int]

    o = dataclassObject(d=od)

    # TODO: uncomment below tests after fixing the resolution of types in dataclass.
    # assert_type(o.d.popitem(), tuple[int, int])
    # assert_type(o.d.popitem(True), tuple[int, int])
    # assert_type(o.d.popitem(False), tuple[int, int])
    # assert_type(o.d.popitem(last=True), tuple[int, int])
    # assert_type(o.d.popitem(last=False), tuple[int, int])
