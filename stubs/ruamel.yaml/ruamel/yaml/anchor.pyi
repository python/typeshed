from typing import Final

anchor_attrib: Final = "_yaml_anchor"

class Anchor:
    attrib: Final = anchor_attrib
    value: str | None
    always_dump: bool
    def __init__(self) -> None: ...
