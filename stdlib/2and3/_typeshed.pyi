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
# On Python versions < 3.10 and if "from __future__ import type_checking" 
# is not used, types from this module must be quoted.

import sys
from typing import Text


# PathType can be used in places where starting with Python 3.6 a path
# can be used instead of a string. The alias is generic over the string
# type and should be used as PathType[str], PathType[Text], or
# PathType[bytes], where only on of these types is allowed, or as
# PathType[Union[Text, bytes]], PathType[Union[str, bytes]], or
# PathType[AnyStr] when both bytes and str (or unicode) are supported.
if sys.version_info >= (3, 6):
    from os import PathLike
    PathType = Union[_T, PathLike[_T]]
else:
    PathType = _T
