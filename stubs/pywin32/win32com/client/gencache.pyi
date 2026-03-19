from typing import Literal

from win32com.client import dynamic

def EnsureDispatch(
    prog_id: str | dynamic.PyIDispatchType | dynamic._GoodDispatchTypes | dynamic.PyIUnknownType,
    bForDemand: bool | Literal[0, 1] = 1,
) -> dynamic.CDispatch: ...
