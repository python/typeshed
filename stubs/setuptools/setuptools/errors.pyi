from ._distutils.errors import DistutilsError

class RemovedCommandError(DistutilsError, RuntimeError): ...
class CCompilerError(Exception): ...
class PreprocessError(CCompilerError): ...
class CompileError(CCompilerError): ...
class LibError(CCompilerError): ...
class LinkError(CCompilerError): ...
class UnknownFileError(CCompilerError): ...
