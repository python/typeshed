from collections import UserDict
from collections.abc import MutableMapping as MutableMapping
from shutil import which as which
from urllib.parse import quote as quote, quote_plus as quote_plus, unquote as unquote, urlparse as urlparse
from urllib.request import urlopen as urlopen

IterableUserDict = UserDict

def reraise(exc_type, exc_value, exc_traceback) -> None: ...
