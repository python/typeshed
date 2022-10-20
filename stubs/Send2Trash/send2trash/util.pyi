from _typeshed import StrOrBytesPath
from collections.abc import Sequence

def preprocess_paths(paths: StrOrBytesPath | Sequence[StrOrBytesPath]) -> list[str | bytes]: ...
