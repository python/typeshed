from typing import Any
from werkzeug.wrappers import BaseRequest as Request, BaseResponse as Response

PIN_TIME = ...  # type: Any

def hash_pin(pin): ...
def get_machine_id(): ...

class _ConsoleFrame:
    console = ...  # type: Any
    id = ...  # type: Any
    def __init__(self, namespace): ...

def get_pin_and_cookie_name(app): ...

class DebuggedApplication:
    app = ...  # type: Any
    evalex = ...  # type: Any
    frames = ...  # type: Any
    tracebacks = ...  # type: Any
    request_key = ...  # type: Any
    console_path = ...  # type: Any
    console_init_func = ...  # type: Any
    show_hidden_frames = ...  # type: Any
    secret = ...  # type: Any
    pin_logging = ...  # type: Any
    pin = ...  # type: Any
    def __init__(self, app, evalex=False, request_key='', console_path='', console_init_func=None, show_hidden_frames=False, lodgeit_url=None, pin_security=True, pin_logging=True): ...
    @property
    def pin_cookie_name(self): ...
    def debug_application(self, environ, start_response): ...
    def execute_command(self, request, command, frame): ...
    def display_console(self, request): ...
    def paste_traceback(self, request, traceback): ...
    def get_resource(self, request, filename): ...
    def check_pin_trust(self, environ): ...
    def pin_auth(self, request): ...
    def log_pin_request(self): ...
    def __call__(self, environ, start_response): ...
