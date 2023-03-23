from _typeshed import Incomplete

def bundle_resources(resources): ...
def rollup_resources(resources): ...
def sort_resources(resources): ...

class Inclusion:
    needed: Incomplete
    resources: Incomplete
    def __init__(
        self,
        needed,
        resources: Incomplete | None = ...,
        compile: bool = ...,
        bundle: bool = ...,
        mode: Incomplete | None = ...,
        rollup: bool = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def render(self): ...
