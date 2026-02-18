import types
from typing_extensions import Self

class Exitable:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: types.TracebackType | None = None,
    ) -> None: ...

def ExitableWithAliases(*exit_methods: str) -> Exitable: ...
