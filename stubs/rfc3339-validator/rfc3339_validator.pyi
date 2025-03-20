import re

__version__: str
RFC3339_REGEX_FLAGS: int
RFC3339_REGEX: re.Pattern[str]

def validate_rfc3339(date_string: str) -> bool: ...
