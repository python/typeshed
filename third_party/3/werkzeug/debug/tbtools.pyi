# Stubs for werkzeug.debug.tbtools (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

UTF8_COOKIE = ...  # type: Any
system_exceptions = ...  # type: Any
HEADER = ...  # type: Any
FOOTER = ...  # type: Any
PAGE_HTML = ...  # type: Any
CONSOLE_HTML = ...  # type: Any
SUMMARY_HTML = ...  # type: Any
FRAME_HTML = ...  # type: Any
SOURCE_LINE_HTML = ...  # type: Any

def render_console_html(secret, evalex_trusted=True): ...
def get_current_traceback(ignore_system_exceptions=False, show_hidden_frames=False, skip=0): ...

class Line:
    lineno = ...  # type: Any
    code = ...  # type: Any
    in_frame = ...  # type: Any
    current = ...  # type: Any
    def __init__(self, lineno, code): ...
    def classes(self): ...
    def render(self): ...

class Traceback:
    exc_type = ...  # type: Any
    exc_value = ...  # type: Any
    exception_type = ...  # type: Any
    frames = ...  # type: Any
    def __init__(self, exc_type, exc_value, tb): ...
    def filter_hidden_frames(self): ...
    def is_syntax_error(self): ...
    def exception(self): ...
    def log(self, logfile=None): ...
    def paste(self): ...
    def render_summary(self, include_title=True): ...
    def render_full(self, evalex=False, secret=None, evalex_trusted=True): ...
    def generate_plaintext_traceback(self): ...
    def plaintext(self): ...
    id = ...  # type: Any

class Frame:
    lineno = ...  # type: Any
    function_name = ...  # type: Any
    locals = ...  # type: Any
    globals = ...  # type: Any
    filename = ...  # type: Any
    module = ...  # type: Any
    loader = ...  # type: Any
    code = ...  # type: Any
    hide = ...  # type: Any
    info = ...  # type: Any
    def __init__(self, exc_type, exc_value, tb): ...
    def render(self): ...
    def render_line_context(self): ...
    def get_annotated_lines(self): ...
    def eval(self, code, mode=''): ...
    def sourcelines(self): ...
    def get_context_lines(self, context=5): ...
    @property
    def current_line(self): ...
    def console(self): ...
    id = ...  # type: Any
