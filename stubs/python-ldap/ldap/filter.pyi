from collections.abc import Iterable

from ldap.functions import strf_secs as strf_secs
from ldap.pkginfo import __version__ as __version__

def escape_filter_chars(assertion_value: str, escape_mode: int = 0) -> str: ...
def filter_format(filter_template: str, assertion_values: Iterable[str]) -> str: ...
def time_span_filter(
    filterstr: str = "",
    from_timestamp: int | float = 0,
    until_timestamp: int | float | None = None,
    delta_attr: str = "modifyTimestamp",
) -> str: ...
def is_filter(ldap_filter: str) -> bool: ...
