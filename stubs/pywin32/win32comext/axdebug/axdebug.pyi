# Can't generate with stubgen because:
# "ImportError: DLL load failed while importing axdebug: The specified module could not be found."
# https://github.com/python/mypy/issues/13822
import _win32typing
from pywintypes import IID as IID

APPBREAKFLAG_DEBUGGER_BLOCK: int
APPBREAKFLAG_DEBUGGER_HALT: int
APPBREAKFLAG_STEP: int
BREAKPOINT_DELETED: int
BREAKPOINT_DISABLED: int
BREAKPOINT_ENABLED: int
BREAKREASON_BREAKPOINT: int
BREAKREASON_DEBUGGER_BLOCK: int
BREAKREASON_DEBUGGER_HALT: int
BREAKREASON_ERROR: int
BREAKREASON_HOST_INITIATED: int
BREAKREASON_LANGUAGE_INITIATED: int
BREAKREASON_STEP: int
BREAKRESUMEACTION_ABORT: int
BREAKRESUMEACTION_CONTINUE: int
BREAKRESUMEACTION_STEP_INTO: int
BREAKRESUMEACTION_STEP_OUT: int
BREAKRESUMEACTION_STEP_OVER: int
CLSID_DefaultDebugSessionProvider: int
CLSID_MachineDebugManager: int
CLSID_ProcessDebugManager: int
DBGPROP_ATTRIB_ACCESS_FINAL: int
DBGPROP_ATTRIB_ACCESS_PRIVATE: int
DBGPROP_ATTRIB_ACCESS_PROTECTED: int
DBGPROP_ATTRIB_ACCESS_PUBLIC: int
DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS: int
DBGPROP_ATTRIB_NO_ATTRIB: int
DBGPROP_ATTRIB_STORAGE_FIELD: int
DBGPROP_ATTRIB_STORAGE_GLOBAL: int
DBGPROP_ATTRIB_STORAGE_STATIC: int
DBGPROP_ATTRIB_STORAGE_VIRTUAL: int
DBGPROP_ATTRIB_TYPE_IS_CONSTANT: int
DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED: int
DBGPROP_ATTRIB_TYPE_IS_VOLATILE: int
DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE: int
DBGPROP_ATTRIB_VALUE_IS_INVALID: int
DBGPROP_ATTRIB_VALUE_READONLY: int
DBGPROP_INFO_ATTRIBUTES: int
DBGPROP_INFO_AUTOEXPAND: int
DBGPROP_INFO_DEBUGPROP: int
DBGPROP_INFO_FULLNAME: int
DBGPROP_INFO_NAME: int
DBGPROP_INFO_TYPE: int
DBGPROP_INFO_VALUE: int
DEBUG_TEXT_ALLOWBREAKPOINTS: int
DEBUG_TEXT_ISEXPRESSION: int
DOCUMENTNAMETYPE_APPNODE: int
DOCUMENTNAMETYPE_FILE_TAIL: int
DOCUMENTNAMETYPE_TITLE: int
DOCUMENTNAMETYPE_URL: int
ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller: int
ERRORRESUMEACTION_ReexecuteErrorStatement: int
ERRORRESUMEACTION_SkipErrorStatement: int
EX_DBGPROP_INFO_DEBUGEXTPROP: int
EX_DBGPROP_INFO_ID: int
EX_DBGPROP_INFO_LOCKBYTES: int
EX_DBGPROP_INFO_NTYPE: int
EX_DBGPROP_INFO_NVALUE: int
SOURCETEXT_ATTR_COMMENT: int
SOURCETEXT_ATTR_FUNCTION_START: int
SOURCETEXT_ATTR_KEYWORD: int
SOURCETEXT_ATTR_NONSOURCE: int
SOURCETEXT_ATTR_NUMBER: int
SOURCETEXT_ATTR_OPERATOR: int
SOURCETEXT_ATTR_STRING: int
TEXT_DOC_ATTR_READONLY: int
APPBREAKFLAG_IN_BREAKPOINT: int
APPBREAKFLAG_STEPTYPE_BYTECODE: int
APPBREAKFLAG_STEPTYPE_MACHINE: int
APPBREAKFLAG_STEPTYPE_MASK: int
APPBREAKFLAG_STEPTYPE_SOURCE: int

def GetStackAddress(*args, **kwargs): ...  # incomplete
def GetThreadStateHandle(*args, **kwargs): ...  # incomplete

IID_IActiveScriptDebug: _win32typing.PyIID
IID_IActiveScriptErrorDebug: _win32typing.PyIID
IID_IActiveScriptSiteDebug: _win32typing.PyIID
IID_IApplicationDebugger: _win32typing.PyIID
IID_IDebugApplication: _win32typing.PyIID
IID_IDebugApplicationNode: _win32typing.PyIID
IID_IDebugApplicationNodeEvents: _win32typing.PyIID
IID_IDebugApplicationThread: _win32typing.PyIID
IID_IDebugCodeContext: _win32typing.PyIID
IID_IDebugDocument: _win32typing.PyIID
IID_IDebugDocumentContext: _win32typing.PyIID
IID_IDebugDocumentHelper: _win32typing.PyIID
IID_IDebugDocumentHost: _win32typing.PyIID
IID_IDebugDocumentInfo: _win32typing.PyIID
IID_IDebugDocumentProvider: _win32typing.PyIID
IID_IDebugDocumentText: _win32typing.PyIID
IID_IDebugDocumentTextAuthor: _win32typing.PyIID
IID_IDebugDocumentTextEvents: _win32typing.PyIID
IID_IDebugDocumentTextExternalAuthor: _win32typing.PyIID
IID_IDebugExpression: _win32typing.PyIID
IID_IDebugExpressionCallBack: _win32typing.PyIID
IID_IDebugExpressionContext: _win32typing.PyIID
IID_IDebugProperty: _win32typing.PyIID
IID_IDebugSessionProvider: _win32typing.PyIID
IID_IDebugStackFrame: _win32typing.PyIID
IID_IDebugStackFrameSniffer: _win32typing.PyIID
IID_IDebugStackFrameSnifferEx: _win32typing.PyIID
IID_IDebugSyncOperation: _win32typing.PyIID
IID_IEnumDebugApplicationNodes: _win32typing.PyIID
IID_IEnumDebugCodeContexts: _win32typing.PyIID
IID_IEnumDebugExpressionContexts: _win32typing.PyIID
IID_IEnumDebugPropertyInfo: _win32typing.PyIID
IID_IEnumDebugStackFrames: _win32typing.PyIID
IID_IEnumRemoteDebugApplicationThreads: _win32typing.PyIID
IID_IEnumRemoteDebugApplications: _win32typing.PyIID
IID_IMachineDebugManager: _win32typing.PyIID
IID_IMachineDebugManagerEvents: _win32typing.PyIID
IID_IProcessDebugManager: _win32typing.PyIID
IID_IProvideExpressionContexts: _win32typing.PyIID
IID_IRemoteDebugApplication: _win32typing.PyIID
IID_IRemoteDebugApplicationEvents: _win32typing.PyIID
IID_IRemoteDebugApplicationThread: _win32typing.PyIID

def SetThreadStateTrace(*args, **kwargs): ...  # incomplete
