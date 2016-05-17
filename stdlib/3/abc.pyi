from typing import Any
# Stubs for abc.

# Thesee definitions have special processing in type checker.
class ABCMeta:
    def register(cls: "ABCMeta", subclass: Any) -> None: ...
abstractmethod = object()
abstractproperty = object()
