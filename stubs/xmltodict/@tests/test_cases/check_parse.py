from __future__ import annotations

from typing import Any
from typing_extensions import assert_type

import xmltodict
from xmltodict import _Item, _Path

XML = "<a><b>1</b><b>2</b></a>"

# Default mode returns the root element as a dict.
assert_type(xmltodict.parse(XML), "dict[str, Any]")
assert_type(xmltodict.parse(XML, item_depth=0), "dict[str, Any]")


# Streaming mode (item_depth > 0) calls item_callback for each item and returns None.
def on_item(path: _Path, item: _Item) -> bool:
    return True


assert_type(xmltodict.parse(XML, item_depth=2, item_callback=on_item), "dict[str, Any] | None")


# force_list and force_cdata callables receive the list of ancestors, not a single tuple.
def force_list(path: _Path, key: str, value: _Item) -> bool:
    return key == "b"


def force_cdata(path: _Path, key: str, value: str) -> bool:
    return len(path) > 1


xmltodict.parse(XML, force_list=force_list, force_cdata=force_cdata)
