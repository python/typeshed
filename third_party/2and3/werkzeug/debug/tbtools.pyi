from typing import Any, Optional

UTF8_COOKIE = ...  # type: Any
system_exceptions = ...  # type: Any
HEADER = ...  # type: Any
FOOTER = ...  # type: Any
PAGE_HTML = ...  # type: Any
CONSOLE_HTML = ...  # type: Any
SUMMARY_HTML = ...  # type: Any
FRAME_HTML = ...  # type: Any
SOURCE_LINE_HTML = ...  # type: Any

def render_console_html(secret, evalex_trusted: bool = ...): ...
def get_current_traceback(ignore_system_exceptions: bool = ..., show_hidden_frames: bool = ..., skip: int = ...): ...

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
    def log(self, logfile: Optional[Any] = ...): ...
    def paste(self): ...
    def render_summary(self, include_title: bool = ...): ...
    def render_full(self, evalex: bool = ..., secret: Optional[Any] = ..., evalex_trusted: bool = ...): ...
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
    def eval(self, code, mode: str = ...): ...
    def sourcelines(self): ...
    def get_context_lines(self, context: int = ...): ...
    @property
    def current_line(self): ...
    def console(self): ...
    id = ...  # type: Any
