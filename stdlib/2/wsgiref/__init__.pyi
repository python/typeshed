# Type declaration for a WSGI Function in Python 2
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
WSGIFunction = Callable[[Dict[Union[unicode, str], Union[unicode, str]],
                         Union[
                           Callable[[Union[unicode, str], List[Tuple[Union[unicode, str], Union[unicode, str]]]], Callable[[Union[unicode, str]], None]],
                           Callable[[Union[unicode, str], List[Tuple[Union[unicode, str], Union[unicode, str]]], exc_info], Callable[[Union[unicode, str]], None]]
                         ]],
                         Iterable[Union[unicode, str]]]
