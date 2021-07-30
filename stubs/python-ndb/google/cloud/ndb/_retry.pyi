from typing import Any

from google.cloud.ndb import exceptions as exceptions, tasklets as tasklets

def wraps_safely(obj: Any, attr_names: Any = ...): ...
def retry_async(callback: Any, retries: Any = ...): ...

TRANSIENT_ERRORS: Any

def is_transient_error(error: Any): ...
