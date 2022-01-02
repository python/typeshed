import threading

_global_lock: threading.Lock
_marker: object

class _LoopBoundMixin: ...
