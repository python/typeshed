# typeshed

[![Tests](https://github.com/python/typeshed/actions/workflows/tests.yml/badge.svg)](https://github.com/python/typeshed/actions/workflows/tests.yml)
[![Chat at https://gitter.im/python/typing](https://badges.gitter.im/python/typing.svg)](https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Pull Requests Welcome](https://img.shields.io/badge/pull%20requests-welcome-brightgreen.svg)](https://github.com/python/typeshed/blob/main/CONTRIBUTING.md)

## About

Typeshed is a repository containing external type annotations for the Python standard library, Python builtins, and third-party packages contributed by individuals external to those projects. 
  
> **These data are used for purposes such as static analysis, type checking, and type inference.**

For information on how to use `typeshed`, read below.  Information for
contributors can be found in [CONTRIBUTING.md](CONTRIBUTING.md).  **Before submitting pull requests, we kindly request that you read this document. If you encounter issues with annotations, please report them here to typeshed rather than the project for which the stubs are intended.**

Further documentation on stub files, typeshed, and Python's typing system in
general, can also be found at https://typing.readthedocs.io/en/latest/.

Typeshed fully supports Python versions 3.8 and up. Support for Python 3.7
is limited: see https://github.com/python/typeshed/issues/10113
for details.

---

## Using

If you're just using a type checker ([mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/) or PyCharm, ...), and not developing it, you do not need to interact directly with the typeshed repository. A copy of the standard library portion of typeshed is typically bundled with type checkers. Additionally, you can install type stubs for third-party packages and modules from PyPI. For instance, if you are using `six` and `requests`, you can install the type stubs using the following command:

```bash
$ pip install types-six types-requests
```

These PyPI packages adhere to [PEP 561](http://www.python.org/dev/peps/pep-0561/)
and are automatically released (multiple times a day, when needed) by
[typeshed internal machinery](https://github.com/typeshed-internal/stub_uploader).

Type checkers should be able to use these stub packages when installed. For more
details, see the documentation for your type checker.

---
### The `_typeshed` package

typeshed includes a package `_typeshed` as part of the standard library.
This package and its submodules contain utility types but are not
available at runtime. For more information about how to use this package,
[see the `stdlib/_typeshed` directory](https://github.com/python/typeshed/tree/main/stdlib/_typeshed).

---
## Discussion

If you encounter behavior in your type checker that suggests the type stubs for a particular library are incorrect or incomplete, we encourage you to share your feedback with us.

Our primary platform for discussion is the project's [GitHub issue
tracker](https://github.com/python/typeshed/issues).  This is the appropriate place to initiate discussions on any topics related to the project.

If you have general questions about typing with Python or need a review of your type annotations or stubs outside of typeshed, please visit
[our discussion forum](https://github.com/python/typing/discussions).
For less formal discussions, you can join the typing chat room on
[gitter.im](https://gitter.im/python/typing).  Some typeshed maintainers
are almost always present; feel free to find us there and we're happy
to chat.  Substantive technical discussion will be redirected to the
issue tracker.
