from __future__ import annotations

import xmltodict
from xmltodict import _AttrDict, _AttrValue


# XML post-processor that eats all `b` elements
def b_eater(path: list[tuple[str, _AttrDict | None]], key: str, value: _AttrValue) -> tuple[str, _AttrValue] | None:
    if key == "b":
        return None  # discard the node entirely
    return key, value


xmltodict.parse("<a><b/><c><b/></c></a>", postprocessor=b_eater)
# returns a tree of just <a><c/></a>
