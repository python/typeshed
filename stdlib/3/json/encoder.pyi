from typing import Any, Callable, Iterator, Tuple

class JSONEncoder:
    item_separator = ...  # type: str
    key_separator = ...  # type: str

    skipkeys = ...  # type: bool
    ensure_ascii = ...  # type: bool
    check_circular = ...  # type: bool
    allow_nan = ...  # type: bool
    sort_keys = ...  # type: bool
    indent = None  # type: int

    def __init__(self, skipkeys: bool=..., ensure_ascii: bool=...,
            check_circular: bool=..., allow_nan: bool=..., sort_keys: bool=...,
            indent: int=None, separators: Tuple[str, str]=None, default: Callable=None) -> None: ...

    def default(self, o: Any) -> Any: ...
    def encode(self, o: Any) -> str: ...
    def iterencode(self, o: Any, _one_shot: bool=False) -> Iterator[str]: ...
