import re
from collections.abc import Sequence
from operator import itemgetter

CS_ESCAPE: re.Pattern[str]
FIRST_ELEMENT: itemgetter[int]

def make_charset(letters: Sequence[str]) -> str: ...
def regex_opt_inner(strings: Sequence[str], open_paren: str) -> str: ...
def regex_opt(strings: Sequence[str], prefix: str = "", suffix: str = "") -> str: ...
