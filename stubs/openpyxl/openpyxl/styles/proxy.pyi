class StyleProxy:
    def __init__(self, target) -> None: ...
    def __getattr__(self, attr: str): ...
    def __setattr__(self, attr: str, value) -> None: ...
    def __copy__(self): ...
    def __add__(self, other): ...
    def copy(self, **kw): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
