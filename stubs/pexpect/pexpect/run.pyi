from _typeshed import FileDescriptorOrPath
from collections.abc import Callable, Mapping
from typing import Any, Literal, TypeAlias, overload

from .spawnbase import _InputRePattern, _Logfile

# Values are sent to the child if they are strings, and called with the
# caller's locals() otherwise.
_Response: TypeAlias = str | bytes | Callable[[dict[str, Any]], object]
_Events: TypeAlias = list[tuple[_InputRePattern, _Response]] | dict[_InputRePattern, _Response]

# The output is bytes unless "encoding" (forwarded to pexpect.spawn) is given, in which case
# it is str. The exit status is None if the child was terminated by a signal.
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: None = None,
    **kwargs: Any,
) -> bytes: ...
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[True] = ...,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: None = None,
    **kwargs: Any,
) -> tuple[bytes, int | None]: ...
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: str,
    **kwargs: Any,
) -> str: ...
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[True] = ...,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: str,
    **kwargs: Any,
) -> tuple[str, int | None]: ...
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: bool = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: None = None,
    **kwargs: Any,
) -> bytes | tuple[bytes, int | None]: ...
@overload
def run(
    command: str,
    timeout: float | None = 30,
    withexitstatus: bool = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    *,
    encoding: str,
    **kwargs: Any,
) -> str | tuple[str, int | None]: ...

# Deprecated: encoding defaults to "utf-8".
@overload
def runu(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    **kwargs: Any,
) -> str: ...
@overload
def runu(
    command: str,
    timeout: float | None = 30,
    withexitstatus: Literal[True] = ...,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    **kwargs: Any,
) -> tuple[str, int | None]: ...
@overload
def runu(
    command: str,
    timeout: float | None = 30,
    withexitstatus: bool = False,
    events: _Events | None = None,
    extra_args: None = None,
    logfile: _Logfile | None = None,
    cwd: FileDescriptorOrPath | None = None,
    env: Mapping[str, str] | None = None,
    **kwargs: Any,
) -> str | tuple[str, int | None]: ...
