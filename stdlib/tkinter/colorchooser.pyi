import sys
from tkinter.commondialog import Dialog
from typing import ClassVar
from tkinter import _Color, Misc

if sys.version_info >= (3, 9):
    __all__ = ["Chooser", "askcolor"]

class Chooser(Dialog):
    command: ClassVar[str]

def askcolor(color: str | bytes | None = ..., *,
initialcolor: _Color=...,
parent: Misc=...,
title: str=...
) -> tuple[None, None] | tuple[tuple[float, float, float], str]: ...
