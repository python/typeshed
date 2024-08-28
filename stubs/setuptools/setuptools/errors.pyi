from typing_extensions import TypeAlias

from ._distutils import errors as _distutils_errors

ByteCompileError: TypeAlias = _distutils_errors.DistutilsByteCompileError
CCompilerError: TypeAlias = _distutils_errors.CCompilerError
ClassError: TypeAlias = _distutils_errors.DistutilsClassError
CompileError: TypeAlias = _distutils_errors.CompileError
ExecError: TypeAlias = _distutils_errors.DistutilsExecError
FileError: TypeAlias = _distutils_errors.DistutilsFileError
InternalError: TypeAlias = _distutils_errors.DistutilsInternalError
LibError: TypeAlias = _distutils_errors.LibError
LinkError: TypeAlias = _distutils_errors.LinkError
ModuleError: TypeAlias = _distutils_errors.DistutilsModuleError
OptionError: TypeAlias = _distutils_errors.DistutilsOptionError
PlatformError: TypeAlias = _distutils_errors.DistutilsPlatformError
PreprocessError: TypeAlias = _distutils_errors.PreprocessError
SetupError: TypeAlias = _distutils_errors.DistutilsSetupError
TemplateError: TypeAlias = _distutils_errors.DistutilsTemplateError
UnknownFileError: TypeAlias = _distutils_errors.UnknownFileError
BaseError: TypeAlias = _distutils_errors.DistutilsError

class InvalidConfigError(OptionError): ...
class RemovedConfigError(OptionError): ...
class RemovedCommandError(BaseError, RuntimeError): ...
class PackageDiscoveryError(BaseError, RuntimeError): ...
