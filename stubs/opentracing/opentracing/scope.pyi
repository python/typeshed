class Scope:
    def __init__(self, manager, span) -> None: ...
    @property
    def span(self): ...
    @property
    def manager(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
