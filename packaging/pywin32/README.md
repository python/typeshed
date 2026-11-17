## Typing stubs for pywin32

This is a [type stub package](https://typing.python.org/en/latest/tutorials/external_libraries.html)
for the [`pywin32`](https://github.com/mhammond/pywin32) package. It can be used by type checkers
to check code that uses `pywin32`. This version of
`types-pywin32` aims to provide accurate annotations for
`pywin32==312.*`.

These stubs come from [typeshed](https://github.com/python/typeshed). This StableKite build includes corrections for Windows handle ownership and wait functions. The matching [stub source](https://github.com/StableKite/typeshed/tree/c65cccd7cf993d87301a2f733820888a4545e5e5/stubs/pywin32) is available in the fork.

This package was tested with the following type checkers:
* [mypy](https://www.mypy-lang.org/) 2.3.0
* [pyrefly](https://pyrefly.org/) 1.3.0.dev1
* [pyright](https://microsoft.github.io/pyright/) 1.1.414
* [ty](https://docs.astral.sh/ty/) 0.0.59

It was generated from typeshed commit
[`c65cccd7cf993d87301a2f733820888a4545e5e5`](https://github.com/StableKite/typeshed/commit/c65cccd7cf993d87301a2f733820888a4545e5e5).
## Updating the package

Regenerate this directory from the canonical stubs with [stub_uploader](https://github.com/typeshed-internal/stub_uploader/tree/b20030cb8594aa8f3ac13c813fbc2505e01d6c3d), then update the source commit and file hashes in `STUB_SOURCE.json`. Run `python packaging/pywin32/check_stubs.py` from a fork checkout to check both copies. Package data paths in `pyproject.toml` use forward slashes on all platforms.
