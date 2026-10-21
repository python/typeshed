from _typeshed import FileDescriptorLike, SupportsRead, SupportsWrite
from collections.abc import Callable
from typing import Any, Final, TypeAlias, overload
from typing_extensions import Self, disjoint_base

CALLBACK_CONTINUE: Final[int]
CALLBACK_ABORT: Final[int]
CALLBACK_MATCHES: Final[int]
CALLBACK_NON_MATCHES: Final[int]
CALLBACK_ALL: Final[int]
CALLBACK_TOO_MANY_MATCHES: Final[int]
__version__: Final[str]
YARA_VERSION: Final[str]
YARA_VERSION_HEX: Final[int]

class Error(Exception): ...
class SyntaxError(Error): ...
class TimeoutError(Error): ...

class WarningError(Error):
    @property
    def warnings(self) -> list[str]: ...

@disjoint_base
class Rule:
    @property
    def is_global(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def identifier(self) -> str: ...
    @property
    def tags(self) -> list[str]: ...
    @property
    def meta(self) -> dict[str, bool | int | str]: ...

@disjoint_base
class Rules:
    @property
    def warnings(self) -> list[str]: ...

    @overload
    def match(
        self,
        filepath: str,
        pid: int = ...,
        data: bytes | str = ...,
        externals: dict[str, bool | int | float | str] | None = None,
        callback: Callable[[dict[str, Any]], Any] | None = None,
        fast: bool = False,
        timeout: int = ...,
        modules_data: dict[str, bytes] | None = None,
        modules_callback: Callable[[dict[str, Any]], int] | None = None,
        which_callbacks: int = ...,
        warnings_callback: Callable[[int, str], int] | None = None,
        console_callback: Callable[[str], Any] | None = None,
        allow_duplicate_metadata: bool = False,
    ) -> list[Match]: ...
    @overload
    def match(
        self,
        *,
        filepath: str = ...,
        pid: int,
        data: bytes | str = ...,
        externals: dict[str, bool | int | float | str] | None = None,
        callback: Callable[[dict[str, Any]], Any] | None = None,
        fast: bool = False,
        timeout: int = ...,
        modules_data: dict[str, bytes] | None = None,
        modules_callback: Callable[[dict[str, Any]], int] | None = None,
        which_callbacks: int = ...,
        warnings_callback: Callable[[int, str], int] | None = None,
        console_callback: Callable[[str], Any] | None = None,
        allow_duplicate_metadata: bool = False,
    ) -> list[Match]: ...
    @overload
    def match(
        self,
        *,
        filepath: str = ...,
        pid: int = ...,
        data: bytes | str,
        externals: dict[str, bool | int | float | str] | None = None,
        callback: Callable[[dict[str, Any]], Any] | None = None,
        fast: bool = False,
        timeout: int = ...,
        modules_data: dict[str, bytes] | None = None,
        modules_callback: Callable[[dict[str, Any]], int] | None = None,
        which_callbacks: int = ...,
        warnings_callback: Callable[[int, str], int] | None = None,
        console_callback: Callable[[str], Any] | None = None,
        allow_duplicate_metadata: bool = False,
    ) -> list[Match]: ...

    @overload
    def save(self, filepath: str) -> None: ...
    @overload
    def save(self, file: SupportsWrite[bytes]) -> None: ...

    def profiling_info(self) -> dict[str, int]: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> Rule: ...

@disjoint_base
class Match:
    @property
    def rule(self) -> str: ...
    @property
    def namespace(self) -> str: ...
    @property
    def tags(self) -> list[str]: ...
    @property
    def meta(
        self,
    ) -> dict[str, bool | int | str] | dict[str, list[bool | int | str]]: ...  # Depending on `allow_duplicate_metadata`
    @property
    def strings(self) -> list[StringMatch]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object, /) -> bool: ...
    def __ne__(self, other: object, /) -> bool: ...
    def __lt__(self, other: object, /) -> bool: ...
    def __gt__(self, other: object, /) -> bool: ...
    def __le__(self, other: object, /) -> bool: ...
    def __ge__(self, other: object, /) -> bool: ...

@disjoint_base
class StringMatch:
    @property
    def identifier(self) -> str: ...
    @property
    def instances(self) -> list[StringMatchInstance]: ...
    def is_xor(self) -> bool: ...
    def __hash__(self) -> int: ...

@disjoint_base
class StringMatchInstance:
    @property
    def offset(self) -> int: ...
    @property
    def matched_data(self) -> bytes: ...
    @property
    def matched_length(self) -> int: ...
    @property
    def xor_key(self) -> int: ...
    def plaintext(self) -> bytes: ...
    def __hash__(self) -> int: ...

modules: list[str]

_IncludeCallback: TypeAlias = Callable[[str | None, str | None, str | None], str]

@overload
def compile(
    filepath: str,
    includes: bool = True,
    externals: dict[str, bool | int | float | str] | None = None,
    error_on_warning: bool = False,
    strict_escape: bool = False,
    include_callback: _IncludeCallback | None = None,
) -> Rules: ...
@overload
def compile(
    *,
    source: str,
    includes: bool = True,
    externals: dict[str, bool | int | float | str] | None = None,
    error_on_warning: bool = False,
    strict_escape: bool = False,
    include_callback: _IncludeCallback | None = None,
) -> Rules: ...
@overload
def compile(
    *,
    file: FileDescriptorLike,
    includes: bool = True,
    externals: dict[str, bool | int | float | str] | None = None,
    error_on_warning: bool = False,
    strict_escape: bool = False,
    include_callback: _IncludeCallback | None = None,
) -> Rules: ...
@overload
def compile(
    *,
    filepaths: dict[str, str],
    includes: bool = True,
    externals: dict[str, bool | int | float | str] | None = None,
    error_on_warning: bool = False,
    strict_escape: bool = False,
    include_callback: _IncludeCallback | None = None,
) -> Rules: ...
@overload
def compile(
    *,
    sources: dict[str, str],
    includes: bool = True,
    externals: dict[str, bool | int | float | str] | None = None,
    error_on_warning: bool = False,
    strict_escape: bool = False,
    include_callback: _IncludeCallback | None = None,
) -> Rules: ...

@overload
def load(filepath: str) -> Rules: ...
@overload
def load(file: SupportsRead[bytes]) -> Rules: ...

def set_config(stack_size: int = 0, max_strings_per_rule: int = 0, max_match_data: int = 0) -> None: ...
