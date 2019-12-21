
import sys

from _dummy_threading import (
    BoundedSemaphore as BoundedSemaphore,
    Condition as Condition,
    Event as Event,
    Lock as Lock,
    RLock as RLock,
    Semaphore as Semaphore,
    Thread as Thread,
    Timer as Timer,
    __all__ as __all__,
    active_count as active_count,
    current_thread as current_thread,
    currentThread as currentThread,
    enumerate as enumerate,
    local as local,
    setprofile as setprofile,
    settrace as settrace,
    stack_size as stack_size
)

if sys.version_info < (3, 0):
    from _dummy_threading import (
        activeCount as activeCount
    )

if sys.version_info >= (3, 0):
    from _dummy_threading import (
        Barrier as Barrier,
        BrokenBarrierError as BrokenBarrierError,
        TIMEOUT_MAX as TIMEOUT_MAX,
        ThreadError as ThreadError,
        get_ident as get_ident
    )

if sys.version_info >= (3, 8):
    from _dummy_threading import (
        ExceptHookArgs as ExceptHookArgs,
        excepthook as excepthook,
        get_native_id as get_native_id
    )
