from _typeshed import Incomplete
from typing import Final, Literal

import _win32typing
from win32.lib.pywintypes import error as error

def AssignProcessToJobObject(
    hJob: int | _win32typing.PyHANDLE | None, hProcess: int | _win32typing.PyHANDLE | None, /
) -> None: ...
def CreateJobObject(jobAttributes: _win32typing.PySECURITY_ATTRIBUTES | None, name: str, /) -> _win32typing.PyHANDLE: ...
def OpenJobObject(desiredAccess: int, inheritHandles: bool | Literal[0, 1], name: str, /) -> _win32typing.PyHANDLE: ...
def TerminateJobObject(hJob: int | _win32typing.PyHANDLE | None, exitCode: int, /) -> None: ...
def UserHandleGrantAccess(
    hUserHandle: int | _win32typing.PyHANDLE | None, hJob: int | _win32typing.PyHANDLE | None, grant: bool | Literal[0, 1], /
) -> None: ...
def IsProcessInJob(hProcess: int | _win32typing.PyHANDLE | None, hJob: int | _win32typing.PyHANDLE | None, /) -> bool: ...
def QueryInformationJobObject(
    Job: int | _win32typing.PyHANDLE | None, JobObjectInfoClass: int, /
) -> _win32typing.InformationJob: ...
def SetInformationJobObject(
    Job: int | _win32typing.PyHANDLE | None, JobObjectInfoClass: int, JobObjectInfo: dict[str, Incomplete], /
) -> None: ...

JOB_OBJECT_ASSIGN_PROCESS: Final = 0x0001
JOB_OBJECT_SET_ATTRIBUTES: Final = 0x0002
JOB_OBJECT_QUERY: Final = 0x0004
JOB_OBJECT_TERMINATE: Final = 0x0008
JOB_OBJECT_SET_SECURITY_ATTRIBUTES: Final = 0x0010
JOB_OBJECT_ALL_ACCESS: Final[int]
JOB_OBJECT_TERMINATE_AT_END_OF_JOB: Final = 0
JOB_OBJECT_POST_AT_END_OF_JOB: Final = 1
JOB_OBJECT_MSG_END_OF_JOB_TIME: Final[int]
JOB_OBJECT_MSG_END_OF_PROCESS_TIME: Final[int]
JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT: Final[int]
JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO: Final[int]
JOB_OBJECT_MSG_NEW_PROCESS: Final[int]
JOB_OBJECT_MSG_EXIT_PROCESS: Final[int]
JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS: Final[int]
JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT: Final[int]
JOB_OBJECT_MSG_JOB_MEMORY_LIMIT: Final[int]
JOB_OBJECT_LIMIT_WORKINGSET: Final = 0x00000001
JOB_OBJECT_LIMIT_PROCESS_TIME: Final = 0x00000002
JOB_OBJECT_LIMIT_JOB_TIME: Final = 0x00000004
JOB_OBJECT_LIMIT_ACTIVE_PROCESS: Final = 0x00000008
JOB_OBJECT_LIMIT_AFFINITY: Final = 0x00000010
JOB_OBJECT_LIMIT_PRIORITY_CLASS: Final = 0x00000020
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME: Final = 0x00000040
JOB_OBJECT_LIMIT_SCHEDULING_CLASS: Final = 0x00000080
JOB_OBJECT_LIMIT_PROCESS_MEMORY: Final = 0x00000100
JOB_OBJECT_LIMIT_JOB_MEMORY: Final = 0x00000200
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION: Final = 0x00000400
JOB_OBJECT_LIMIT_BREAKAWAY_OK: Final = 0x00000800
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK: Final = 0x00001000
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: Final = 0x00002000
JOB_OBJECT_LIMIT_VALID_FLAGS: Final[int]
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS: Final[int]
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS: Final[int]
JOB_OBJECT_UILIMIT_NONE: Final[int]
JOB_OBJECT_UILIMIT_HANDLES: Final = 0x00000001
JOB_OBJECT_UILIMIT_READCLIPBOARD: Final = 0x00000002
JOB_OBJECT_UILIMIT_WRITECLIPBOARD: Final = 0x00000004
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS: Final = 0x00000008
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS: Final = 0x00000010
JOB_OBJECT_UILIMIT_GLOBALATOMS: Final = 0x00000020
JOB_OBJECT_UILIMIT_DESKTOP: Final = 0x00000040
JOB_OBJECT_UILIMIT_EXITWINDOWS: Final = 0x00000080
JOB_OBJECT_UILIMIT_ALL: Final[int]
JOB_OBJECT_UI_VALID_FLAGS: Final[int]
JOB_OBJECT_SECURITY_NO_ADMIN: Final = 0x00000001
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN: Final = 0x00000002
JOB_OBJECT_SECURITY_ONLY_TOKEN: Final = 0x00000004
JOB_OBJECT_SECURITY_FILTER_TOKENS: Final = 0x00000008
JOB_OBJECT_SECURITY_VALID_FLAGS: Final[int]
JobObjectBasicAccountingInformation: Final = 1
JobObjectBasicLimitInformation: Final = 2
JobObjectBasicProcessIdList: Final = 3
JobObjectBasicUIRestrictions: Final = 4
JobObjectSecurityLimitInformation: Final = 5
JobObjectEndOfJobTimeInformation: Final = 6
JobObjectAssociateCompletionPortInformation: Final[int]
JobObjectBasicAndIoAccountingInformation: Final = 8
JobObjectExtendedLimitInformation: Final = 9
JobObjectJobSetInformation: Final[int]
MaxJobObjectInfoClass: Final[int]
UNICODE: Final = 1
