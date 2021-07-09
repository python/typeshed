from typing import List, Tuple

class struct_passwd(Tuple[str, str, int, int, str, str, str]):
    pw_name: str
    pw_passwd: str
    pw_uid: int
    pw_gid: int
    pw_gecos: str
    pw_dir: str
    pw_shell: str

    @property
    def n_fields(self) -> int: ...
    @property
    def n_sequence_fields(self) -> int: ...
    @property
    def n_unnamed_fields(self) -> int: ...

def getpwall() -> List[struct_passwd]: ...
def getpwuid(__uid: int) -> struct_passwd: ...
def getpwnam(__name: str) -> struct_passwd: ...
