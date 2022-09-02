from collections import Counter, defaultdict, deque
from collections.abc import Callable, Generator, Iterable, Sequence
from queue import Queue
from threading import Event as _UninterruptibleEvent
from typing import Optional
from typing_extensions import Literal, TypeAlias

from ._canonical_names import all_modifiers as all_modifiers, sided_modifiers as sided_modifiers
from ._generic import GenericListener as _GenericListener
from ._keyboard_event import KEY_DOWN as KEY_DOWN, KEY_UP as KEY_UP, KeyboardEvent as KeyboardEvent

_Key: TypeAlias = int | str
_ScanCodeList: TypeAlias = list[int] | tuple[int, ...]
_ParseableHotkey: TypeAlias = _Key | list[int | _ScanCodeList] | tuple[int | _ScanCodeList, ...]
_Callback: TypeAlias = Callable[[KeyboardEvent], Optional[bool]] | Callable[[], Optional[bool]]
# Can't use ParamSpecArgs on `args`, only on `*args`
# _P = ParamSpec("_P")
_P: TypeAlias = tuple[object, ...]

version: str

class _Event(_UninterruptibleEvent):
    def wait(self) -> None: ...  # type: ignore[override]  # Actual implementation

def is_modifier(key: _Key | None) -> bool: ...

class _KeyboardListener(_GenericListener):
    transition_table: dict[
        tuple[Literal["free"], Literal["up"], Literal["modifier"]]
        | tuple[Literal["free"], Literal["down"], Literal["modifier"]]
        | tuple[Literal["pending"], Literal["up"], Literal["modifier"]]
        | tuple[Literal["pending"], Literal["down"], Literal["modifier"]]
        | tuple[Literal["suppressed"], Literal["up"], Literal["modifier"]]
        | tuple[Literal["suppressed"], Literal["down"], Literal["modifier"]]
        | tuple[Literal["allowed"], Literal["up"], Literal["modifier"]]
        | tuple[Literal["allowed"], Literal["down"], Literal["modifier"]]
        | tuple[Literal["free"], Literal["up"], Literal["hotkey"]]
        | tuple[Literal["free"], Literal["down"], Literal["hotkey"]]
        | tuple[Literal["pending"], Literal["up"], Literal["hotkey"]]
        | tuple[Literal["pending"], Literal["down"], Literal["hotkey"]]
        | tuple[Literal["suppressed"], Literal["up"], Literal["hotkey"]]
        | tuple[Literal["suppressed"], Literal["down"], Literal["hotkey"]]
        | tuple[Literal["allowed"], Literal["up"], Literal["hotkey"]]
        | tuple[Literal["allowed"], Literal["down"], Literal["hotkey"]]
        | tuple[Literal["free"], Literal["up"], Literal["other"]]
        | tuple[Literal["free"], Literal["down"], Literal["other"]]
        | tuple[Literal["pending"], Literal["up"], Literal["other"]]
        | tuple[Literal["pending"], Literal["down"], Literal["other"]]
        | tuple[Literal["suppressed"], Literal["up"], Literal["other"]]
        | tuple[Literal["suppressed"], Literal["down"], Literal["other"]]
        | tuple[Literal["allowed"], Literal["up"], Literal["other"]]
        | tuple[Literal["allowed"], Literal["down"], Literal["other"]],
        tuple[Literal[False], Literal[True], Literal["free"]]
        | tuple[Literal[False], Literal[False], Literal["pending"]]
        | tuple[Literal[True], Literal[True], Literal["free"]]
        | tuple[Literal[False], Literal[True], Literal["allowed"]]
        | tuple[Literal[False], Literal[False], Literal["free"]]
        | tuple[Literal[False], Literal[False], Literal["suppressed"]]
        | tuple[Literal[False], None, Literal["free"]]
        | tuple[Literal[False], None, Literal["suppressed"]]
        | tuple[Literal[False], None, Literal["allowed"]]
        | tuple[Literal[True], Literal[True], Literal["allowed"]]
        | tuple[Literal[False], Literal[False], Literal["allowed"]],
    ]
    active_modifiers: set[int]
    blocking_hooks: list[_Callback]
    blocking_keys: defaultdict[int, list[_Callback]]
    nonblocking_keys: defaultdict[int, list[_Callback]]
    blocking_hotkeys: defaultdict[tuple[int, ...], list[_Callback]]
    nonblocking_hotkeys: defaultdict[tuple[int, ...], list[_Callback]]
    filtered_modifiers: Counter[int]
    is_replaying: bool
    modifier_states: dict[_Key, str]
    def init(self) -> None: ...
    def pre_process_event(self, event): ...
    def direct_callback(self, event): ...
    def listen(self) -> None: ...

def key_to_scan_codes(key: _ParseableHotkey, error_if_missing: bool = ...) -> tuple[int, ...]: ...
def parse_hotkey(hotkey: _ParseableHotkey) -> tuple[tuple[tuple[int, ...], ...], ...]: ...
def send(hotkey: _ParseableHotkey, do_press: bool = ..., do_release: bool = ...) -> None: ...

press_and_release = send

def press(hotkey: _ParseableHotkey) -> None: ...
def release(hotkey: _ParseableHotkey) -> None: ...

# is_pressed cannot check multi-step hotkeys, so not using _ParseableHotkey

def is_pressed(hotkey: _Key | _ScanCodeList) -> bool: ...
def call_later(fn: Callable[..., None], args: _P = ..., delay: float = ...) -> None: ...
def hook(callback: _Callback, suppress: bool = ..., on_remove: Callable[[], None] = ...) -> Callable[[], None]: ...
def on_press(callback: _Callback, suppress: bool = ...) -> Callable[[], None]: ...
def on_release(callback: _Callback, suppress: bool = ...) -> Callable[[], None]: ...
def hook_key(key: _ParseableHotkey, callback: _Callback, suppress: bool = ...) -> Callable[[], None]: ...
def on_press_key(key: _ParseableHotkey, callback: _Callback, suppress: bool = ...) -> Callable[[], None]: ...
def on_release_key(key: _ParseableHotkey, callback: _Callback, suppress: bool = ...) -> Callable[[], None]: ...
def unhook(remove: _Callback) -> None: ...

unhook_key = unhook

def unhook_all() -> None: ...
def block_key(key: _ParseableHotkey) -> Callable[[], None]: ...

unblock_key = unhook_key

def remap_key(src: _ParseableHotkey, dst: _ParseableHotkey) -> Callable[[], None]: ...

unremap_key = unhook_key

def parse_hotkey_combinations(hotkey: _ParseableHotkey) -> tuple[tuple[tuple[int, ...], ...], ...]: ...
def add_hotkey(
    hotkey: _ParseableHotkey,
    callback: Callable[..., bool | None],
    args: _P = ...,
    suppress: bool = ...,
    timeout: float = ...,
    trigger_on_release: bool = ...,
) -> Callable[[], None]: ...

register_hotkey = add_hotkey

def remove_hotkey(hotkey_or_callback: _ParseableHotkey | _Callback) -> None: ...

unregister_hotkey = remove_hotkey
clear_hotkey = remove_hotkey

def unhook_all_hotkeys() -> None: ...

unregister_all_hotkeys = unhook_all_hotkeys
remove_all_hotkeys = unhook_all_hotkeys
clear_all_hotkeys = unhook_all_hotkeys

def remap_hotkey(
    src: _ParseableHotkey, dst: _ParseableHotkey, suppress: bool = ..., trigger_on_release: bool = ...
) -> Callable[[], None]: ...

unremap_hotkey = remove_hotkey

def stash_state() -> list[int]: ...
def restore_state(scan_codes: Iterable[int]) -> None: ...
def restore_modifiers(scan_codes: Iterable[int]) -> None: ...
def write(text: str, delay: float = ..., restore_state_after: bool = ..., exact: bool | None = ...) -> None: ...
def wait(hotkey: _ParseableHotkey | None = ..., suppress: bool = ..., trigger_on_release: bool = ...) -> None: ...
def get_hotkey_name(names: Iterable[str] | None = ...) -> str: ...
def read_event(suppress: bool = ...) -> KeyboardEvent: ...
def read_key(suppress: bool = ...) -> _Key: ...
def read_hotkey(suppress: bool = ...) -> str: ...
def get_typed_strings(events: Iterable[KeyboardEvent], allow_backspace: bool = ...) -> Generator[str, None, None]: ...
def start_recording(
    recorded_events_queue: Queue[KeyboardEvent] | None = ...,
) -> tuple[Queue[KeyboardEvent], Callable[[], None]]: ...
def stop_recording() -> list[deque[KeyboardEvent]]: ...
def record(until: str = ..., suppress: bool = ..., trigger_on_release: bool = ...) -> list[deque[KeyboardEvent]]: ...
def play(events: Iterable[KeyboardEvent], speed_factor: float = ...) -> None: ...

replay = play

def add_word_listener(
    word: str, callback: _Callback, triggers: Sequence[str] = ..., match_suffix: bool = ..., timeout: float = ...
) -> Callable[[], None]: ...
def remove_word_listener(word_or_handler: str | _Callback) -> None: ...
def add_abbreviation(
    source_text: str, replacement_text: str, match_suffix: bool = ..., timeout: float = ...
) -> Callable[[], None]: ...

register_word_listener = add_word_listener
register_abbreviation = add_abbreviation
remove_abbreviation = remove_word_listener
