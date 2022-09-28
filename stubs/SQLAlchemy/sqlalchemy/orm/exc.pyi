from typing import Any

from .. import exc as sa_exc
from ..exc import NoResultFound as NoResultFound

NO_STATE: Any

class StaleDataError(sa_exc.SQLAlchemyError): ...

ConcurrentModificationError = StaleDataError

class FlushError(sa_exc.SQLAlchemyError): ...
class UnmappedError(sa_exc.InvalidRequestError): ...
class ObjectDereferencedError(sa_exc.SQLAlchemyError): ...

class DetachedInstanceError(sa_exc.SQLAlchemyError):
    code: str

class UnmappedInstanceError(UnmappedError):
    def __init__(self, obj, msg: Any | None = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedClassError(UnmappedError):
    def __init__(self, cls, msg: Any | None = ...) -> None: ...
    def __reduce__(self): ...

class ObjectDeletedError(sa_exc.InvalidRequestError):
    def __init__(self, state, msg: Any | None = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedColumnError(sa_exc.InvalidRequestError): ...

class LoaderStrategyException(sa_exc.InvalidRequestError):
    def __init__(self, applied_to_property_type, requesting_property, applies_to, actual_strategy_type, strategy_key) -> None: ...
