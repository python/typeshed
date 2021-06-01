from tkinter.commondialog import Dialog
from typing import Any, ClassVar, Optional, Tuple, Union

class Chooser(Dialog):
    command: ClassVar[str]

def askcolor(
    color: Optional[str | bytes] = ..., **options: Any
) -> Union[Tuple[None, None], Tuple[Tuple[float, float, float], str]]: ...
