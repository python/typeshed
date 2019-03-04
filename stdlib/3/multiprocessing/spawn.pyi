from typing import Any, Dict, List, Optional
from types import ModuleType

WINEXE: bool
WINSERVICE: bool
# undocumented
_python_exe: str

def set_executable(executable: str) -> None: ...
def get_executable() -> str: ...
def is_forking(argv: List[str]) -> bool: ...
def freeze_support() -> None: ...
def get_command_line(**kwds: Any) -> List[str]: ...
def spawn_main(pipe_handle: int, parent_pid: Optional[int] = ..., tracker_fd: Optional[float] = ...) -> None: ...
# undocumented
def _main(fd: int) -> Any: ...
def get_preparation_data(name: str) -> Dict[str,str]: ...
old_main_modules: List[ModuleType] = ...
def prepare(data: Dict[str,str]) -> None: ... 
def import_main_path(main_path: str) -> None: ...