# Stubs for sqlalchemy.util.deprecations (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .langhelpers import decorator as decorator

def warn_deprecated(msg, stacklevel: int = ...): ...
def warn_pending_deprecation(msg, stacklevel: int = ...): ...
def deprecated(version, message: Optional[Any] = ..., add_deprecation_to_docstring: bool = ...): ...
def pending_deprecation(version, message: Optional[Any] = ..., add_deprecation_to_docstring: bool = ...): ...
def inject_docstring_text(doctext, injecttext, pos): ...
