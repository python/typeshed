from _typeshed import Incomplete

from tensorflow.python.trackable.base import Trackable

class _ResourceMetaclass(type): ...

# Internal type that is commonly used as a base class
# and some public apis the signature needs it.
class CapturableResource(Trackable, metaclass=_ResourceMetaclass): ...

def __getattr__(name: str) -> Incomplete: ...
