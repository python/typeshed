This directory contains several tests:
- `tests/mypy_test.py`
tests the stubs with [mypy](https://github.com/python/mypy/)
- `tests/pytype_test.py` tests the stubs with
[pytype](https://github.com/google/pytype/).
- `tests/pyright_test.py` tests the stubs with
[pyright](https://github.com/microsoft/pyright).
- `tests/regr_test.py` runs mypy against the test cases for typeshed's
stubs, guarding against accidental regressions.
- `tests/check_consistent.py` checks certain files in typeshed remain
consistent with each other.
- `tests/stubtest_stdlib.py` checks standard library stubs against the
objects at runtime.
- `tests/stubtest_third_party.py` checks third-party stubs against the
objects at runtime.
- `tests/typecheck_typeshed.py` runs mypy against typeshed's own code
in the `tests` and `scripts` directories.

To run the tests, follow the [setup instructions](../CONTRIBUTING.md#preparing-the-environment)
in the `CONTRIBUTING.md` document. In particular, we recommend running with Python 3.9+.

## Run all tests for a specific stub

Run using:
```
(.venv3)$ python3 scripts/runtests.py <stdlib-or-stubs>/<stub-to-test>
```

This script will run all tests below for a specific typeshed directory. If a
test supports multiple python versions, the oldest supported by typeshed will
be selected. A summary of the results will be printed to the terminal.

You must provide a single argument which is a path to the stubs to test, like
so: `stdlib/os` or `stubs/requests`.

## mypy\_test.py

Run using:
```
(.venv3)$ python3 tests/mypy_test.py
```

The test has two parts: running mypy on the stdlib stubs,
and running mypy on the third-party stubs.

This test is shallow — it verifies that all stubs can be
imported but doesn't check whether stubs match their implementation
(in the Python standard library or a third-party package).

Run `python tests/mypy_test.py --help` for information on the various configuration options
for this script.

## pytype\_test.py

Note: this test cannot be run on Windows
systems unless you are using Windows Subsystem for Linux.

Run using:
```
(.venv3)$ python3 tests/pytype_test.py
```

This test works similarly to `mypy_test.py`, except it uses `pytype`.

## pyright\_test.py

This test requires [Node.js](https://nodejs.org) to be installed. Although
typeshed runs pyright in CI, it does not currently use this script. However,
this script uses the same pyright version and configuration as the CI.
```
(.venv3)$ python3 tests/pyright_test.py                                # Check all files
(.venv3)$ python3 tests/pyright_test.py stdlib/sys.pyi                 # Check one file
(.venv3)$ python3 tests/pyright_test.py -p pyrightconfig.stricter.json # Check with the stricter config.
```

`pyrightconfig.stricter.json` is a stricter configuration that enables additional
checks that would typically fail on incomplete stubs (such as `Unknown` checks).
In typeshed's CI, pyright is run with these configuration settings on a subset of
the stubs in typeshed (including the standard library).

## regr\_test.py

This test runs mypy against the test cases for typeshed's stdlib and third-party
stubs. See the README in the `test_cases` directory for more information about what
these test cases are for and how they work. Run `python tests/regr_test.py --help`
for information on the various configuration options.

## check\_consistent.py

Run using:
```
python3 tests/check_consistent.py
```

## stubtest\_stdlib.py

Run using
```
(.venv3)$ python3 tests/stubtest_stdlib.py
```

This test compares the stdlib stubs against the objects at runtime. Because of
this, the output depends on which version of Python and on what kind of system
it is run.
As such, if you run this test locally, it may complain about system-specific
differences (in e.g, `socket`) that the type system cannot capture or our stubtest settings
in CI do not account for. If you run into this issue, consider opening a draft PR and letting CI
test it automatically (or
[running the test via Github Actions](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow#running-a-workflow)
on your typeshed fork).

If you need a specific version of Python to repro a CI failure,
[pyenv](https://github.com/pyenv/pyenv) can also help.

Due to its dynamic nature, you may run into false positives. In this case, you
can add to the allowlists for each affected Python version in
`tests/stubtest_allowlists`. Please file issues for stubtest false positives
at [mypy](https://github.com/python/mypy/issues).

## stubtest\_third\_party.py

:warning: This script downloads and executes arbitrary code from PyPI. Only run
this script locally if you know you can trust the packages you're running
stubtest on.

Run using
```
(.venv3)$ python3 tests/stubtest_third_party.py
```

Similar to `stubtest_stdlib.py`, but tests the third party stubs. By default,
it checks all third-party stubs, but you can provide the distributions to
check on the command line:

```
(.venv3)$ python3 tests/stubtest_third_party.py Pillow toml  # check stubs/Pillow and stubs/toml
```

If you have the runtime package installed in your local virtual environment, you can also run stubtest
directly, with
```
(.venv3)$ MYPYPATH=<path-to-module-stubs> python3 -m mypy.stubtest \
  --custom-typeshed-dir <path-to-typeshed> \
  <third-party-module>
```

For each distribution, stubtest ignores definitions listed in a `@tests/stubtest_allowlist.txt` file,
relative to the distribution. Additional packages that are needed to run stubtest for a
distribution can be added to `@tests/requirements-stubtest.txt`.

### Using stubtest to find objects missing from the stubs

By default, stubtest emits an error if a public object is present at runtime
but missing from the stub. However, this behaviour can be disabled using the
`--ignore-missing-stub` option.

Many third-party stubs packages in typeshed are currently incomplete, and so by
default, `stubtest_third_party.py` runs stubtest with the
`--ignore-missing-stub` option to test our third-party stubs. However, this
option is not used if the distribution has `ignore_missing_stub = false` in the
`tool.stubtest` section of its `tests/METADATA.toml` file. This setting
indicates that the package is considered "complete", for example:
https://github.com/python/typeshed/blob/6950c3237065e6e2a9b64810765fec716252d52a/stubs/emoji/METADATA.toml#L3-L4

You can help make typeshed's stubs more complete by adding
`ignore_missing_stub = false` to the `tests/METADATA.toml` file for a
third-party stubs distribution, running stubtest, and then adding things that
stubtest reports to be missing to the stub. However, note that not *everything*
that stubtest reports to be missing should necessarily be added to the stub.
For some implementation details, it is often better to add allowlist entries
for missing objects rather than trying to match the runtime in every detail.

## typecheck\_typeshed.py

Run using
```
(.venv3)$ python3 tests/typecheck_typeshed.py
```

This is a small wrapper script that uses mypy to typecheck typeshed's own code in the
`scripts` and `tests` directories. Run `python tests/typecheck_typeshed.py --help` for
information on the various configuration options.
