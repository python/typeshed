from _typeshed import StrOrBytesPath

# Should be consistent with `__init__.py`
def preprocess_paths(paths: list[Any] | StrOrBytesPath) -> list[str | bytes]: ...
