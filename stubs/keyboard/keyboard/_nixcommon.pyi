from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from io import BufferedReader, BufferedWriter
from queue import Queue
from typing import NamedTuple
from typing_extensions import Literal

event_bin_format: Literal["llHHI"]
EV_SYN: Literal[0]
EV_KEY: Literal[1]
EV_REL: Literal[2]
EV_ABS: Literal[3]
EV_MSC: Literal[4]

def make_uinput() -> BufferedWriter: ...

class EventDevice:
    path: str
    def __init__(self, path: str) -> None: ...
    @property
    def input_file(self) -> BufferedReader: ...
    @property
    def output_file(self) -> BufferedWriter: ...
    def read_event(self) -> tuple[float, Incomplete, Incomplete, Incomplete, str]: ...
    def write_event(self, type, code, value) -> None: ...

class AggregatedEventDevice:
    event_queue: Queue[tuple[float, Incomplete, Incomplete, Incomplete, str]]
    devices: Sequence[EventDevice]
    output: EventDevice
    def __init__(self, devices: Sequence[EventDevice], output: EventDevice | None = ...) -> None: ...
    def read_event(self) -> EventDevice: ...
    def write_event(self, type, code, value) -> None: ...

class DeviceDescription(NamedTuple):
    event_file: str
    is_mouse: bool
    is_keyboard: bool

device_pattern: str

def list_devices_from_proc(type_name: str) -> Generator[EventDevice, None, None]: ...
def list_devices_from_by_id(name_suffix: str, by_id: bool = ...) -> Generator[EventDevice, None, None]: ...
def aggregate_devices(type_name: str) -> AggregatedEventDevice | EventDevice: ...
def ensure_root() -> None: ...
