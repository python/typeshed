import sys
from _typeshed import structseq
from typing import Any
from typing_extensions import Final, final

if sys.platform != "win32":
    @final
    class struct_spwd(structseq[Any], tuple[str, str, int, int, int, int, int, int, int]):
        if sys.version_info >= (3, 10):
            __match_args__: Final = (
                "sp_namp",
                "sp_pwdp",
                "sp_lstchg",
                "sp_min",
                "sp_max",
                "sp_warn",
                "sp_inact",
                "sp_expire",
                "sp_flag",
            )
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
