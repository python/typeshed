from typing import AnyStr, Callable, FrozenSet, Generic, Iterator, NoReturn, TypeVar, overload

_T = TypeVar("_T")

class Pattern(Generic[AnyStr]):

    pattern: AnyStr
    flags: int
    groups: int
    groupindex: dict[str, int]
    named_lists: dict[str, FrozenSet[AnyStr]]
    def search(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> Match[AnyStr] | None: ...
    def match(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> Match[AnyStr] | None: ...
    def fullmatch(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> Match[AnyStr] | None: ...
    def split(
        self, string: AnyStr, maxsplit: int = ..., concurrent: bool | None = ..., timeout: int | None = ...
    ) -> list[AnyStr]: ...
    def splititer(
        self, string: AnyStr, maxsplit: int = ..., concurrent: bool | None = ..., timeout: int | None = ...
    ) -> Splitter[AnyStr]: ...
    def findall(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        overlapped: bool = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> list[AnyStr] | list[tuple[AnyStr, ...]]: ...
    def finditer(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        overlapped: bool = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> Scanner[AnyStr]: ...
    def sub(
        self,
        repl: AnyStr | Callable[[Match[AnyStr]], AnyStr],
        string: AnyStr,
        count: int = ...,
        flags: int = ...,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> AnyStr: ...
    def subf(
        self,
        format: AnyStr | Callable[[Match[AnyStr]], AnyStr],
        string: AnyStr,
        count: int = ...,
        flags: int = ...,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> AnyStr: ...
    def subn(
        self,
        repl: AnyStr | Callable[[Match[AnyStr]], AnyStr],
        string: AnyStr,
        count: int = ...,
        flags: int = ...,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> tuple[AnyStr, int]: ...
    def subfn(
        self,
        format: AnyStr | Callable[[Match[AnyStr]], AnyStr],
        string: AnyStr,
        count: int = ...,
        flags: int = ...,
        pos: int | None = ...,
        endpos: int | None = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> tuple[AnyStr, int]: ...
    def scanner(
        self,
        string: AnyStr,
        pos: int | None = ...,
        endpos: int | None = ...,
        overlapped: bool = ...,
        concurrent: bool | None = ...,
        timeout: int | None = ...,
    ) -> Scanner[AnyStr]: ...

class Match(Generic[AnyStr]):

    re: Pattern[AnyStr]
    string: AnyStr
    pos: int
    endpos: int
    partial: bool
    regs: tuple[tuple[int, int], ...]
    fuzzy_counts: tuple[int, int, int]
    fuzzy_changes: tuple[list[int], list[int], list[int]]
    lastgroup: str | None
    lastindex: int | None
    @overload
    def group(self, __group: int | str = ...) -> AnyStr | None: ...
    @overload
    def group(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[AnyStr | None, ...]: ...
    @overload
    def groups(self, default: None = ...) -> tuple[AnyStr | None, ...]: ...
    @overload
    def groups(self, default: _T) -> tuple[AnyStr | _T, ...]: ...
    @overload
    def groupdict(self, default: None = ...) -> dict[str, AnyStr | None]: ...
    @overload
    def groupdict(self, default: _T) -> dict[str, AnyStr | _T]: ...
    @overload
    def span(self, __group: int | str = ...) -> tuple[int, int]: ...
    @overload
    def span(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[tuple[int, int], ...]: ...
    @overload
    def spans(self, __group: int | str = ...) -> list[tuple[int, int]]: ...
    @overload
    def spans(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[list[tuple[int, int]], ...]: ...
    @overload
    def start(self, __group: int | str = ...) -> int: ...
    @overload
    def start(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[int, ...]: ...
    @overload
    def starts(self, __group: int | str = ...) -> list[int]: ...
    @overload
    def starts(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[list[int], ...]: ...
    @overload
    def end(self, __group: int | str = ...) -> int: ...
    @overload
    def end(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[int, ...]: ...
    @overload
    def ends(self, __group: int | str = ...) -> list[int]: ...
    @overload
    def ends(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[list[int], ...]: ...
    def expand(self, template: AnyStr) -> AnyStr: ...
    def expandf(self, format: AnyStr) -> AnyStr: ...
    @overload
    def captures(self, __group: int | str = ...) -> list[AnyStr]: ...
    @overload
    def captures(self, __group1: int | str, __group2: int | str, *groups: int | str) -> tuple[list[AnyStr], ...]: ...
    def capturesdict(self) -> dict[str, list[AnyStr]]: ...
    def detach_string(self) -> NoReturn: ...

class Splitter(Generic[AnyStr]):

    pattern: Pattern[AnyStr]
    def __iter__(self) -> Iterator[AnyStr]: ...
    def __next__(self) -> AnyStr: ...
    def split(self) -> AnyStr | None: ...

class Scanner(Generic[AnyStr]):

    pattern: Pattern[AnyStr]
    def __iter__(self) -> Iterator[Match[AnyStr]]: ...
    def __next__(self) -> Match[AnyStr]: ...
    def match(self) -> Match[AnyStr] | None: ...
    def search(self) -> Match[AnyStr] | None: ...
