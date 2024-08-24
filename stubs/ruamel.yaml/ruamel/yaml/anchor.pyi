from _typeshed import Incomplete
from typing import Literal

anchor_attrib: Literal["_yaml_anchor"]

class Anchor:
    attrib = anchor_attrib
    value: Incomplete
    always_dump: bool
    def __init__(self) -> None: ...
