# typeshed

[![Tests](https://github.com/python/typeshed/actions/workflows/tests.yml/badge.svg)](https://github.com/python/typeshed/actions/workflows/tests.yml)
[![Chat at https://gitter.im/python/typing](https://badges.gitter.im/python/typing.svg)](https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Pull Requests Welcome](https://img.shields.io/badge/pull%20requests-welcome-brightgreen.svg)](https://github.com/python/typeshed/blob/main/CONTRIBUTING.md)

## About

Typeshed contains external type annotations for the Python standard library
and Python builtins, as well as third party packages as contributed by
people external to those projects.

This data can e.g. be used for static analysis, type checking or type inference.

For information on how to use `typeshed`, read below.  Information for
contributors can be found in [CONTRIBUTING.md](CONTRIBUTING.md).  **Please read
it before submitting pull requests; do not report issues with annotations to
the project the stubs are for, but instead report them here to typeshed.**

Further documentation on stub files, typeshed, and Python's typing system in
general, can also be found at https://typing.readthedocs.io/en/latest/.

Typeshed fully supports Python versions 3.8 and up. Support for Python 3.7
is limited: see https://github.com/python/typeshed/issues/10113
for details.

## Using

If you're just using a type checker ([mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/), PyCharm, ...), as opposed to
developing it, you don't need to interact with the typeshed repo at
all: a copy of standard library part of typeshed is bundled with type checkers.
And type stubs for third party packages and modules you are using can
be installed from PyPI. For example, if you are using `six` and `requests`,
you can install the type stubs using

```bash
$ pip install types-six types-requests
```

These PyPI packages follow [PEP 561](http://www.python.org/dev/peps/pep-0561/)
and are automatically released (multiple times a day, when needed) by
[typeshed internal machinery](https://github.com/typeshed-internal/stub_uploader).

Type checkers should be able to use these stub packages when installed. For more
details, see the documentation for your type checker.

### Package versioning for third-party stubs

Version numbers of third-party stub packages consist of at least four parts.
All parts of the stub version, except for the last part, correspond to the
version of the runtime package being stubbed. For example, if the `types-foo`
package has version `1.1.2.0`, this signifies that the package contains stubs
for the `foo==1.1.2`. In this example, the final element of the version
indicates that this is the first revision of the stubs for `foo`. If an update
to the stubs was pushed (but the stubs were still aiming to provide
annotations for `foo==1.1.2`), then the version of `types-foo` would
increment to `1.1.2.1`.

At typeshed, we try to keep breaking changes to a minimum. However, due to the
nature of stubs, any version bump can introduce changes that might make your
code fail to type check.

There are several strategies available for specifying the version of a stubs
package you're using, each with its own tradeoffs

* Use the same pin that you use for the package being stubbed. For example,
  if you use `requests>=2.30.0,<2.32`, you can use
  `types-requests>=2.30.0,<2.32`. This ensures that the stubs are compatible
  with the package you are using, but it carries a small risk of breaking
  type checking due to changes in the stubs.

  Another risk of this strategy is that stubs often lag behind
  the package being stubbed. You might want to force the package being stubbed
  to a certain minimum version, because it fixes a critical bug, but you
  could be unable to update the stubs, since an update has not been released.
* Pin the stubs to a known good version and update manually. For example, if
  you use `types-requests==2.31.0.1`, you can be sure that upgrading
  dependencies will not break type checking. However, you will miss out on
  improvements in the stubs that could potentially improve type checking.
  It also has the risk that the stubs you are using are not compatible with
  the package being stubbed.
* Don't pin the stubs. This is the most flexible option, but it carries the
  risk that the stubs become incompatible with the package being stubbed.
  For example, if a new major version of the package is released, there's a
  chance the stubs might be updated to reflect the new version of the runtime
  package before you update the package being stubbed.

You can also use the different strategies as needed. For example, you could
default match the pinning, but pin the stubs to a known good version when
a problem arises that can't easily be fixed.

### The `_typeshed` package

typeshed includes a package `_typeshed` as part of the standard library.
This package and its submodules contains utility types, but is not
available at runtime. For more information about how to use this package,
[see the `stdlib/_typeshed` directory](https://github.com/python/typeshed/tree/main/stdlib/_typeshed).

## Discussion

If you've run into behavior in the type checker that suggests the type
stubs for a given library are incorrect or incomplete,
we want to hear from you!

Our main forum for discussion is the project's [GitHub issue
tracker](https://github.com/python/typeshed/issues).  This is the right
place to start a discussion of any of the above or most any other
topic concerning the project.

If you have general questions about typing with Python, or you need
a review of your type annotations or stubs outside of typeshed, head over to
[our discussion forum](https://github.com/python/typing/discussions).
For less formal discussion, try the typing chat room on
[gitter.im](https://gitter.im/python/typing).  Some typeshed maintainers
are almost always present; feel free to find us there and we're happy
to chat.  Substantive technical discussion will be directed to the
issue tracker.
