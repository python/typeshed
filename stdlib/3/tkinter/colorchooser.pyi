from tkinter.commondialog import Dialog
from typing import Any, ClassVar, Optional, Text, Tuple

class Chooser(Dialog):
    command: ClassVar[str]

def askcolor(color: Optional[Text] = ..., **options: Any) -> Tuple[Optional[Tuple[float, float, float]], Optional[str]]: ...
