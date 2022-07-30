## Regression tests for typeshed

This directory contains regression tests for the stubs found elsewhere in the
typeshed repo. Each file contains a number of test cases, all of which should
pass a type checker without error.

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
`collections.abc.Callable`, and `re.Match` instead of `typing.Match` (etc.).
