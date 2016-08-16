# Stubs for distutils.spawn

from typing import Optional

def spawn(cmd: List[str], search_path: bool = ...,
          verbose: bool = ..., dry_run: bool = ...) -> None: ...
def find_executable(executable: str,
                    path: Optional[str] = ...) -> Optional[str]: ...
