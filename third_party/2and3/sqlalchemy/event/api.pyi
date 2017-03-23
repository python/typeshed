# Stubs for sqlalchemy.event.api (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .base import _registrars as _registrars
from .registry import _EventKey as _EventKey

CANCEL = ...  # type: Any
NO_RETVAL = ...  # type: Any

def listen(target, identifier, fn, *args, **kw): ...
def listens_for(target, identifier, *args, **kw): ...
def remove(target, identifier, fn): ...
def contains(target, identifier, fn): ...
