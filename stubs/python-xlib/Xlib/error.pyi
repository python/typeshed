from _typeshed import SliceableBuffer
from typing_extensions import Literal

from Xlib.protocol import display, rq

class DisplayError(Exception):
    display: object
    def __init__(self, display: object) -> None: ...

class DisplayNameError(DisplayError): ...

class DisplayConnectionError(DisplayError):
    display: object
    msg: object
    def __init__(self, display: object, msg: object) -> None: ...

class ConnectionClosedError(Exception):
    whom: object
    def __init__(self, whom: object) -> None: ...

class XauthError(Exception): ...
class XNoAuthError(Exception): ...
class ResourceIDError(Exception): ...

class XError(rq.GetAttrData, Exception):
    def __init__(self, display: display.Display, data: SliceableBuffer) -> None: ...

class XResourceError(XError): ...
class BadRequest(XError): ...
class BadValue(XError): ...
class BadWindow(XResourceError): ...
class BadPixmap(XResourceError): ...
class BadAtom(XError): ...
class BadCursor(XResourceError): ...
class BadFont(XResourceError): ...
class BadMatch(XError): ...
class BadDrawable(XResourceError): ...
class BadAccess(XError): ...
class BadAlloc(XError): ...
class BadColor(XResourceError): ...
class BadGC(XResourceError): ...
class BadIDChoice(XResourceError): ...
class BadName(XError): ...
class BadLength(XError): ...
class BadImplementation(XError): ...

xerror_class: dict[int, type[XError]]

class CatchError:
    error_types: tuple[type[XError], ...]
    error: XError | None
    request: rq.Request | None
    def __init__(self, *errors: type[XError]) -> None: ...
    def __call__(self, error: XError, request: rq.Request | None) -> Literal[0, 1]: ...
    def get_error(self) -> XError | None: ...
    def get_request(self) -> rq.Request | None: ...
    def reset(self) -> None: ...
