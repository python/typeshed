from collections.abc import MutableMapping
from typing import Protocol
from typing_extensions import TypeAlias

_AttrKey: TypeAlias = tuple[str | None, str]
_Attrs: TypeAlias = MutableMapping[_AttrKey, str]

class _Callback(Protocol):  # noqa: Y046
    def __call__(self, attrs: _Attrs, new: bool = ...) -> _Attrs: ...

def nofollow(attrs: _Attrs, new: bool = ...) -> _Attrs: ...
def target_blank(attrs: _Attrs, new: bool = ...) -> _Attrs: ...
