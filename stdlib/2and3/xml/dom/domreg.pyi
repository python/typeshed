from typing import Any, Callable, Dict, Iterable, Optional, Tuple, Union

from ._types import DOMImplementation

well_known_implementations: Dict[str, str]
registered: Dict[str, Callable[[], DOMImplementation]]

def registerDOMImplementation(name: str, factory: Callable[[], DOMImplementation]) -> None: ...
def getDOMImplementation(name: Optional[str], features: Union[str, Iterable[Tuple[str, Optional[str]]]]) -> DOMImplementation: ...
