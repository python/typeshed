from typing import Any

from google.cloud.ndb import model

class _ClassKeyProperty(model.StringProperty):
    def __init__(self, name: Any = ..., indexed: bool = ...) -> None: ...

class PolyModel(model.Model):
    class_: Any = ...
