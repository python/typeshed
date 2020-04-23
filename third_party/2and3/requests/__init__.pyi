# Stubs for requests (based on version 2.6.0, Python 3)

from typing import Any
from . import models
from . import api
from . import sessions
from . import status_codes
from . import exceptions
from . import packages
import logging

from .models import Request, Response, PreparedRequest
from .api import request, get, head, post, patch, put, delete, options
from .sessions import session, Session
from .status_codes import codes
from .exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError
)

__title__: Any
__build__: Any
__license__: Any
__copyright__: Any
__version__: Any

class NullHandler(logging.Handler):
    def emit(self, record): ...
