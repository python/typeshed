from typing import Any, Dict

from jinja2.filters import FILTERS
from jinja2.tests import TESTS

DEFAULT_FILTERS = FILTERS
DEFAULT_TESTS = TESTS

BLOCK_START_STRING: str
BLOCK_END_STRING: str
VARIABLE_START_STRING: str
VARIABLE_END_STRING: str
COMMENT_START_STRING: str
COMMENT_END_STRING: str
LINE_STATEMENT_PREFIX: str | None
LINE_COMMENT_PREFIX: str | None
TRIM_BLOCKS: bool
LSTRIP_BLOCKS: bool
NEWLINE_SEQUENCE: str
KEEP_TRAILING_NEWLINE: bool
DEFAULT_NAMESPACE: dict[str, Any]
DEFAULT_POLICIES = Dict[str, Any]
