from collections import UserDict
from collections.abc import MutableMapping as MutableMapping
from shutil import which as which
from types import TracebackType
from typing import NoReturn
from urllib.parse import quote as quote, quote_plus as quote_plus, unquote as unquote, urlparse as urlparse
from urllib.request import urlopen as urlopen

IterableUserDict = UserDict

def reraise(exc_type: type[BaseException], exc_value: BaseException, exc_traceback: TracebackType | None) -> NoReturn: ...
