from _typeshed import Self
from collections.abc import Callable, Iterable, Sequence
from typing import Protocol, TypeVar

from cv2.cv2 import GArrayT, GCompileArg, GOpaqueT, gapi_GKernelPackage, gapi_GNetPackage, gapi_ie_PyParams
from cv2.gapi.streaming import queue_capacity

class _KernelCls(Protocol):
    id: str
    outMeta: object
    on: staticmethod[tuple[type, ...] | type]

_K = TypeVar("_K", bound=_KernelCls)
_F = TypeVar("_F", bound=Callable[..., object])
_A = TypeVar("_A")

def register(mname: str) -> Callable[[_F], _F]: ...
def networks(*args: gapi_ie_PyParams) -> gapi_GNetPackage: ...
def compile_args(*args: gapi_GKernelPackage | gapi_GNetPackage | queue_capacity) -> list[GCompileArg]: ...
def GIn(*args: _A) -> list[_A]: ...
def GOut(*args: _A) -> list[_A]: ...
def gin(*args: _A) -> list[_A]: ...
def descr_of(*args: _A) -> list[_A]: ...

class GOpaque:
    def __new__(cls, argtype: int) -> GOpaqueT: ...  # type: ignore[misc]

    class Bool:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Int:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Double:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Float:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class String:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Point:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Point2f:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Size:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Rect:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Prim:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

    class Any:
        def __new__(self) -> GOpaqueT: ...  # type: ignore[misc]

class GArray:
    def __new__(cls, argtype: int) -> GArrayT: ...  # type: ignore[misc]

    class Bool:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Int:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Double:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Float:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class String:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Point:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Point2f:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Size:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Rect:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Scalar:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Mat:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class GMat:
        def __new__(self) -> GArrayT: ...  # type: ignore[misc]

    class Prim:
        def __new__(self: Self) -> Self: ...

    class Any:
        def __new__(self: Self) -> Self: ...

def op(op_id: str, in_types: Sequence[type], out_types: Iterable[type]) -> Callable[[_K], _K]: ...
def kernel(op_cls: _KernelCls) -> Callable[[_K], _K]: ...
