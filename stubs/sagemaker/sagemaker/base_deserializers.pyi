import abc
from _typeshed import Incomplete

class BaseDeserializer(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deserialize(self, stream, content_type): ...
    @property
    @abc.abstractmethod
    def ACCEPT(self): ...

class SimpleBaseDeserializer:
    accept: Incomplete
    def __init__(self, accept: str = "*/*") -> None: ...
    @property
    def ACCEPT(self): ...

class StringDeserializer(SimpleBaseDeserializer):
    encoding: Incomplete
    def __init__(self, encoding: str = "UTF-8", accept: str = "application/json") -> None: ...
    def deserialize(self, stream, content_type): ...

class BytesDeserializer(SimpleBaseDeserializer):
    def deserialize(self, stream, content_type): ...

class CSVDeserializer(SimpleBaseDeserializer):
    encoding: Incomplete
    def __init__(self, encoding: str = "utf-8", accept: str = "text/csv") -> None: ...
    def deserialize(self, stream, content_type): ...

class StreamDeserializer(SimpleBaseDeserializer):
    def deserialize(self, stream, content_type): ...

class NumpyDeserializer(SimpleBaseDeserializer):
    dtype: Incomplete
    allow_pickle: Incomplete
    def __init__(self, dtype: Incomplete | None = None, accept: str = "application/x-npy", allow_pickle: bool = True) -> None: ...
    def deserialize(self, stream, content_type): ...

class JSONDeserializer(SimpleBaseDeserializer):
    def __init__(self, accept: str = "application/json") -> None: ...
    def deserialize(self, stream, content_type): ...

class PandasDeserializer(SimpleBaseDeserializer):
    def __init__(self, accept=("text/csv", "application/json")) -> None: ...
    def deserialize(self, stream, content_type): ...

class JSONLinesDeserializer(SimpleBaseDeserializer):
    def __init__(self, accept: str = "application/jsonlines") -> None: ...
    def deserialize(self, stream, content_type): ...
