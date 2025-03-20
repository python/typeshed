import re

__version__: str
__author__: str
__email__: str
RFC3339_REGEX_FLAGS: int
RFC3339_REGEX: re.Pattern[str]

def validate_rfc3339(date_string: str) -> bool: ...
