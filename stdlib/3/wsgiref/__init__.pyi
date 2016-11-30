# Type declaration for a WSGI Function in Python 3
#
# This function actually exist, but we need a central place to define the type
# of a WSGI Application.
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

exc_info = Tuple[Optional[Type[BaseException]],
                 Optional[BaseException],
                 Optional[TracebackType]]
WSGIFunction = Callable[[Dict[str, str],
                         Union[
                           Callable[[str, List[Tuple[str, str]]], Callable[[Union[bytes, str]], None]],
                           Callable[[str, List[Tuple[str, str]], exc_info], Callable[[Union[bytes, str]], None]]
                         ]],
                         Iterable[Union[bytes, str]]]
