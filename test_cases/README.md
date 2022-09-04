## Regression tests for typeshed

This directory contains regression tests for the stubs found elsewhere in the
typeshed repo.

**This directory should *only* contain tests for functions and classes which
are known to have caused problems in the past, where the stubs are difficult to
get right.** 100% test coverage for typeshed is neither necessary nor
desirable, as it would lead to code duplication. Moreover, typeshed has
multiple other mechanisms for spotting errors in the stubs.

### The purpose of these tests

Different tests in this directory serve different purposes. For some stubs in
typeshed, the type annotations are complex enough that it's useful to have
basic sanity checks that test whether a type checker understands the intent of
the annotations correctly. Examples of tests like these are
`stdlib/builtins/test_pow.py` and `stdlib/asyncio/test_gather.py`.

Other tests, such as the tests for `ExitStack` in `stdlib/test_contextlib.py`
and the tests for `LogRecord` in `stdlib/test_logging.py`, do not relate to
stubs where the annotations are particularly complex, but they *do* relate to
stubs where decisions have been taken that might be slightly unusual. These
tests serve a different purpose: to check that type checkers do not emit
false-positive errors for idiomatic usage of these classes.

### How the tests work

Some files in this directory simply contain samples of idiomatic Python, which
should not (if the stubs are correct) cause a type checker to emit any errors.

Many test cases also make use of
[`assert_type`](https://docs.python.org/3.11/library/typing.html#typing.assert_type),
a function which allows us to test whether a type checker's inferred type of an
expression is what we'd like it be.

Finally, some tests make use of `# type: ignore` comments (in combination with
mypy's
[`--warn-unused-ignores`](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-warn-unused-ignores)
setting and pyright's
[`reportUnnecessaryTypeIgnoreComment`](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#type-check-diagnostics-settings)
setting) to test instances where a type checker *should* emit some kind of
error, if the stubs are correct. Both settings are enabled by default for the entire
subdirectory.

For more information on using `assert_type` and
`--warn-unused-ignores`/`reportUnnecessaryTypeIgnoreComment` to test type
annotations,
[this page](https://typing.readthedocs.io/en/latest/source/quality.html#testing-using-assert-type-and-warn-unused-ignores)
provides a useful guide.

### Naming convention

Use the same top-level name for the module / package you would like to test.
Use `test_${thing}.py` naming pattern for individual test files.

By default, tests go into a test file with the same name as the stub file, prefixed with `test_`.
For example: `stdlib/test_contextlib.py`.

If that file becomes too big, we instead create a directory with files named after individual objects being tested.
For example: `stdlib/builtins/test_dict.py`.

### Differences to the rest of typeshed

Unlike the rest of typeshed, this directory largely contains `.py` files. This
is because the purpose of this folder is to test the implications of typeshed
changes for end users.

Another difference to the rest of typeshed is that the test cases in this
directory cannot always use modern syntax for type hints.

For example, PEP 604
syntax (unions with a pipe `|` operator) is new in Python 3.10. While this
syntax can be used on older Python versions in a `.pyi` file, code using this
syntax will fail at runtime on Python <=3.9. Since the test cases all use `.py`
extensions, and since the tests need to pass on all Python versions >=3.7, PEP
604 syntax cannot be used in a test case. Use `typing.Union` and
`typing.Optional` instead.

PEP 585 syntax can also not be used in the `test_cases` directory. Use
`typing.Tuple` instead of `tuple`, `typing.Callable` instead of
`collections.abc.Callable`, and `typing.Match` instead of `re.Match` (etc.).
