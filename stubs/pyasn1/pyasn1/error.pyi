class PyAsn1Error(Exception):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def context(self): ...

class ValueConstraintError(PyAsn1Error): ...
class SubstrateUnderrunError(PyAsn1Error): ...
class EndOfStreamError(SubstrateUnderrunError): ...
class UnsupportedSubstrateError(PyAsn1Error): ...

class PyAsn1UnicodeError(PyAsn1Error, UnicodeError):
    def __init__(self, message, unicode_error: UnicodeError | None = None) -> None: ...

class PyAsn1UnicodeDecodeError(PyAsn1UnicodeError, UnicodeDecodeError): ...
class PyAsn1UnicodeEncodeError(PyAsn1UnicodeError, UnicodeEncodeError): ...
