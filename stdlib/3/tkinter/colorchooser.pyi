from tkinter.commondialog import Dialog
from typing import Any, ClassVar, Optional, Text, Tuple

class Chooser(Dialog):
    command: ClassVar[str]

def askcolor(color: Optional[Text] = ..., **options: Any) -> Union[Tuple[None, None], Tuple[Tuple[float, float, float], str]]: ...
