from typing import Dict, Type, TypeVar, Optional, Union

_T = TypeVar('_T')


def Arg(typ: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultArg(typ: _T = ..., name: Optional[str] = ...) -> _T: ...

def NamedArg(typ: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultNamedArg(typ: _T = ..., name: Optional[str] = ...) -> _T: ...

def VarArg(typ: _T = ...) -> _T: ...

def KwArg(typ: _T = ...) -> _T: ...


def TypedDict(typename: str, fields: Dict[str, Type[_T]]) -> Type[dict]: ...

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = Union[None]
