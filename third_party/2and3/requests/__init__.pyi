# Stubs for requests (based on version 2.6.0, Python 3)

import logging
from typing import Any

from . import api, exceptions, models, packages, sessions, status_codes

__title__: Any
__build__: Any
__license__: Any
__copyright__: Any
__version__: Any

Request = models.Request
Response = models.Response
PreparedRequest = models.PreparedRequest
request = api.request
get = api.get
head = api.head
post = api.post
patch = api.patch
put = api.put
delete = api.delete
options = api.options
session = sessions.session
Session = sessions.Session
codes = status_codes.codes
RequestException = exceptions.RequestException
Timeout = exceptions.Timeout
URLRequired = exceptions.URLRequired
TooManyRedirects = exceptions.TooManyRedirects
HTTPError = exceptions.HTTPError
ConnectionError = exceptions.ConnectionError

class NullHandler(logging.Handler):
    def emit(self, record): ...
