from _typeshed import Incomplete

from .core import Construct, Subconstruct

class Probe(Construct):
    counter: int
    printname: Incomplete
    show_stream: Incomplete
    show_context: Incomplete
    show_stack: Incomplete
    stream_lookahead: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        show_stream: bool = True,
        show_context: bool = True,
        show_stack: bool = True,
        stream_lookahead: int = 100,
    ) -> None: ...
    def printout(self, stream, context) -> None: ...

class Debugger(Subconstruct):
    def handle_exc(self, msg: Incomplete | None = None) -> None: ...
