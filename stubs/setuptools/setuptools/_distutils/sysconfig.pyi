from typing import Literal, overload
from typing_extensions import deprecated

from setuptools._distutils.ccompiler import CCompiler

PREFIX: str
EXEC_PREFIX: str

@overload
@deprecated("SO is deprecated, use EXT_SUFFIX. Support will be removed when this module is synchronized with stdlib Python 3.11")
def get_config_var(name: Literal["SO"]) -> int | str | None: ...
@overload
def get_config_var(name: str) -> int | str | None: ...
@overload
def get_config_vars() -> dict[str, str | int]: ...
@overload
def get_config_vars(arg: str, /, *args: str) -> list[str | int]: ...
def get_config_h_filename() -> str: ...
def get_makefile_filename() -> str: ...
def get_python_inc(plat_specific: bool = False, prefix: str | None = ...) -> str: ...
def get_python_lib(plat_specific: bool = False, standard_lib: bool = False, prefix: str | None = ...) -> str: ...
def customize_compiler(compiler: CCompiler) -> None: ...
