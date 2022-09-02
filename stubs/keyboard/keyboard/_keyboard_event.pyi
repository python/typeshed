from typing import Tuple  # noqa: Y022 # Arbitrary length Tuple
from typing_extensions import Literal

from ._canonical_names import canonical_names as canonical_names, normalize_name as normalize_name

basestring = str
KEY_DOWN: Literal["down"]
KEY_UP: Literal["up"]

class KeyboardEvent:
    event_type: Literal["down", "up"] | None
    scan_code: int | None
    name: str | None
    time: float | None
    device: str | None
    modifiers: Tuple[str, ...] | None
    is_keypad: bool | None

    def __init__(
        self,
        event_type: Literal["down", "up"] | None,
        scan_code: int | None,
        name: str | None = ...,
        time: float | None = ...,
        device: str | None = ...,
        modifiers: Tuple[str, ...] | None = ...,
        is_keypad: bool | None = ...,
    ) -> None: ...
    def to_json(self, ensure_ascii: bool = ...) -> str: ...
    def __eq__(self, other: object) -> bool: ...
