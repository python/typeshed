from typing import Iterable, Tuple, Optional, Any, Type
from types import TracebackType

def __getattr__(name: str) -> Any: ...  # incomplete

_SysExcInfoType = Tuple[
    Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]
]

# undocumented
class _Outcome:
    def __getattr__(name: str) -> Any: ...  # incomplete
    # Any below should actually be TestCase, but that results in circular
    # references, and moving TestCase in here means moving a lot of other
    # pieces around. So, for now, just use Any.
    errors = ...  # type: Iterable[Tuple[Any, Optional[_SysExcInfoType]]]
