from typing import List, Tuple
from _markupbase import ParserBase
import sys

class HTMLParser(ParserBase):
    if sys.version_info >= (3, 5):
        def __init__(self, *, convert_charrefs: bool = ...) -> None: ...
    elif sys.version_info >= (3, 4):
        def __init__(self, strict: bool = ..., *,  # type: ignore
                     convert_charrefs: bool = ...) -> None: ...
    else:
        def __init__(self, strict: bool = ...) -> None: ...  # type: ignore
    def feed(self, feed: str) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def getpos(self) -> Tuple[int, int]: ...
    def get_starttag_text(self) -> str: ...

    def handle_starttag(self, tag: str,
                        attrs: List[Tuple[str, str]]) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_startendtag(self, tag: str,
                           attrs: List[Tuple[str, str]]) -> None: ...
    def handle_data(self, data: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def handle_charref(self, name: str) -> None: ...
    def handle_comment(self, data: str) -> None: ...
    def handle_decl(self, decl: str) -> None: ...
    def handle_pi(self, data: str) -> None: ...
    def unknown_decl(self, data: str) -> None: ...

if sys.version_info < (3, 5):
    class HTMLParseError(Exception): ...
