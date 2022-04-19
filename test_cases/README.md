## Regression tests for typeshed

This directory contains regression tests for the stubs found elsewhere in the
typeshed repo. Each file contains a number of test cases, all of which should
pass a type checker without error.

The internal structure of this directory should mimic typeshed as a whole.
However, unlike the rest of typeshed, this directory largely contains `.py`
files, because the purpose of this folder is to test the implications of
typeshed changes for end-users. For example, the stub for `builtins.pow` is
found in `stdlib/builtins.pyi`, and the regression tests for `pow` are found in
`test_cases/stdlib/test_builtins.py`.

100% test coverage for typeshed is neither necessary nor desirable, as it would
lead to unnecessary code duplication, and we have multiple other mechanisms for
spotting errors in the stubs. As such, this directory should only contain tests
for functions and classes which are known to have caused problems in the past,
and are difficult to get right.