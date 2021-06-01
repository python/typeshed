from tkinter.commondialog import Dialog
from typing import Any, ClassVar, Tuple, Union

class Chooser(Dialog):
    command: ClassVar[str]

def askcolor(
    color: str | bytes | None = ..., **options: Any
) -> Union[Tuple[None, None], Tuple[Tuple[float, float, float], str]]: ...
