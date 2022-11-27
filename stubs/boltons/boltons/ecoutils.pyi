# TODO: DONE!

from typing import Any, NoReturn

ECO_VERSION: str
PY_GT_2: bool
HAVE_URANDOM: bool
INSTANCE_ID: str
IS_64BIT: bool
HAVE_UCS4: bool
HAVE_READLINE: bool
SQLITE_VERSION: str
OPENSSL_VERSION: str
TKINTER_VERSION: str
ZLIB_VERSION: str
EXPAT_VERSION: str
CPU_COUNT: int
HAVE_THREADING: bool
HAVE_IPV6: bool
RLIMIT_NOFILE: int
RLIMIT_FDS_SOFT: int
RLIMIT_FDS_HARD: int
START_TIME_INFO: dict[str, str | float]

# def getrandbits(__k: int) -> int: ...
getrandbits: Any

def get_python_info() -> dict[str, Any]: ...
def get_profile(**kwargs) -> dict[str, Any]: ...
def get_profile_json(indent: bool = ...) -> str: ...
def main() -> NoReturn: ...
def dumps(val: Any, indent: int) -> str: ...

# def _escape_shell_args(args, sep=' ', style=None) -> str: ...
# def _args2sh(args, sep=' ') -> str: ...
# def _args2cmd(args, sep=' ') -> str: ...
