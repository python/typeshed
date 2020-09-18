from tkinter import Frame, Grid, Misc, Pack, Place, Scrollbar, Text
from typing import Any, Optional

# At runtime, just Text, but the methods from the other 3 are dynamically inherited
class ScrolledText(Pack, Grid, Place, Text):
    frame: Frame
    vbar: Scrollbar
    def __init__(self, master: Optional[Misc], **kwargs: Any) -> None: ...
