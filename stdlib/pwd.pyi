from _typeshed import structseq
from typing import Any, Sequence, overload
from typing_extensions import Literal, SupportsIndex

class struct_passwd(structseq[Any]):  # Constructor must be passed a sequence of length 7
    @overload  # type: ignore[override]
    def __getitem__(self, __i: Literal[0, 1, 4, 5, 6]) -> str: ...
    @overload
    def __getitem__(self, __i: Literal[2, 3]) -> int: ...
    @overload
    def __getitem__(self, __i: SupportsIndex) -> Any: ...
    @overload
    def __getitem__(self, __i: slice) -> Sequence[Any]: ...
    @property
    def pw_name(self) -> str: ...
    @property
    def pw_passwd(self) -> str: ...
    @property
    def pw_uid(self) -> int: ...
    @property
    def pw_gid(self) -> int: ...
    @property
    def pw_gecos(self) -> str: ...
    @property
    def pw_dir(self) -> str: ...
    @property
    def pw_shell(self) -> str: ...

def getpwall() -> list[struct_passwd]: ...
def getpwuid(__uid: int) -> struct_passwd: ...
def getpwnam(__name: str) -> struct_passwd: ...
