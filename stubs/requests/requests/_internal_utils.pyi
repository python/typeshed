from re import Pattern

_VALID_HEADER_NAME_RE_BYTE: Pattern[bytes]
_VALID_HEADER_NAME_RE_STR: Pattern[str]
_VALID_HEADER_VALUE_RE_BYTE: Pattern[bytes]
_VALID_HEADER_VALUE_RE_STR: Pattern[str]

HEADER_VALIDATORS = {
    bytes: (_VALID_HEADER_NAME_RE_BYTE, _VALID_HEADER_VALUE_RE_BYTE),
    str: (_VALID_HEADER_NAME_RE_STR, _VALID_HEADER_VALUE_RE_STR),
}

def to_native_string(string: str | bytes, encoding: str = ...) -> str: ...
def unicode_is_ascii(u_string: str) -> bool: ...
