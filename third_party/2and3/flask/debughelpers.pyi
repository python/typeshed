# Stubs for flask.debughelpers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from .app import Flask
from .blueprints import Blueprint
from .globals import _request_ctx_stack

class UnexpectedUnicodeError(AssertionError, UnicodeError): ...

class DebugFilesKeyError(KeyError, AssertionError):
    msg: Any = ...
    def __init__(self, request: Any, key: Any) -> None: ...

class FormDataRoutingRedirect(AssertionError):
    def __init__(self, request: Any) -> None: ...

def attach_enctype_error_multidict(request: Any): ...
def explain_template_loading_attempts(app: Any, template: Any, attempts: Any) -> None: ...
def explain_ignored_app_run() -> None: ...
