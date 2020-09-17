# Source: https://hg.python.org/cpython/file/2.7/Lib/sre_compile.py
# and https://github.com/python/cpython/blob/master/Lib/sre_compile.py

import sys
from sre_parse import SubPattern
from typing import Any, List, Pattern, Tuple, Type, Union

# SRE_* constants are undocumented
SRE_FLAG_ASCII: int
SRE_FLAG_DEBUG: int
SRE_FLAG_DOTALL: int
SRE_FLAG_IGNORECASE: int
SRE_FLAG_LOCALE: int
SRE_FLAG_MULTILINE: int
SRE_FLAG_TEMPLATE: int
SRE_FLAG_UNICODE: int
SRE_FLAG_VERBOSE: int
SRE_INFO_CHARSET: int
SRE_INFO_LITERAL: int
SRE_INFO_PREFIX: int

MAXCODE: int
if sys.version_info < (3, 0):
    STRING_TYPES: Tuple[Type[str], Type[unicode]]
    _IsStringType = int
else:
    from sre_constants import _NamedIntConstant
    def dis(code: List[_NamedIntConstant]) -> None: ...
    _IsStringType = bool

def isstring(obj: Any) -> _IsStringType: ...
def compile(p: Union[str, bytes, SubPattern], flags: int = ...) -> Pattern[Any]: ...
