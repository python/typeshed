# mypy: disable-error-code="method-assign"
from __future__ import annotations

import tkinter
import traceback
import types


def custom_handler(exc: type[BaseException], val: BaseException, tb: types.TracebackType | None) -> None:
    print("oh no")


def custom_wrong_handler(exc: BaseException, val: BaseException, tb: types.TracebackType | None) -> None:
    print("oh no")


root = tkinter.Tk()
root.report_callback_exception = traceback.print_exception
root.report_callback_exception = custom_handler
root.report_callback_exception = custom_wrong_handler  # type: ignore
