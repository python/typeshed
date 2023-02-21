class PyAsn1Error(Exception): ...
class ValueConstraintError(PyAsn1Error): ...
class SubstrateUnderrunError(PyAsn1Error): ...

class PyAsn1UnicodeError(PyAsn1Error, UnicodeError):
    def __init__(self, message, unicode_error: UnicodeError | None = ...) -> None: ...

class PyAsn1UnicodeDecodeError(PyAsn1UnicodeError, UnicodeDecodeError): ...
class PyAsn1UnicodeEncodeError(PyAsn1UnicodeError, UnicodeEncodeError): ...
