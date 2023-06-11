from _typeshed import Incomplete

class ExceptionPexpect(Exception):
    def __init__(self, value: str) -> None: ...
    def get_trace(self): ...

class EOF(ExceptionPexpect): ...
class TIMEOUT(ExceptionPexpect): ...
