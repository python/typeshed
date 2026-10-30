from __future__ import annotations

import sys
import tkinter
import tkinter.filedialog
import traceback
import types
from typing_extensions import assert_type


def custom_handler(exc: type[BaseException], val: BaseException, tb: types.TracebackType | None) -> None:
    print("oh no")


root = tkinter.Tk()
root.report_callback_exception = traceback.print_exception
root.report_callback_exception = custom_handler


def foo(x: int, y: str) -> None:
    pass


root.after(1000, foo, 10, "lol")
root.after(1000, foo, 10, 10)  # type: ignore

# Font size must be integer
label = tkinter.Label()
label.config(font=("", 12))
label.config(font=("", 12.34))  # type: ignore
label.config(font=("", 12, "bold"))
label.config(font=("", 12.34, "bold"))  # type: ignore


# Test the `.count()` method. Comments show values that are returned at runtime.
t = tkinter.Text()
t.insert("end", "asd asd asd\nasd asd")

assert_type(t.count("1.0", "2.3"), tuple[int] | None)  # (15,)
assert_type(t.count("2.3", "2.3"), tuple[int] | None)  # None
assert_type(t.count("1.0", "2.3", "indices"), tuple[int] | None)  # (15,)
assert_type(t.count("2.3", "2.3", "indices"), tuple[int] | None)  # None
assert_type(t.count("1.0", "2.3", "indices", "update"), int | None)  # 15
assert_type(t.count("2.3", "2.3", "indices", "update"), int | None)  # None
assert_type(t.count("1.0", "2.3", "indices", "lines"), tuple[int, int])  # (15, 1)
assert_type(t.count("2.3", "2.3", "indices", "lines"), tuple[int, int])  # (0, 0)
assert_type(t.count("1.0", "2.3", "indices", "lines", "update"), tuple[int, ...])  # (15, 1)
assert_type(t.count("2.3", "2.3", "indices", "lines", "update"), tuple[int, ...])  # (0, 0)
assert_type(t.count("1.0", "2.3", "indices", "lines", "chars"), tuple[int, ...])  # (15, 1, 15)
assert_type(t.count("2.3", "2.3", "indices", "lines", "chars"), tuple[int, ...])  # (0, 0, 0)——
assert_type(t.count("1.0", "2.3", "indices", "lines", "chars", "update"), tuple[int, ...])  # (15, 1, 15)
assert_type(t.count("2.3", "2.3", "indices", "lines", "chars", "update"), tuple[int, ...])  # (0, 0, 0)
assert_type(t.count("1.0", "2.3", "indices", "lines", "chars", "ypixels"), tuple[int, ...])  # (15, 1, 15, 19)
assert_type(t.count("2.3", "2.3", "indices", "lines", "chars", "ypixels"), tuple[int, ...])  # (0, 0, 0, 0)

if sys.version_info >= (3, 13):
    assert_type(t.count("1.0", "2.3", return_ints=True), int)  # 15
    assert_type(t.count("2.3", "2.3", return_ints=True), int)  # 0
    assert_type(t.count("1.0", "2.3", "indices", return_ints=True), int)  # 15
    assert_type(t.count("2.3", "2.3", "indices", return_ints=True), int)  # 0
    assert_type(t.count("1.0", "2.3", "indices", "update", return_ints=True), int)  # 15
    assert_type(t.count("2.3", "2.3", "indices", "update", return_ints=True), int)  # 0
    assert_type(t.count("1.0", "2.3", "indices", "lines", return_ints=True), tuple[int, int])  # (15, 1)
    assert_type(t.count("2.3", "2.3", "indices", "lines", return_ints=True), tuple[int, int])  # (0, 0)
    assert_type(t.count("1.0", "2.3", "indices", "lines", "update", return_ints=True), tuple[int, ...])  # (15, 1)
    assert_type(t.count("2.3", "2.3", "indices", "lines", "update", return_ints=True), tuple[int, ...])  # (0, 0)
    assert_type(t.count("1.0", "2.3", "indices", "lines", "chars", return_ints=True), tuple[int, ...])  # (15, 1, 15)
    assert_type(t.count("2.3", "2.3", "indices", "lines", "chars", return_ints=True), tuple[int, ...])  # (0, 0, 0)
    assert_type(t.count("1.0", "2.3", "indices", "lines", "chars", "update", return_ints=True), tuple[int, ...])  # (15, 1, 15)
    assert_type(t.count("2.3", "2.3", "indices", "lines", "chars", "update", return_ints=True), tuple[int, ...])  # (0, 0, 0)
    assert_type(
        t.count("1.0", "2.3", "indices", "lines", "chars", "ypixels", return_ints=True), tuple[int, ...]
    )  # (15, 1, 15, 19)
    assert_type(t.count("2.3", "2.3", "indices", "lines", "chars", "ypixels", return_ints=True), tuple[int, ...])  # (0, 0, 0, 0)


# Cancelling a dialog gives an empty string or an empty tuple, depending on the Tk version.
assert_type(tkinter.filedialog.askopenfilename(), str | tuple[()])
assert_type(tkinter.filedialog.asksaveasfilename(), str | tuple[()])
assert_type(tkinter.filedialog.askdirectory(), str | tuple[()])
