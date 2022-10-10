from _typeshed import Incomplete
from typing import Any, NamedTuple

class NativeMethodPatchedResult(NamedTuple):
    py: Incomplete
    native: Incomplete

def testOverwriteNativeMethod(arg) -> NativeMethodPatchedResult: ...
def dumpBool(*args, **kwargs) -> Any: ...  # incomplete
def dumpCString(*args, **kwargs) -> Any: ...  # incomplete
def dumpDouble(*args, **kwargs) -> Any: ...  # incomplete
def dumpFloat(*args, **kwargs) -> Any: ...  # incomplete
def dumpInputArray(*args, **kwargs) -> Any: ...  # incomplete
def dumpInputArrayOfArrays(*args, **kwargs) -> Any: ...  # incomplete
def dumpInputOutputArray(*args, **kwargs) -> Any: ...  # incomplete
def dumpInputOutputArrayOfArrays(*args, **kwargs) -> Any: ...  # incomplete
def dumpInt(*args, **kwargs) -> Any: ...  # incomplete
def dumpRange(*args, **kwargs) -> Any: ...  # incomplete
def dumpRect(*args, **kwargs) -> Any: ...  # incomplete
def dumpRotatedRect(*args, **kwargs) -> Any: ...  # incomplete
def dumpSizeT(*args, **kwargs) -> Any: ...  # incomplete
def dumpString(*args, **kwargs) -> Any: ...  # incomplete
def dumpTermCriteria(*args, **kwargs) -> Any: ...  # incomplete
def dumpVectorOfDouble(*args, **kwargs) -> Any: ...  # incomplete
def dumpVectorOfInt(*args, **kwargs) -> Any: ...  # incomplete
def dumpVectorOfRect(*args, **kwargs) -> Any: ...  # incomplete
def generateVectorOfInt(*args, **kwargs) -> Any: ...  # incomplete
def generateVectorOfMat(*args, **kwargs) -> Any: ...  # incomplete
def generateVectorOfRect(*args, **kwargs) -> Any: ...  # incomplete
def testAsyncArray(*args, **kwargs) -> Any: ...  # incomplete
def testAsyncException(*args, **kwargs) -> Any: ...  # incomplete
def testOverloadResolution(*args, **kwargs) -> Any: ...  # incomplete
def testRaiseGeneralException(*args, **kwargs) -> Any: ...  # incomplete
def testReservedKeywordConversion(*args, **kwargs) -> Any: ...  # incomplete
def testRotatedRect(*args, **kwargs) -> Any: ...  # incomplete
def testRotatedRectVector(*args, **kwargs) -> Any: ...  # incomplete
