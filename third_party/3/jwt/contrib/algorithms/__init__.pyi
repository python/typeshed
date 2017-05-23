from typing import Callable, Any, Union
from hashlib import _DataType

# In reality, _HashAlg is a function of the type
# that hashlib.sha256/384/512 are, but there doesn't
# seem to be a consistent exportable name that we can reference
# for that, so we'll just say it's a Callable here.
_HashAlg = Callable[[_DataType], Any]
