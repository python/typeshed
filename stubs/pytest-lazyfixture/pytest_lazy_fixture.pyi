from typing import Any, Iterable, List

class LazyFixture:
    name: str
    def __init__(self, name: str) -> None: ...
    def __eq__(self, other: LazyFixture) -> bool: ...

def lazy_fixture(names: str | Iterable[str]) -> LazyFixture | List[LazyFixture]: ...
def is_lazy_fixture(val: Any) -> bool: ...
def pytest_configure() -> None: ...
def __getattr__(name: str) -> Any: ...  # incomplete
