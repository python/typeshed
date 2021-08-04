from sre_constants import SRE_FLAG_ASCII as SRE_FLAG_ASCII
from sre_constants import SRE_FLAG_DEBUG as SRE_FLAG_DEBUG
from sre_constants import SRE_FLAG_DOTALL as SRE_FLAG_DOTALL
from sre_constants import SRE_FLAG_IGNORECASE as SRE_FLAG_IGNORECASE
from sre_constants import SRE_FLAG_LOCALE as SRE_FLAG_LOCALE
from sre_constants import SRE_FLAG_MULTILINE as SRE_FLAG_MULTILINE
from sre_constants import SRE_FLAG_TEMPLATE as SRE_FLAG_TEMPLATE
from sre_constants import SRE_FLAG_UNICODE as SRE_FLAG_UNICODE
from sre_constants import SRE_FLAG_VERBOSE as SRE_FLAG_VERBOSE
from sre_constants import SRE_INFO_CHARSET as SRE_INFO_CHARSET
from sre_constants import SRE_INFO_LITERAL as SRE_INFO_LITERAL
from sre_constants import SRE_INFO_PREFIX as SRE_INFO_PREFIX
from sre_constants import _NamedIntConstant
from sre_parse import SubPattern
from typing import Any, List, Pattern, Union

MAXCODE: int

def dis(code: List[_NamedIntConstant]) -> None: ...
def isstring(obj: Any) -> bool: ...
def compile(p: Union[str, bytes, SubPattern], flags: int = ...) -> Pattern[Any]: ...
