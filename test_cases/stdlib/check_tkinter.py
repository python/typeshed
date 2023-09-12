from __future__ import annotations

import traceback
import tkinter
import types

def custom_handler(
    exc: type[BaseException], val: BaseException, tb: types.TracebackType | None
) -> None:
    traceback.print_exception(exc, val, tb)


root = tkinter.Tk()
root.report_callback_exception = traceback.print_exception
root.report_callback_exception = custom_handler
