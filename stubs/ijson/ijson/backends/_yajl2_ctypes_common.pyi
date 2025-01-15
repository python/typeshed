from _typeshed import Incomplete

C_EMPTY: Incomplete
C_INT: Incomplete
C_LONG: Incomplete
C_LONGLONG: Incomplete
C_DOUBLE: Incomplete
C_STR: Incomplete
YAJL_OK: int
YAJL_CANCELLED: int
YAJL_INSUFFICIENT_DATA: int
YAJL_ERROR: int

def get_yajl(version): ...
def make_callbaks(send, use_float, yajl_version): ...
def yajl_get_error(yajl, handle, buffer): ...
