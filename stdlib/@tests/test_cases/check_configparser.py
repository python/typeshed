from configparser import SectionProxy
from typing_extensions import assert_type

sp: SectionProxy
assert_type(sp.get("foo", fallback="hi"), str)
