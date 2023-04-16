from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import TypeVar, overload
from typing_extensions import Literal

from .engine.result import ResultMetaData

_T = TypeVar("_T")
_T_co = TypeVar("_T_co")
# _KS = TypeVar("_KS", Literal[0], Literal[1], Literal[2, 3], int)

class BaseRow(Iterable[_T_co]):
    @overload
    def __init__(
        self,
        __parent: ResultMetaData,
        __processors: Iterable[Callable[[_T_co], Incomplete] | None] | None,
        __keymap: dict[Incomplete, Incomplete],
        __key_style: Literal[1],
        __row: Sequence[_T_co],
    ) -> None: ...
    @overload
    def __init__(
        self,
        __parent: ResultMetaData | None,
        __processors: Iterable[Callable[[_T_co], Incomplete]] | None,
        __keymap: dict[Incomplete, Incomplete],
        __key_style: int,
        __row: Sequence[_T_co],
    ) -> None: ...
    def __reduce__(self): ...
    def __iter__(self) -> Iterator[_T_co]: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __getattr__(self, name: str) -> _T_co: ...
    @overload
    def __getitem__(self, index: slice) -> tuple[_T_co, ...]: ...  # type: ignore[misc]
    @overload
    def __getitem__(self, index: object) -> _T_co: ...

# TODO: Keeping BaseRow non-Generic for now to reduce the amount of changes seen by mypy_primer
# Change to the implementation below in a different PR
# class BaseRow(Iterable[_T_co], Generic[_T_co, _KS]):
#     @overload
#     def __init__(
#         self
#         __parent: ResultMetaData,
#         __processors: Iterable[Callable[[Self], Incomplete]] | None,
#         __keymap: dict[Incomplete, Incomplete],
#         __key_style: Literal[1],
#         __row: Sequence[_T_co],
#     ) -> None: ...
#     @overload
#     def __init__(
#         self
#         __parent: ResultMetaData | None,
#         __processors: Iterable[Callable[[Self], Incomplete]] | None,
#         __keymap: dict[Incomplete, Incomplete],
#         __key_style: _KS,
#         __row: Sequence[_T_co],
#     ) -> None: ...
#     def __reduce__(self): ...
#     def __iter__(self) -> Iterator[_T_co]: ...
#     def __len__(self) -> int: ...
#     def __hash__(self) -> int: ...
#     def __getattr__(self, name: str) -> _T_co: ...
#     ###
#     # __key_style = 0
#     ###
#     @overload
#     def __getitem__(self: BaseRow[_T_co, Literal[0]], index: int) -> _T_co: ...
#     @overload
#     def __getitem__(self: BaseRow[_T_co, Literal[0]], index: slice) -> tuple[_T_co, ...]: ...  # type: ignore[misc]
#     # Needed because the int overload would assume index=object|str is aceptable with __key_style=0
#     @overload
#     def __getitem__(  # type: ignore[misc]
#         self: BaseRow[_T_co, Literal[0]], index: object
#     ) -> _T_co | tuple[_T_co, ...] | NoReturn: ...
#     ###
#     # __key_style = 1
#     ###
#     # Needed because next overload is "object & Not[int | slice]"
#     @overload
#     def __getitem__(self: BaseRow[_T_co, Literal[1]], index: int | slice) -> NoReturn: ...
#     @overload
#     def __getitem__(self: BaseRow[_T_co, Literal[1]], index: object) -> _T_co: ...  # type: ignore[misc]
#     ###
#     # __key_style = 3 | 4
#     ###
#     # General fallbacks if _KS evaluates to int
#     @overload
#     def __getitem__(self: BaseRow[_T_co, int], index: slice) -> tuple[_T_co, ...]: ...  # type: ignore[misc]
#     @overload
#     def __getitem__(self: BaseRow[_T_co, int], index: object) -> _T_co: ...

def safe_rowproxy_reconstructor(__cls: type[_T], __state: dict[str, Incomplete]) -> _T: ...
