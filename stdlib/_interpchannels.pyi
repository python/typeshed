from _collections_abc import Buffer
from _typeshed import structseq
from typing import Any, Final, Literal, TypeVar, final
from typing_extensions import Self, TypeAlias

_T = TypeVar("_T")
_SendType: TypeAlias = Literal["send", "recv", "both"]

class ChannelError(RuntimeError): ...
class ChannelClosedError(ChannelError): ...
class ChannelEmptyError(ChannelError): ...
class ChannelNotEmptyError(ChannelError): ...
class ChannelNotFoundError(ChannelError): ...

@final
class ChannelID:
    @property
    def end(self) -> _SendType: ...
    @property
    def send(self) -> Self: ...
    @property
    def recv(self) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

@final
class ChannelInfo(structseq[Any], tuple[bool, bool, bool, int, int, int, int, int]):
    __match_args__: Final = (
        "open",
        "closing",
        "closed",
        "count",
        "num_interp_send",
        "num_interp_send_released",
        "num_interp_recv",
        "num_interp_recv_released",
    )
    @property
    def open(self) -> bool: ...
    @property
    def closing(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def count(self) -> int: ...  # type: ignore[override]
    @property
    def num_interp_send(self) -> int: ...
    @property
    def num_interp_send_released(self) -> int: ...
    @property
    def num_interp_recv(self) -> int: ...
    @property
    def num_interp_recv_released(self) -> int: ...
    @property
    def num_interp_both(self) -> int: ...
    @property
    def num_interp_both_recv_released(self) -> int: ...
    @property
    def num_interp_both_send_released(self) -> int: ...
    @property
    def num_interp_both_released(self) -> int: ...
    @property
    def recv_associated(self) -> bool: ...
    @property
    def recv_released(self) -> bool: ...
    @property
    def send_associated(self) -> bool: ...
    @property
    def send_released(self) -> bool: ...

def create() -> ChannelID: ...
def destroy(cid: int) -> None: ...
def list_all() -> list[int]: ...
def list_interpreters(cid: int, *, send: bool) -> list[int]: ...
def send(cid: int, obj: object, *, blocking: bool = True, timeout: float | None = None) -> None: ...
def send_buffer(cid: int, obj: Buffer, *, blocking: bool = True, timeout: float | None = None) -> None: ...
def recv(cid: int, default: _T | None = None) -> object | _T: ...
def close(cid: int, *, send: bool = False, recv: bool = False) -> None: ...
def get_info(cid: int) -> ChannelInfo: ...
def release(cid: int, *, send: bool = False, recv: bool = False, force: bool = False) -> None: ...
