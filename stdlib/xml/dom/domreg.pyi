from collections.abc import Callable, Iterable
from _typeshed.xml import DOMImplementation


well_known_implementations: dict[str, str]
registered: dict[str, Callable[[], DOMImplementation]]

def registerDOMImplementation(name: str, factory: Callable[[], DOMImplementation]) -> None: ...
def getDOMImplementation(name: str | None = ..., features: str | Iterable[tuple[str, str | None]] = ...) -> DOMImplementation: ...
