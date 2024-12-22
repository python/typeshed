from typing import Final
from typing_extensions import TypeAlias

_TagHandleToPrefix: TypeAlias = dict[str, str]

tag_attrib: Final = "_yaml_tag"

class Tag:
    attrib: Final = tag_attrib
    handle: str | None
    suffix: str | None
    handles: _TagHandleToPrefix | None
    def __init__(
        self, *, handle: str | None = None, suffix: str | None = None, handles: _TagHandleToPrefix | None = None
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Tag | str, /) -> bool: ...  # type: ignore[override]
    def startswith(self, x: str, /) -> bool: ...
    @property
    def trval(self) -> str | None: ...
    value = trval
    @property
    def uri_decoded_suffix(self) -> str | None: ...
    def select_transform(self, val: bool, /) -> None: ...
    def check_handle(self) -> bool: ...
