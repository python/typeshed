from ctypes import Structure
from typing import Any

from .compat import binary_type as binary_type
from .util import preprocess_paths as preprocess_paths

Foundation: Any
CoreServices: Any
GetMacOSStatusCommentString: Any
FSPathMakeRefWithOptions: Any
FSMoveObjectToTrashSync: Any
kFSPathMakeRefDefaultOptions: int
kFSPathMakeRefDoNotFollowLeafSymlink: int
kFSFileOperationDefaultOptions: int
kFSFileOperationOverwrite: int
kFSFileOperationSkipSourcePermissionErrors: int
kFSFileOperationDoNotMoveAcrossVolumes: int
kFSFileOperationSkipPreflight: int

class FSRef(Structure): ...

def check_op_result(op_result) -> None: ...
def send2trash(paths) -> None: ...
