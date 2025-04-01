from ijson.common import IncompleteJSONError as IncompleteJSONError, JSONError as JSONError, ObjectBuilder as ObjectBuilder
from ijson.utils import coroutine as coroutine, sendable_list as sendable_list

from ._abstract_backend import _BackendModule
from .version import __version__ as __version__

def get_backend(backend: str) -> _BackendModule: ...

backend: _BackendModule = ...
basic_parse = backend.basic_parse
basic_parse_coro = backend.basic_parse_coro
parse = backend.parse
parse_coro = backend.parse_coro
items = backend.items
items_coro = backend.items_coro
kvitems = backend.kvitems
kvitems_coro = backend.kvitems_coro
basic_parse_async = backend.basic_parse_async
parse_async = backend.parse_async
items_async = backend.items_async
kvitems_async = backend.kvitems_async
