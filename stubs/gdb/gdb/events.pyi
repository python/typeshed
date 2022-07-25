from collections.abc import Callable, Sequence

import gdb

class ThreadEvent:
    inferior_thread: gdb.InferiorThread

class ContinueEvent(ThreadEvent): ...

class ContinueEventRegistry:
    def connect(self, __object: Callable[[ContinueEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[ContinueEvent], Any]) -> None: ...

cont: ContinueEventRegistry

class ExitedEvent:
    exit_code: int
    inferior: gdb.Inferior

class ExitedEventRegistry:
    def connect(self, __object: Callable[[ExitedEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[ExitedEvent], Any]) -> None: ...

exited: ExitedEventRegistry

class StopEvent(ThreadEvent):
    stop_signal: str

class BreakpointEvent(StopEvent):
    breakpoints: Sequence[gdb.Breakpoint]
    breakpoint: gdb.Breakpoint

class StopEventRegistry:
    def connect(self, __object: Callable[[StopEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[StopEvent], Any]) -> None: ...

stop: StopEventRegistry

class NewObjFileEvent:
    new_objfile: gdb.Objfile

class NewObjFileEventRegistry:
    def connect(self, __object: Callable[[NewObjFileEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[NewObjFileEvent], Any]) -> None: ...

new_objfile: NewObjFileEventRegistry

class ClearObjFilesEvent:
    progspace: gdb.Progspace

class ClearObjFilesEventRegistry:
    def connect(self, __object: Callable[[ClearObjFilesEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[ClearObjFilesEvent], Any]) -> None: ...

clear_objfiles: ClearObjFilesEventRegistry

class InferiorCallEvent: ...

class InferiorCallPreEvent(InferiorCallEvent):
    ptid: gdb.InferiorThread
    address: gdb.Value

class InferiorCallPostEvent(InferiorCallEvent):
    ptid: gdb.InferiorThread
    address: gdb.Value

class InferiorCallEventRegistry:
    def connect(self, __object: Callable[[InferiorCallEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[InferiorCallEvent], Any]) -> None: ...

inferior_call: InferiorCallEventRegistry

class MemoryChangedEvent:
    address: gdb.Value
    length: int

class MemoryChangedEventRegistry:
    def connect(self, __object: Callable[[MemoryChangedEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[MemoryChangedEvent], Any]) -> None: ...

memory_changed: MemoryChangedEventRegistry

class RegisterChangedEvent:
    frame: gdb.Frame
    regnum: str

class RegisterChangedEventRegistry:
    def connect(self, __object: Callable[[RegisterChangedEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[RegisterChangedEvent], Any]) -> None: ...

register_changed: RegisterChangedEventRegistry

class BreakpointEventRegistry:
    def connect(self, __object: Callable[[gdb.Breakpoint], Any]) -> None: ...
    def disconnect(self, __object: Callable[[gdb.Breakpoint], Any]) -> None: ...

breakpoint_created: BreakpointEventRegistry
breakpoint_modified: BreakpointEventRegistry
breakpoint_deleted: BreakpointEventRegistry

class BeforePromptEventRegistry:
    def connect(self, __object: Callable[[], Any]) -> None: ...
    def disconnect(self, __object: Callable[[], Any]) -> None: ...

before_prompt: BeforePromptEventRegistry

class NewInferiorEvent:
    inferior: gdb.Inferior

class NewInferiorEventRegistry:
    def connect(self, __object: Callable[[NewInferiorEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[NewInferiorEvent], Any]) -> None: ...

new_inferior: NewInferiorEventRegistry

class InferiorDeletedEvent:
    inferior: gdb.Inferior

class InferiorDeletedEventRegistry:
    def connect(self, __object: Callable[[InferiorDeletedEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[InferiorDeletedEvent], Any]) -> None: ...

inferior_deleted: InferiorDeletedEventRegistry

class NewThreadEvent(ThreadEvent): ...

class NewThreadEventRegistry:
    def connect(self, __object: Callable[[NewThreadEvent], Any]) -> None: ...
    def disconnect(self, __object: Callable[[NewThreadEvent], Any]) -> None: ...

new_thread: NewThreadEventRegistry
