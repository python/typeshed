from .lib import GEOSException as GEOSException, ShapelyError as ShapelyError

def setup_signal_checks(interval: int = 10000) -> None: ...

class UnsupportedGEOSVersionError(ShapelyError): ...
class DimensionError(ShapelyError): ...
class TopologicalError(ShapelyError): ...
class ShapelyDeprecationWarning(FutureWarning): ...
class EmptyPartError(ShapelyError): ...
class GeometryTypeError(ShapelyError): ...

# deprecated aliases
ReadingError = ShapelyError
WKBReadingError = ShapelyError
WKTReadingError = ShapelyError
PredicateError = ShapelyError
InvalidGeometryError = ShapelyError
