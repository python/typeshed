from typing import Any, ClassVar, Dict, List, Tuple
from typing_extensions import Literal

from docutils import parsers
from docutils.parsers.rst.states import RSTState, RSTStateMachine

class Parser(parsers.Parser):
    config_section_dependencies: ClassVar[Tuple[str, ...]]
    initial_state: Literal["Body", "RFC2822Body"]
    state_classes: Any
    inliner: Any
    def __init__(self, rfc2822: bool = ..., inliner: Any | None = ...) -> None: ...

class DirectiveError(Exception):
    level: Any
    msg: str
    def __init__(self, level: Any, message: str) -> None: ...

class Directive:
    def __init__(
        self,
        name: str,
        arguments: List[object],
        options: Dict[str, object],
        content: List[str],
        lineno: int,
        content_offset: int,
        block_text: str,
        state: RSTState,
        state_machine: RSTStateMachine,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...  # incomplete

def convert_directive_function(directive_fn): ...
