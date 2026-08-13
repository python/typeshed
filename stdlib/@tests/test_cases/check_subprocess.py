from __future__ import annotations

from subprocess import PIPE, Popen
from typing import IO
from typing_extensions import assert_type


def check_streams_follow_the_type_parameter() -> None:
    # Popen is generic in AnyStr, and the std* streams must carry that
    # parameter through instead of degrading to IO[Any].
    with Popen(["command"], stdin=PIPE, stdout=PIPE, stderr=PIPE) as process:
        assert_type(process, Popen[bytes])
        assert_type(process.stdin, IO[bytes] | None)
        assert_type(process.stdout, IO[bytes] | None)
        assert_type(process.stderr, IO[bytes] | None)

    with Popen(["command"], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True) as process_text:
        assert_type(process_text, Popen[str])
        assert_type(process_text.stdin, IO[str] | None)
        assert_type(process_text.stdout, IO[str] | None)
        assert_type(process_text.stderr, IO[str] | None)


def check_streams_follow_the_other_text_arguments() -> None:
    with Popen(["command"], stdout=PIPE, encoding="utf-8") as process_encoding:
        assert_type(process_encoding.stdout, IO[str] | None)

    with Popen(["command"], stdout=PIPE, errors="replace") as process_errors:
        assert_type(process_errors.stdout, IO[str] | None)

    with Popen(["command"], stdout=PIPE, universal_newlines=True) as process_universal:
        assert_type(process_universal.stdout, IO[str] | None)


def check_reading_a_stream_yields_the_right_type() -> None:
    with Popen(["command"], stdout=PIPE, text=True) as process:
        if process.stdout is not None:
            assert_type(process.stdout.read(), str)
            for line in process.stdout:
                assert_type(line, str)
