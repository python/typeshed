import tkinter
import types

def log_tkinter_error(
    exc: type[BaseException], val: BaseException, tb: types.TracebackType | None
) -> None:
    print("oh no")

root = tkinter.Tk()
root.report_callback_exception = log_tkinter_error
