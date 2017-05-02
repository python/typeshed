from typing import Dict, Type, TypeVar, Optional, Union

_T = TypeVar('_T')


def TypedDict(typename: str, fields: Dict[str, Type[_T]]) -> Type[dict]: ...

def Arg(type: _T = ..., name: Optional[str] = ...) -> _T: ...
def DefaultArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...
def NamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...
def DefaultNamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...
def VarArg(type: _T = ...) -> _T: ...
def KwArg(type: _T = ...) -> _T: ...

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = Union[None]
