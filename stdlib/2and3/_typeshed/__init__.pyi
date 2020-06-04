# Utility types for typeshed

# This module contains various common types to be used by typeshed. The
# module and its types do not exist at runtime. You can use this module
# outside of typeshed, but no API stability guarantees are made. To use
# it in implementation (.py) files, the following construct must be used:
#
#     from typing import TYPE_CHECKING
#     if TYPE_CHECKING:
#         from _typeshed import ...
#
# If on Python versions < 3.10 and "from __future__ import annotations"
# is not used, types from this module must be quoted.

import sys
from typing import Text, Union

# StrPath and AnyPath can be used in places where a
# path can be used instead of a string, starting with Python 3.6.
if sys.version_info >= (3, 6):
    from os import PathLike
    StrPath = Union[str, PathLike[str]]
    BytesPath = Union[bytes, PathLike[bytes]]
    AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
    StrPath = Text
    BytesPath = bytes
    AnyPath = Union[Text, bytes]
