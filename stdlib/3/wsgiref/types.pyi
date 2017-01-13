# Type declaration for a WSGI Function in Python 3
#
# wsgiref/typing.py doesn't exist and neither does WSGIApplication, it's a type
# provided for type checking purposes.
#
# To correctly use this type stub, utilize the `TYPE_CHECKING` flag in
# typing:
#
# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#   from wsgiref import WSGIFunction
#

from typing import Callable, Iterable, List, Optional, Tuple, Type, Union
from types import TracebackType

_exc_info = Tuple[Optional[Type[BaseException]],
                  Optional[BaseException],
                  Optional[TracebackType]]
WSGIApplication = Callable[[Dict[str, str],
                            Union[
                                Callable[[str, List[Tuple[str, str]]], Callable[[Union[bytes, str]], None]],
                                Callable[[str, List[Tuple[str, str]], _exc_info], Callable[[Union[bytes, str]], None]]
                            ]],
                            Iterable[Union[bytes, str]]]
