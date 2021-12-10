from _typeshed import structseq
from typing import Any, Tuple, overload
from typing_extensions import Literal, SupportsIndex, final

@final
class struct_spwd(structseq[Any]):  # Constructor must be passed an iterable of length 9
    @overload  # type: ignore[override]
    def __getitem__(self, __i: Literal[0, 1]) -> str: ...
    @overload
    def __getitem__(self, __i: Literal[2, 3, 4, 5, 6, 7, 8]) -> int: ...
    @overload
    def __getitem__(self, __i: SupportsIndex) -> Any: ...
    @overload
    def __getitem__(self, __i: slice) -> Tuple[Any, ...]: ...
    @property
    def sp_namp(self) -> str: ...
    @property
    def sp_pwdp(self) -> str: ...
    @property
    def sp_lstchg(self) -> int: ...
    @property
    def sp_min(self) -> int: ...
    @property
    def sp_max(self) -> int: ...
    @property
    def sp_warn(self) -> int: ...
    @property
    def sp_inact(self) -> int: ...
    @property
    def sp_expire(self) -> int: ...
    @property
    def sp_flag(self) -> int: ...

def getspall() -> list[struct_spwd]: ...
def getspnam(__arg: str) -> struct_spwd: ...
