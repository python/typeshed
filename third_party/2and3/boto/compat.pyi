import sys

from typing import Any
from base64 import encodestring as encodebytes

from six.moves import http_client

expanduser: Any

if sys.version_info >= (3, 0):
    StandardError = Exception
else:
    StandardError = __builtins__.StandardError

long_type: Any
unquote_str: Any
parse_qs_safe: Any
