from typing import Any

from stubs.pyvmomi.pyVmomi.vmodl import ManagedObject

def __getattr__(name: str) -> Any: ...  # incomplete

class InvalidArgument(Exception): ...

class ManagedObjectNotFound:
    obj: ManagedObject
