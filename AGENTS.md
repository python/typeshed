# typeshed - Python type stub repository

typeshed contains [type stubs](https://typing.python.org/en/latest/spec/distributing.html)
for Python's standard library as well as for some packages available on
[PyPI](https://pypi.org/) that don't provide their own type annotations.

## Directory Structure

- `stdlib/` - Python standard library stubs
- `stubs/` - PyPI package stubs, one directory per package
- `scripts`/ - utility scripts
- `tests/` - scripts for various tests, see `tests/README.md`
- `lib/` - utility modules used by multiple scripts

## Running tests

To run all tests, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-tests.txt
python tests/runtests.py <path>
```

`<path>` is either:

- `stdlib/<stub>.pyi`
- `stubs/<package>`

See `tests/README.md` for more information about running tests.

## Pull Requests

When opening pull requests, do the following:

- Follow the guidance from `CONTRIBUTING.md`.
- Run the tests as described above before submitting.
- Don't include tests for .pyi files, unless the situation is complex. See
  `tests/REGRESSION.md`.
