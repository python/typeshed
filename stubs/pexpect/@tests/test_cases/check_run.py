from __future__ import annotations

import sys
from typing_extensions import assert_type

import pexpect

if sys.platform != "win32":
    # run() returns bytes unless an encoding is passed to it.
    assert_type(pexpect.run("ls"), bytes)
    assert_type(pexpect.run("ls", encoding="utf-8"), str)
    assert_type(pexpect.run("ls", timeout=None, withexitstatus=False), bytes)

    # With withexitstatus, run() returns the exit status, which is None
    # if the child was killed by a signal.
    assert_type(pexpect.run("ls", withexitstatus=True), tuple[bytes, int | None])
    assert_type(pexpect.run("ls", 30, True), tuple[bytes, int | None])
    assert_type(pexpect.run("ls", withexitstatus=True, encoding="utf-8"), tuple[str, int | None])

    flag: bool = bool(sys.argv)
    assert_type(pexpect.run("ls", withexitstatus=flag), bytes | tuple[bytes, int | None])

    # Responses may be strings, bytes or callbacks.
    pexpect.run("ls", events={"Password:": "secret\n", b"\?": b"y\n", "done": lambda d: True})
    pexpect.run("ls", events=[("Password:", "secret\n")])

    assert_type(pexpect.runu("ls"), str)
    assert_type(pexpect.runu("ls", withexitstatus=True), tuple[str, int | None])

    # wait() returns None if the child was killed by a signal.
    child = pexpect.spawn("ls")
    assert_type(child.wait(), int | None)
