# Stubs for sqlalchemy.dialects.mysql.types (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import sqltypes
from ... import types as sqltypes

class _NumericType:
    unsigned = ...  # type: Any
    zerofill = ...  # type: Any
    def __init__(self, unsigned: bool = ..., zerofill: bool = ..., **kw) -> None: ...

class _FloatType(_NumericType, sqltypes.Float):
    scale = ...  # type: Any
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...

class _IntegerType(_NumericType, sqltypes.Integer):
    display_width = ...  # type: Any
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class _StringType(sqltypes.String):
    charset = ...  # type: Any
    ascii = ...  # type: Any
    unicode = ...  # type: Any
    binary = ...  # type: Any
    national = ...  # type: Any
    def __init__(self, charset: Optional[Any] = ..., collation: Optional[Any] = ..., ascii: bool = ..., binary: bool = ..., unicode: bool = ..., national: bool = ..., **kw) -> None: ...

class _MatchType(sqltypes.Float, sqltypes.MatchType):
    def __init__(self, **kw) -> None: ...

class NUMERIC(_NumericType, sqltypes.NUMERIC):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...

class DECIMAL(_NumericType, sqltypes.DECIMAL):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...

class DOUBLE(_FloatType):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...

class REAL(_FloatType, sqltypes.REAL):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...

class FLOAT(_FloatType, sqltypes.FLOAT):
    __visit_name__ = ...  # type: str
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw) -> None: ...
    def bind_processor(self, dialect): ...

class INTEGER(_IntegerType, sqltypes.INTEGER):
    __visit_name__ = ...  # type: str
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class BIGINT(_IntegerType, sqltypes.BIGINT):
    __visit_name__ = ...  # type: str
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class MEDIUMINT(_IntegerType):
    __visit_name__ = ...  # type: str
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class TINYINT(_IntegerType):
    __visit_name__ = ...  # type: str
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class SMALLINT(_IntegerType, sqltypes.SMALLINT):
    __visit_name__ = ...  # type: str
    def __init__(self, display_width: Optional[Any] = ..., **kw) -> None: ...

class BIT(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    length = ...  # type: Any
    def __init__(self, length: Optional[Any] = ...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIME(sqltypes.TIME):
    __visit_name__ = ...  # type: str
    fsp = ...  # type: Any
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class TIMESTAMP(sqltypes.TIMESTAMP):
    __visit_name__ = ...  # type: str
    fsp = ...  # type: Any
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None: ...

class DATETIME(sqltypes.DATETIME):
    __visit_name__ = ...  # type: str
    fsp = ...  # type: Any
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None: ...

class YEAR(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    display_width = ...  # type: Any
    def __init__(self, display_width: Optional[Any] = ...) -> None: ...

class TEXT(_StringType, sqltypes.TEXT):
    __visit_name__ = ...  # type: str
    def __init__(self, length: Optional[Any] = ..., **kw) -> None: ...

class TINYTEXT(_StringType):
    __visit_name__ = ...  # type: str
    def __init__(self, **kwargs) -> None: ...

class MEDIUMTEXT(_StringType):
    __visit_name__ = ...  # type: str
    def __init__(self, **kwargs) -> None: ...

class LONGTEXT(_StringType):
    __visit_name__ = ...  # type: str
    def __init__(self, **kwargs) -> None: ...

class VARCHAR(_StringType, sqltypes.VARCHAR):
    __visit_name__ = ...  # type: str
    def __init__(self, length: Optional[Any] = ..., **kwargs) -> None: ...

class CHAR(_StringType, sqltypes.CHAR):
    __visit_name__ = ...  # type: str
    def __init__(self, length: Optional[Any] = ..., **kwargs) -> None: ...

class NVARCHAR(_StringType, sqltypes.NVARCHAR):
    __visit_name__ = ...  # type: str
    def __init__(self, length: Optional[Any] = ..., **kwargs) -> None: ...

class NCHAR(_StringType, sqltypes.NCHAR):
    __visit_name__ = ...  # type: str
    def __init__(self, length: Optional[Any] = ..., **kwargs) -> None: ...

class TINYBLOB(sqltypes._Binary):
    __visit_name__ = ...  # type: str

class MEDIUMBLOB(sqltypes._Binary):
    __visit_name__ = ...  # type: str

class LONGBLOB(sqltypes._Binary):
    __visit_name__ = ...  # type: str
