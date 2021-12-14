from ... import types as sqltypes

class JSON(sqltypes.JSON): ...

class _FormatTypeMixin:
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSONIndexType(_FormatTypeMixin, sqltypes.JSON.JSONIndexType): ...
class JSONPathType(_FormatTypeMixin, sqltypes.JSON.JSONPathType): ...
