from .cli import main as main
from .errors import (
    SamplingModuleNotFoundError as SamplingModuleNotFoundError,
    SamplingScriptNotFoundError as SamplingScriptNotFoundError,
    SamplingUnknownProcessError as SamplingUnknownProcessError,
)

MACOS_PERMISSION_ERROR: str
LINUX_PERMISSION_ERROR: str
WINDOWS_PERMISSION_ERROR: str
GENERIC_PERMISSION_ERROR: str

def handle_permission_error() -> None: ...
