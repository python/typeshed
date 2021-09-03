from .compat import PY3 as PY3

class TrashPermissionError(_permission_error):
    def __init__(self, filename) -> None: ...
