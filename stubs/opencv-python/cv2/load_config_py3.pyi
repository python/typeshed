from _typeshed import StrOrBytesPath
from collections.abc import Mapping
from typing import Any

def exec_file_wrapper(fpath: StrOrBytesPath, g_vars: dict[str, Any] | None, l_vars: Mapping[str, object] | None) -> None: ...
