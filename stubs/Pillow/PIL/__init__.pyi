from typing import Any

__version__: str

class UnidentifiedImageError(OSError): ...

# Submodules are missing, __init__.pyi itself is complete.
def __getattr__(__name: str) -> Any: ...  # incomplete
