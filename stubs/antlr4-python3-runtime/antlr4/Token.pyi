from _typeshed import Incomplete

class Token:
    INVALID_TYPE: int
    EPSILON: int
    MIN_USER_TOKEN_TYPE: int
    EOF: int
    DEFAULT_CHANNEL: int
    HIDDEN_CHANNEL: int
    source: Incomplete
    type: Incomplete
    channel: Incomplete
    start: Incomplete
    stop: Incomplete
    tokenIndex: Incomplete
    line: Incomplete
    column: Incomplete
    def __init__(self) -> None: ...
    @property
    def text(self) -> Incomplete: ...
    @text.setter
    def text(self, text: str) -> Incomplete: ...
    def getTokenSource(self) -> Incomplete: ...
    def getInputStream(self) -> Incomplete: ...

class CommonToken(Token):
    EMPTY_SOURCE: Incomplete
    source: Incomplete
    type: Incomplete
    channel: Incomplete
    start: Incomplete
    stop: Incomplete
    tokenIndex: int
    line: Incomplete
    column: Incomplete
    def __init__(
        self,
        source: tuple[Incomplete, Incomplete] = ...,
        type: int | None = None,
        channel: int = ...,
        start: int = ...,
        stop: int = ...,
    ) -> None: ...
    def clone(self) -> Incomplete: ...
    @property
    def text(self) -> Incomplete: ...
    @text.setter
    def text(self, text: str) -> Incomplete: ...
