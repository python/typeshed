from typing import Any, Type
import sys
# Stubs for abc.

# Thesee definitions have special processing in type checker.
class ABCMeta(type):
    def register(cls: "ABCMeta", subclass: Type[Any]) -> None: ...
abstractmethod = object()
abstractproperty = object()

if sys.version_info >= (3, 4):
    class ABC(metaclass=ABCMeta):
        pass
