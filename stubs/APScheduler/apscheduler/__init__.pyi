from _typeshed import Incomplete

release: str
version_info: tuple[int | str, ...]
version: str
__version__: str

def __getattr__(name: str) -> Incomplete: ...
