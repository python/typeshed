from __future__ import annotations

import tkinter
import traceback
import types


def custom_handler(exc: type[BaseException], val: BaseException, tb: types.TracebackType | None) -> None:
    print("oh no")


root = tkinter.Tk()
root.report_callback_exception = traceback.print_exception
root.report_callback_exception = custom_handler


def foo(x: int, y: str) -> None:
    pass


root.after(1000, foo, 10, "lol")
root.after(1000, foo, 10, 10)  # type: ignore
