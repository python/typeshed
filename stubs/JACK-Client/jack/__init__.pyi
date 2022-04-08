from _typeshed import Self
from typing import Any, Callable, Generator, Iterable, Iterator, Sequence, overload

_NDArray = Any  # FIXME: no typings for numpy arrays

class _JackPositionT: ...

class _CBufferType:
    @overload
    def __getitem__(self, key: int) -> str: ...
    @overload
    def __getitem__(self, key: slice) -> bytes: ...
    @overload
    def __setitem__(self, key: int, val: str) -> None: ...
    @overload
    def __setitem__(self, key: slice, val: bytes) -> None: ...
    def __len__(self) -> int: ...
    def __bytes__(self) -> bytes: ...

STOPPED: int
ROLLING: int
STARTING: int
NETSTARTING: int
PROPERTY_CREATED: int
PROPERTY_CHANGED: int
PROPERTY_DELETED: int
POSITION_BBT: int
POSITION_TIMECODE: int
POSITION_BBT_FRAME_OFFSET: int
POSITION_AUDIO_VIDEO_RATIO: int
POSITION_VIDEO_FRAME_OFFSET: int

class JackError(Exception): ...

class JackErrorCode(JackError):
    def __init__(self, message: str, code: int) -> None: ...
    message: str = ...
    code: int = ...

class JackOpenError(JackError):
    def __init__(self, name: str, status: Status) -> None: ...
    name: str = ...
    status: Status = ...

class Client:
    def __init__(
        self,
        name: str,
        use_exact_name: bool = ...,
        no_start_server: bool = ...,
        servername: str | None = ...,
        session_id: str | None = ...,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def uuid(self) -> str: ...
    @property
    def samplerate(self) -> int: ...
    @property
    def blocksize(self) -> int: ...
    @blocksize.setter
    def blocksize(self, blocksize: int) -> None: ...
    @property
    def status(self) -> Status: ...
    @property
    def realtime(self) -> bool: ...
    @property
    def frames_since_cycle_start(self) -> int: ...
    @property
    def frame_time(self) -> int: ...
    @property
    def last_frame_time(self) -> int: ...
    @property
    def inports(self) -> Ports: ...
    @property
    def outports(self) -> Ports: ...
    @property
    def midi_inports(self) -> Ports: ...
    @property
    def midi_outports(self) -> Ports: ...
    def owns(self, port: str | Port) -> bool: ...
    def activate(self) -> None: ...
    def deactivate(self, ignore_errors: bool = ...) -> None: ...
    def cpu_load(self) -> float: ...
    def close(self, ignore_errors: bool = ...) -> None: ...
    def connect(self, source: str | Port, destination: str | Port) -> None: ...
    def disconnect(self, source: str | Port, destination: str | Port) -> None: ...
    def transport_start(self) -> None: ...
    def transport_stop(self) -> None: ...
    @property
    def transport_state(self) -> TransportState: ...
    @property
    def transport_frame(self) -> int: ...
    @transport_frame.setter
    def transport_frame(self, frame: int) -> None: ...
    def transport_locate(self, frame: int) -> None: ...
    def transport_query(self) -> tuple[TransportState, dict[str, Any]]: ...
    def transport_query_struct(self) -> tuple[TransportState, _JackPositionT]: ...
    def transport_reposition_struct(self, position: _JackPositionT) -> None: ...  # TODO
    def set_sync_timeout(self, timeout: int) -> None: ...
    def set_freewheel(self, onoff: bool) -> None: ...
    def set_shutdown_callback(self, callback: Callable[[Status, str], None]) -> None: ...
    def set_process_callback(self, callback: Callable[[int], None]) -> None: ...
    def set_freewheel_callback(self, callback: Callable[[bool], None]) -> None: ...
    def set_blocksize_callback(self, callback: Callable[[int], None]) -> None: ...
    def set_samplerate_callback(self, callback: Callable[[int], None]) -> None: ...
    def set_client_registration_callback(self, callback: Callable[[str, bool], None]) -> None: ...
    def set_port_registration_callback(
        self, callback: Callable[[Port, bool], None] | None = ..., only_available: bool = ...
    ) -> None: ...
    def set_port_connect_callback(
        self, callback: Callable[[Port, Port, bool], None] | None = ..., only_available: bool = ...
    ) -> None: ...
    def set_port_rename_callback(
        self, callback: Callable[[Port, str, str], None] | None = ..., only_available: bool = ...
    ) -> None: ...
    def set_graph_order_callback(self, callback: Callable[[], None]) -> None: ...
    def set_xrun_callback(self, callback: Callable[[float], None]) -> None: ...
    def set_sync_callback(self, callback: Callable[[int, _JackPositionT], None] | None) -> None: ...
    def release_timebase(self) -> None: ...
    def set_timebase_callback(
        self, callback: Callable[[int, int, _JackPositionT, bool], None] | None = ..., conditional: bool = ...
    ) -> bool: ...
    def set_property_change_callback(self, callback: Callable[[int, str, int], None]) -> None: ...
    def get_uuid_for_client_name(self, name: str) -> str: ...
    def get_client_name_by_uuid(self, uuid: str) -> str: ...
    def get_port_by_name(self, name: str) -> Port: ...
    def get_all_connections(self, port: Port) -> list[Port]: ...
    def get_ports(
        self,
        name_pattern: str = ...,
        is_audio: bool = ...,
        is_midi: bool = ...,
        is_input: bool = ...,
        is_output: bool = ...,
        is_physical: bool = ...,
        can_monitor: bool = ...,
        is_terminal: bool = ...,
    ) -> list[Port]: ...
    def set_property(self, subject: int | str, key: str, value: str | bytes, type: str = ...) -> None: ...
    def remove_property(self, subject: int | str, key: str) -> None: ...
    def remove_properties(self, subject: int | str) -> int: ...
    def remove_all_properties(self) -> None: ...

class Port:
    def __init__(self, port_ptr: Any, client: Client) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def shortname(self) -> str: ...
    @shortname.setter
    def shortname(self, shortname: str) -> None: ...
    @property
    def aliases(self) -> list[str]: ...
    def set_alias(self, alias: str) -> None: ...
    def unset_alias(self, alias: str) -> None: ...
    @property
    def uuid(self) -> str: ...
    @property
    def is_audio(self) -> bool: ...
    @property
    def is_midi(self) -> bool: ...
    @property
    def is_input(self) -> bool: ...
    @property
    def is_output(self) -> bool: ...
    @property
    def is_physical(self) -> bool: ...
    @property
    def can_monitor(self) -> bool: ...
    @property
    def is_terminal(self) -> bool: ...
    def request_monitor(self, onoff: bool) -> None: ...

class MidiPort(Port):
    is_audio: bool = ...
    is_midi: bool = ...

class OwnPort(Port):
    @property
    def number_of_connections(self) -> int: ...
    @property
    def connections(self) -> list[Port]: ...
    def is_connected_to(self, port: str | Port) -> bool: ...
    def connect(self, port: str | Port) -> None: ...
    def disconnect(self, other: str | Port | None = ...) -> None: ...
    def unregister(self) -> None: ...
    def get_buffer(self) -> _CBufferType: ...
    def get_array(self) -> _NDArray: ...

class OwnMidiPort(MidiPort, OwnPort):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_buffer(self) -> _CBufferType: ...
    def get_array(self) -> _NDArray: ...
    @property
    def max_event_size(self) -> int: ...
    @property
    def lost_midi_events(self) -> int: ...
    def incoming_midi_events(self) -> Generator[tuple[int, _CBufferType], None, None]: ...
    def clear_buffer(self) -> None: ...
    def write_midi_event(self, time: int, event: bytes | Sequence[int] | _CBufferType) -> None: ...
    def reserve_midi_event(self, time: int, size: int) -> _CBufferType: ...

class Ports:
    def __init__(self, client: Client, porttype: Any, flag: Any) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, name: str) -> Port: ...
    def __iter__(self) -> Iterator[Port]: ...
    def register(self, shortname: str, is_terminal: bool = ..., is_physical: bool = ...) -> Port: ...
    def clear(self) -> None: ...

class RingBuffer:
    def __init__(self, size: int) -> None: ...
    @property
    def write_space(self) -> int: ...
    def write(self, data: bytes | Iterable[int] | _CBufferType) -> int: ...
    @property
    def write_buffers(self) -> tuple[_CBufferType, _CBufferType]: ...
    def write_advance(self, size: int) -> None: ...
    @property
    def read_space(self) -> int: ...
    def read(self, size: int) -> _CBufferType: ...
    def peek(self, size: int) -> _CBufferType: ...
    @property
    def read_buffers(self) -> tuple[_CBufferType, _CBufferType]: ...
    def read_advance(self, size: int) -> None: ...
    def mlock(self) -> None: ...
    def reset(self, size: int | None = ...) -> None: ...
    @property
    def size(self) -> int: ...

class Status:
    def __init__(self, code: int) -> None: ...
    @property
    def failure(self) -> bool: ...
    @property
    def invalid_option(self) -> bool: ...
    @property
    def name_not_unique(self) -> bool: ...
    @property
    def server_started(self) -> bool: ...
    @property
    def server_failed(self) -> bool: ...
    @property
    def server_error(self) -> bool: ...
    @property
    def no_such_client(self) -> bool: ...
    @property
    def load_failure(self) -> bool: ...
    @property
    def init_failure(self) -> bool: ...
    @property
    def shm_failure(self) -> bool: ...
    @property
    def version_error(self) -> bool: ...
    @property
    def backend_error(self) -> bool: ...
    @property
    def client_zombie(self) -> bool: ...

class TransportState:
    def __init__(self, code: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class CallbackExit(Exception): ...

def get_property(subject: int | str, key: str) -> tuple[bytes, str] | None: ...
def get_properties(subject: int | str) -> dict[str, tuple[bytes, str]]: ...
def get_all_properties() -> dict[str, dict[str, tuple[bytes, str]]]: ...
def position2dict(pos: _JackPositionT) -> dict[str, Any]: ...
def version() -> tuple[int, int, int, int]: ...
def version_string() -> str: ...
def client_name_size() -> int: ...
def port_name_size() -> int: ...
def set_error_function(callback: Callable[[str], None] | None = ...) -> None: ...
def set_info_function(callback: Callable[[str], None] | None = ...) -> None: ...
def client_pid(name: str) -> int: ...
