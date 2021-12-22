from _markupbase import ParserBase
from typing import Pattern, Tuple

class HTMLParser(ParserBase):
    def __init__(self, *, convert_charrefs: bool = ...) -> None: ...
    def feed(self, data: str) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def getpos(self) -> tuple[int, int]: ...
    def get_starttag_text(self) -> str | None: ...
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None: ...
    def handle_endtag(self, tag: str) -> None: ...
    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None: ...
    def handle_data(self, data: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def handle_charref(self, name: str) -> None: ...
    def handle_comment(self, data: str) -> None: ...
    def handle_decl(self, decl: str) -> None: ...
    def handle_pi(self, data: str) -> None: ...
    def unknown_decl(self, data: str) -> None: ...
    CDATA_CONTENT_ELEMENTS: Tuple[str, ...]
    def check_for_whole_start_tag(self, i: int) -> int: ...  # undocumented
    def clear_cdata_mode(self) -> None: ...  # undocumented
    def goahead(self, end: bool) -> None: ...  # undocumented
    def parse_bogus_comment(self, i: int, report: bool = ...) -> int: ...  # undocumented
    def parse_endtag(self, i: int) -> int: ...  # undocumented
    def parse_html_declaration(self, i: int) -> int: ...  # undocumented
    def parse_pi(self, i: int) -> int: ...  # undocumented
    def parse_starttag(self, i: int) -> int: ...  # undocumented
    def set_cdata_mode(self, elem: str) -> None: ...  # undocumented
    rawdata: str  # undocumented
    cdata_elem: str | None  # undocumented
    convert_charrefs: bool  # undocumented
    interesting: Pattern[str]  # undocumented
    lasttag: str  # undocumented
    lineno: int  # undocumented
    offset: int  # undocumented
