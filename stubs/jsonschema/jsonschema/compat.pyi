from collections import MutableMapping as MutableMapping, Sequence as Sequence
from functools import lru_cache as lru_cache
from typing import Any
from urllib.parse import SplitResult as SplitResult, unquote as unquote, urljoin as urljoin
from urllib.request import pathname2url as pathname2url, urlopen as urlopen

PY3: Any
zip = zip
str_types: Any
int_types: Any
iteritems: Any

def urldefrag(url): ...
