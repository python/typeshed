from _typeshed import Unused
from collections.abc import Callable, Iterable
from types import ModuleType
from typing import Any, NoReturn, TypeVar
from typing_extensions import deprecated

_R = TypeVar("_R")
_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])

# This changes the signature by replacing a `txt` parameter with `text`.
def support_deprecated_txt_arg(fn: Callable[..., _R]) -> Callable[..., _R]: ...
def deprecated_parameter(parameters: Iterable[tuple[str, str]]) -> Callable[[_CallableT], _CallableT]: ...

class WarnOnDeprecatedModuleAttributes(ModuleType):
    def __call__(self) -> NoReturn: ...
    @property
    @deprecated("deprecated in favour of FPDF(font_cache_dir=...)")
    def FPDF_CACHE_DIR(self) -> None: ...
    @FPDF_CACHE_DIR.setter
    @deprecated("deprecated in favour of FPDF(font_cache_dir=...)")
    def FPDF_CACHE_DIR(self, value: Unused, /) -> None: ...
    @property
    @deprecated("deprecated in favour of FPDF(font_cache_dir=...)")
    def FPDF_CACHE_MODE(self) -> None: ...
    @FPDF_CACHE_MODE.setter
    @deprecated("deprecated in favour of FPDF(font_cache_dir=...)")
    def FPDF_CACHE_MODE(self, value: Unused, /) -> None: ...

def get_stack_level() -> int: ...
