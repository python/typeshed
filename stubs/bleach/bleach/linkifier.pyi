from _typeshed import Incomplete
from collections.abc import Container, Iterable, Iterator
from re import Pattern

from .callbacks import _Callback
from .html5lib_shim import Filter

DEFAULT_CALLBACKS: list[_Callback]

TLDS: list[str]

def build_url_re(tlds: Iterable[str] = ['zw', 'zm', 'za', 'yu', 'yt', 'ye', 'xxx', 'xn', 'ws', 'wf', 'vu', 'vn', 'vi', 'vg', 've', 'vc', 'va', 'uz', 'uy', 'us', 'uk', 'ug', 'ua', 'tz', 'tw', 'tv', 'tt', 'travel', 'tr', 'tp', 'to', 'tn', 'tm', 'tl', 'tk', 'tj', 'th', 'tg', 'tf', 'tel', 'td', 'tc', 'sz', 'sy', 'sx', 'sv', 'su', 'st', 'ss', 'sr', 'so', 'sn', 'sm', 'sl', 'sk', 'sj', 'si', 'sh', 'sg', 'se', 'sd', 'sc', 'sb', 'sa', 'rw', 'ru', 'rs', 'ro', 're', 'qa', 'py', 'pw', 'pt', 'ps', 'pro', 'pr', 'post', 'pn', 'pm', 'pl', 'pk', 'ph', 'pg', 'pf', 'pe', 'pa', 'org', 'om', 'nz', 'nu', 'nr', 'np', 'no', 'nl', 'ni', 'ng', 'nf', 'net', 'ne', 'nc', 'name', 'na', 'mz', 'my', 'mx', 'mw', 'mv', 'museum', 'mu', 'mt', 'ms', 'mr', 'mq', 'mp', 'mobi', 'mo', 'mn', 'mm', 'ml', 'mk', 'mil', 'mh', 'mg', 'me', 'md', 'mc', 'ma', 'ly', 'lv', 'lu', 'lt', 'ls', 'lr', 'lk', 'li', 'lc', 'lb', 'la', 'kz', 'ky', 'kw', 'kr', 'kp', 'kn', 'km', 'ki', 'kh', 'kg', 'ke', 'jp', 'jobs', 'jo', 'jm', 'je', 'it', 'is', 'ir', 'iq', 'io', 'int', 'info', 'in', 'im', 'il', 'ie', 'id', 'hu', 'ht', 'hr', 'hn', 'hm', 'hk', 'gy', 'gw', 'gu', 'gt', 'gs', 'gr', 'gq', 'gp', 'gov', 'gn', 'gm', 'gl', 'gi', 'gh', 'gg', 'gf', 'ge', 'gd', 'gb', 'ga', 'fr', 'fo', 'fm', 'fk', 'fj', 'fi', 'eu', 'et', 'es', 'er', 'eg', 'ee', 'edu', 'ec', 'dz', 'do', 'dm', 'dk', 'dj', 'de', 'cz', 'cy', 'cx', 'cv', 'cu', 'cr', 'coop', 'com', 'co', 'cn', 'cm', 'cl', 'ck', 'ci', 'ch', 'cg', 'cf', 'cd', 'cc', 'cat', 'ca', 'bz', 'by', 'bw', 'bv', 'bt', 'bs', 'br', 'bo', 'bn', 'bm', 'bj', 'biz', 'bi', 'bh', 'bg', 'bf', 'be', 'bd', 'bb', 'ba', 'az', 'ax', 'aw', 'au', 'at', 'asia', 'as', 'arpa', 'ar', 'aq', 'ao', 'an', 'am', 'al', 'ai', 'ag', 'af', 'aero', 'ae', 'ad', 'ac'], protocols: Iterable[str] = ...) -> Pattern[str]: ...

URL_RE: Pattern[str]
PROTO_RE: Pattern[str]

def build_email_re(tlds: Iterable[str] = ['zw', 'zm', 'za', 'yu', 'yt', 'ye', 'xxx', 'xn', 'ws', 'wf', 'vu', 'vn', 'vi', 'vg', 've', 'vc', 'va', 'uz', 'uy', 'us', 'uk', 'ug', 'ua', 'tz', 'tw', 'tv', 'tt', 'travel', 'tr', 'tp', 'to', 'tn', 'tm', 'tl', 'tk', 'tj', 'th', 'tg', 'tf', 'tel', 'td', 'tc', 'sz', 'sy', 'sx', 'sv', 'su', 'st', 'ss', 'sr', 'so', 'sn', 'sm', 'sl', 'sk', 'sj', 'si', 'sh', 'sg', 'se', 'sd', 'sc', 'sb', 'sa', 'rw', 'ru', 'rs', 'ro', 're', 'qa', 'py', 'pw', 'pt', 'ps', 'pro', 'pr', 'post', 'pn', 'pm', 'pl', 'pk', 'ph', 'pg', 'pf', 'pe', 'pa', 'org', 'om', 'nz', 'nu', 'nr', 'np', 'no', 'nl', 'ni', 'ng', 'nf', 'net', 'ne', 'nc', 'name', 'na', 'mz', 'my', 'mx', 'mw', 'mv', 'museum', 'mu', 'mt', 'ms', 'mr', 'mq', 'mp', 'mobi', 'mo', 'mn', 'mm', 'ml', 'mk', 'mil', 'mh', 'mg', 'me', 'md', 'mc', 'ma', 'ly', 'lv', 'lu', 'lt', 'ls', 'lr', 'lk', 'li', 'lc', 'lb', 'la', 'kz', 'ky', 'kw', 'kr', 'kp', 'kn', 'km', 'ki', 'kh', 'kg', 'ke', 'jp', 'jobs', 'jo', 'jm', 'je', 'it', 'is', 'ir', 'iq', 'io', 'int', 'info', 'in', 'im', 'il', 'ie', 'id', 'hu', 'ht', 'hr', 'hn', 'hm', 'hk', 'gy', 'gw', 'gu', 'gt', 'gs', 'gr', 'gq', 'gp', 'gov', 'gn', 'gm', 'gl', 'gi', 'gh', 'gg', 'gf', 'ge', 'gd', 'gb', 'ga', 'fr', 'fo', 'fm', 'fk', 'fj', 'fi', 'eu', 'et', 'es', 'er', 'eg', 'ee', 'edu', 'ec', 'dz', 'do', 'dm', 'dk', 'dj', 'de', 'cz', 'cy', 'cx', 'cv', 'cu', 'cr', 'coop', 'com', 'co', 'cn', 'cm', 'cl', 'ck', 'ci', 'ch', 'cg', 'cf', 'cd', 'cc', 'cat', 'ca', 'bz', 'by', 'bw', 'bv', 'bt', 'bs', 'br', 'bo', 'bn', 'bm', 'bj', 'biz', 'bi', 'bh', 'bg', 'bf', 'be', 'bd', 'bb', 'ba', 'az', 'ax', 'aw', 'au', 'at', 'asia', 'as', 'arpa', 'ar', 'aq', 'ao', 'an', 'am', 'al', 'ai', 'ag', 'af', 'aero', 'ae', 'ad', 'ac']) -> Pattern[str]: ...

EMAIL_RE: Pattern[str]

class Linker:
    def __init__(
        self,
        callbacks: Iterable[_Callback] = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
        recognized_tags: Container[str] | None = ...,
    ) -> None: ...
    def linkify(self, text: str) -> str: ...

class LinkifyFilter(Filter):
    callbacks: Iterable[_Callback]
    skip_tags: Container[str]
    parse_email: bool
    url_re: Pattern[str]
    email_re: Pattern[str]
    def __init__(
        self,
        source,
        callbacks: Iterable[_Callback] | None = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
    ) -> None: ...
    def apply_callbacks(self, attrs, is_new): ...
    def extract_character_data(self, token_list): ...
    def handle_email_addresses(self, src_iter): ...
    def strip_non_url_bits(self, fragment): ...
    def handle_links(self, src_iter): ...
    def handle_a_tag(self, token_buffer): ...
    def extract_entities(self, token): ...
    def __iter__(self) -> Iterator[Incomplete]: ...
