from __future__ import annotations

import tkinter
import types


def log_tkinter_error(exc: int, val: int, tb: int) -> None:
    print("oh no")


root = tkinter.Tk()
root.report_callback_exception = log_tkinter_error
