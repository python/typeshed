# typeshed

[![Build status](https://github.com/python/typeshed/workflows/Check%20stubs/badge.svg)](https://github.com/python/typeshed/actions?query=workflow%3A%22Check+stubs%22)
[![Chat at https://gitter.im/python/typing](https://badges.gitter.im/python/typing.svg)](https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Pull Requests Welcome](https://img.shields.io/badge/pull%20requests-welcome-brightgreen.svg)](https://github.com/python/typeshed/blob/master/CONTRIBUTING.md)

## About

Typeshed contains external type annotations for the Python standard library
and Python builtins, as well as third party packages as contributed by
people external to those projects.

This data can e.g. be used for static analysis, type checking or type inference.

For information on how to use `typeshed`, read below.  Information for
contributors can be found in [CONTRIBUTING.md](CONTRIBUTING.md).  **Please read
it before submitting pull requests; do not report issues with annotations to
the project the stubs are for, but instead report them here to typeshed.**

Typeshed supports Python versions 2.7 and 3.6 and up.

## Using

If you're just using mypy (or pytype or PyCharm), as opposed to
developing it, you don't need to interact with the typeshed repo at
all: a copy of standard library part of typeshed is bundled with mypy.
And type stubs for third party packages and modules you are using can
be installed from PyPI. For example, if you are using `six` and `requests`,
you can install the type stubs using

    $ pip install types-six types-requests

These PyPI packages follow [PEP 561](http://www.python.org/dev/peps/pep-0561/)
and are automatically generated by typeshed internal machinery. Also starting
from version 0.900 mypy will provide an option to automatically install missing
type stub packages (if found on PyPI).

PyCharm, pytype etc. work in a similar way, for more details see documentation
for the type-checking tool you are using.

## Discussion

If you've run into behavior in the type checker that suggests the type
stubs for a given library are incorrect or incomplete,
we want to hear from you!

Our main forum for discussion is the project's [GitHub issue
tracker](https://github.com/python/typeshed/issues).  This is the right
place to start a discussion of any of the above or most any other
topic concerning the project.

For less formal discussion, try the typing chat room on
[gitter.im](https://gitter.im/python/typing).  Some Mypy core developers
are almost always present; feel free to find us there and we're happy
to chat.  Substantive technical discussion will be directed to the
issue tracker.

## Issue-tracker conventions

We aim to reply to all new issues promptly.  We'll assign one or more
labels to indicate we've triaged an issue, but most typeshed issues
are relatively simple (stubs for a given module or package are
missing, incomplete or incorrect) and we won't add noise to the
tracker by labeling all of them.  Please see the
[list of all labels](https://github.com/python/typeshed/issues/labels)
for a detailed description of the labels we use.

Sometimes a PR can't make progress until some external issue is
addressed.  We indicate this by editing the subject to add a ``[WIP]``
prefix.  (This should be removed before committing the issue once
unblocked!)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.
If you have questions related to contributing, drop by the [typing Gitter](https://gitter.im/python/typing).

## Running the tests

The tests are automatically run on every PR and push to the repo.
Therefore you don't need to run them locally, unless you want to run
them before making a pull request or you want to debug some problem without
creating several small commits.

There are several tests:
- `tests/mypy_test.py`
tests typeshed with [mypy](https://github.com/python/mypy/)
- `tests/pytype_test.py` tests typeshed with
[pytype](https://github.com/google/pytype/).
- `tests/pyright_test.py` tests typeshed with
[pyright](https://github.com/microsoft/pyright).
- `tests/mypy_test_suite.py` runs a subset of mypy's test suite using this version of
typeshed.
- `tests/check_consistent.py` checks certain files in typeshed remain
consistent with each other.
- `tests/stubtest_test.py` checks stubs against the objects at runtime.
- `flake8` enforces a style guide.

### Setup

Run:
```
$ python3 -m venv .venv3
$ source .venv3/bin/activate
(.venv3)$ pip install -U pip
(.venv3)$ pip install -r requirements-tests-py3.txt
```
This will install mypy (you need the latest master branch from GitHub),
typed-ast, flake8 (and plugins), pytype, black and isort.

If you want to run the pyright tests, you need to have
[Node.js](https://nodejs.org/) installed.

### mypy_test.py

This test requires Python 3.6 or higher; Python 3.6.1 or higher is recommended.
Run using:
```
(.venv3)$ python3 tests/mypy_test.py
```

This test is shallow — it verifies that all stubs can be
imported but doesn't check whether stubs match their implementation
(in the Python standard library or a third-party package). It has an exclude list of
modules that are not tested at all, which also lives in the tests directory.

You can restrict mypy tests to a single version by passing `-p2` or `-p3.9`:
```bash
(.venv3)$ python3 tests/mypy_test.py -p3.9
```

### pytype_test.py

This test requires Python 2.7 and Python 3.6. Pytype will
find these automatically if they're in `PATH`, but otherwise you must point to
them with the `--python27-exe` and `--python36-exe` arguments, respectively.
Run using:
```
(.venv3)$ python3 tests/pytype_test.py
```

This test works similarly to `mypy_test.py`, except it uses `pytype`.

### pyright\_test.py

This test requires Node.js to be installed. It is currently not part of the CI,
but it uses the same pyright version and configuration as the CI.
```
(.venv3)$ python3 tests/pyright_test.py                 # Check all files
(.venv3)$ python3 tests/pyright_test.py stdlib/sys.pyi  # Check one file
```

### mypy\_test\_suite.py

This test requires Python 3.5 or higher; Python 3.6.1 or higher is recommended.
Run using:
```
(.venv3)$ python3 tests/mypy_test_suite.py
```

This test runs mypy's own test suite using the typeshed code in your repo. This
will sometimes catch issues with incorrectly typed stubs, but is much slower
than the other tests.

### check_consistent.py

Run using:
```
python3 tests/check_consistent.py
```

### stubtest_test.py

This test requires Python 3.6 or higher.
Run using
```
(.venv3)$ python3 tests/stubtest_test.py
```

This test compares the stdlib stubs against the objects at runtime. Because of
this, the output depends on which version of Python and on what kind of system
it is run.
Thus the easiest way to run this test is via Github Actions on your fork;
if you run it locally, it'll likely complain about system-specific
differences (in e.g, `socket`) that the type system cannot capture.
If you need a specific version of Python to repro a CI failure,
[pyenv](https://github.com/pyenv/pyenv) can help.

Due to its dynamic nature, you may run into false positives. In this case, you
can add to the whitelists for each affected Python version in
`tests/stubtest_whitelists`. Please file issues for stubtest false positives
at [mypy](https://github.com/python/mypy/issues).

To run stubtest against third party stubs, it's easiest to use stubtest
directly, with
```
(.venv3)$ python3 -m mypy.stubtest \
  --custom-typeshed-dir <path-to-typeshed> \
  <third-party-module>
```
stubtest can also help you find things missing from the stubs.


### flake8

flake8 requires Python 3.6 or higher. Run using:
```
(.venv3)$ flake8
```

Note typeshed uses the `flake8-pyi` and `flake8-bugbear` plugins.
