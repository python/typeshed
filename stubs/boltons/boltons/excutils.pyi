# TODO: DONE!

from typing import Any

class ExceptionCauseMixin(Exception):
    cause: Any
    def get_str(self) -> str: ...
