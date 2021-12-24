from _typeshed import structseq
from typing import Any
from typing_extensions import final

@final
class struct_passwd(structseq[Any], tuple[str, str, int, int, str, str, str]):
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
