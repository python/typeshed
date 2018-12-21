from typing import Any, List, MutableMapping, Protocol, Pattern, Iterable, Optional

_Attrs = MutableMapping[Any, str]

class _Callback(Protocol):
    def __call__(self, attrs: _Attrs, new: bool = ...) -> _Attrs: ...

DEFAULT_CALLBACKS: List[_Callback]

TLDS: List[str]

def build_url_re(tlds: Iterable[str] = ..., protocols: Iterable[str] = ...) -> Pattern[str]: ...

URL_RE: Pattern[str]
PHOTO_RE: Pattern[str]
EMAIL_RE: Pattern[str]

class Linker:
    def __init__(
        self,
        callbacks: List[_Callback] = ...,
        skip_tags: Optional[List[str]] = ...,
        parse_email: bool = ...,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
    ) -> None: ...
    def linkify(self, text: str) -> str: ...

class LinkifyFilter:
    def __getattr__(self, item: str) -> Any: ...  # incomplete
