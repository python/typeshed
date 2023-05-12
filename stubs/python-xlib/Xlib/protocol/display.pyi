from _typeshed import _BufferWithLen
from socket import socket
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from Xlib import error
from Xlib._typing import ErrorHandler
from Xlib.display import _ResourceBaseClass, _ResourceBaseClassesType
from Xlib.protocol import rq
from Xlib.support import lock
from Xlib.xobject import colormap, cursor, drawable, fontable, resource

_T = TypeVar("_T")

class bytesview:
    view: memoryview
    @overload
    def __init__(self, data: bytes | bytesview, offset: int, size: int) -> None: ...
    @overload
    def __init__(self, data: _BufferWithLen, offset: int = 0, size: int | None = None) -> None: ...
    @overload
    def __getitem__(self, key: slice[Any, Any, Any]) -> bytes: ...
    @overload
    def __getitem__(self, key: int) -> int: ...
    def __len__(self) -> int: ...

class Display:
    extension_major_opcodes: dict[str, int]
    error_classes: dict[int, type[error.XError]]
    event_classes: dict[int, type[rq.Event] | dict[int, type[rq.Event]]]
    resource_classes: _ResourceBaseClassesType | None
    display_name: str
    default_screen: int
    socket: socket
    socket_error_lock: lock._DummyLock
    socket_error: Exception | None
    event_queue_read_lock: lock._DummyLock
    event_queue_write_lock: lock._DummyLock
    event_queue: list[rq.Event]
    request_queue_lock: lock._DummyLock
    request_serial: int
    request_queue: list[tuple[rq.Request | rq.ReplyRequest | ConnectionSetupRequest, int]]
    send_recv_lock: lock._DummyLock
    send_active: int
    recv_active: int
    event_waiting: int
    event_wait_lock: lock._DummyLock
    request_waiting: int
    request_wait_lock: lock._DummyLock
    recv_buffer_size: int
    sent_requests: list[rq.Request | rq.ReplyRequest | ConnectionSetupRequest]
    recv_packet_len: int
    data_send: bytes
    data_recv: bytes
    data_sent_bytes: int
    resource_id_lock: lock._DummyLock
    resource_ids: dict[int, None]
    last_resource_id: int
    error_handler: ErrorHandler[object] | None
    big_endian: bool
    info: ConnectionSetupRequest
    def __init__(self, display: str | None = None) -> None: ...
    def get_display_name(self) -> str: ...
    def get_default_screen(self) -> int: ...
    def fileno(self) -> int: ...
    def next_event(self) -> rq.Event: ...
    def pending_events(self) -> int: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def set_error_handler(self, handler: ErrorHandler[object] | None) -> None: ...
    def allocate_resource_id(self) -> int: ...
    def free_resource_id(self, rid: int) -> None: ...
    @overload
    def get_resource_class(self, class_name: Literal["resource"], default: object = None) -> type[resource.Resource]: ...
    @overload
    def get_resource_class(self, class_name: Literal["drawable"], default: object = None) -> type[drawable.Drawable]: ...
    @overload
    def get_resource_class(self, class_name: Literal["window"], default: object = None) -> type[drawable.Window]: ...
    @overload
    def get_resource_class(self, class_name: Literal["pixmap"], default: object = None) -> type[drawable.Pixmap]: ...
    @overload
    def get_resource_class(self, class_name: Literal["fontable"], default: object = None) -> type[fontable.Fontable]: ...
    @overload
    def get_resource_class(self, class_name: Literal["font"], default: object = None) -> type[fontable.Font]: ...
    @overload
    def get_resource_class(self, class_name: Literal["gc"], default: object = None) -> type[fontable.GC]: ...
    @overload
    def get_resource_class(self, class_name: Literal["colormap"], default: object = None) -> type[colormap.Colormap]: ...
    @overload
    def get_resource_class(self, class_name: Literal["cursor"], default: object) -> type[cursor.Cursor]: ...
    @overload
    def get_resource_class(self, class_name: str, default: _T) -> type[_ResourceBaseClass] | _T: ...
    @overload
    def get_resource_class(self, class_name: str, default: None = None) -> type[_ResourceBaseClass] | None: ...
    def set_extension_major(self, extname: str, major: int) -> None: ...
    def get_extension_major(self, extname: str) -> int: ...
    def add_extension_event(self, code: int, evt: type[rq.Event], subcode: int | None = None) -> None: ...
    def add_extension_error(self, code: int, err: type[error.XError]) -> None: ...
    def check_for_error(self) -> None: ...
    def send_request(self, request: rq.Request | rq.ReplyRequest | ConnectionSetupRequest, wait_for_response: bool) -> None: ...
    def close_internal(self, whom: object) -> None: ...
    def send_and_recv(self, flush: bool = False, event: bool = False, request: int | None = None, recv: bool = False) -> None: ...
    def parse_response(self, request: int) -> bool: ...
    def parse_error_response(self, request: int) -> bool: ...
    def default_error_handler(self, err: object) -> None: ...
    def parse_request_response(self, request: int) -> bool: ...
    def parse_event_response(self, etype: int) -> None: ...
    def get_waiting_request(self, sno: int) -> rq.ReplyRequest | ConnectionSetupRequest | None: ...
    def get_waiting_replyrequest(self) -> rq.ReplyRequest | ConnectionSetupRequest: ...
    def parse_connection_setup(self) -> bool: ...

PixmapFormat: rq.Struct
VisualType: rq.Struct
Depth: rq.Struct
Screen: rq.Struct

class ConnectionSetupRequest(rq.GetAttrData):
    def __init__(self, display: Display, *args: object, **keys: object) -> None: ...
