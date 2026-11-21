# Contributing to typeshed

Welcome! typeshed is a community project that aims to work for a wide
range of Python users and Python codebases. If you're trying a type
checker on your Python code, your experience and what you can contribute
are important to the project's success.

## The contribution process at a glance

1. [Prepare your environment](#preparing-the-environment).
2. Find out [where to make your changes](#where-to-make-changes).
3. [Making your changes](#making-changes):
    * Small fixes and additions can be submitted directly as pull requests,
      but [contact us](README.md#discussion) before starting significant work.
    * Create your stubs, considering [what to include](#what-to-include) and
      conforming to the [coding style](https://typing.readthedocs.io/en/latest/guides/writing_stubs.html#style-guide).
4. Optionally [format and check your stubs](#stub-content-and-style).
5. Optionally [run the tests](tests/README.md).
6. [Submit your changes](#submitting-changes) by opening a pull request.
7. Make sure that all tests in CI are passing.

You can expect a reply within a few days, but please be patient when
it takes a bit longer. For more details, read below.

## Preparing the environment

### Code away!

Typeshed runs continuous integration (CI) on all pull requests. This means that
if you file a pull request (PR), our full test suite
-- including our linter, [`flake8-pyi`](https://github.com/pycqa/flake8-pyi) --
is run on your PR. It also means that bots will automatically apply
changes to your PR (using [Black](https://github.com/psf/black) and
[Ruff](https://github.com/astral-sh/ruff)) to fix any formatting issues.
This frees you up to ignore all local setup on your side, focus on the
code and rely on the CI to fix everything, or point you to the places that
need fixing.

### ... Or create a local development environment

If you prefer to run the tests and formatting locally, it's
possible too. Follow platform-specific instructions below.
For more information about our available tests, see
[tests/README.md](tests/README.md).

Whichever platform you're using, you will need a
virtual environment. If you're not familiar with what it is and how it works,
please refer to this
[documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Note that some tests require extra setup steps to install the required dependencies.

<table>
<tr>
  <td>Linux / macOS / WSL</td>
  <td>

  To install the necessary requirements, run the following commands from a
  terminal window:

  ```bash
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  (.venv)$ pip install -U pip
  (.venv)$ pip install -r requirements-tests.txt
  ```

  </td>
</tr>
<tr><!-- disables zebra striping --></tr>
<tr>
  <td>Windows</td>
  <td>

  Run the following commands from a Windows terminal to install all requirements:

  ```powershell
  > py -m venv .venv
  > .venv\Scripts\activate
  (.venv) > python -m pip install -U pip
  (.venv) > pip install -r requirements-tests.txt
  ```

  </td>
</tr>
<tr><!-- disables zebra striping --></tr>
<tr>
  <td>Using uv</td>
  <td>

  If you already have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, you can simply replace the commands above with:

  ```shell
  uv venv
  uv pip install -r requirements-tests.txt
  ```

  </td>
</tr>
</table>

## Where to make changes

### Standard library stubs

The `stdlib` directory contains stubs for modules in the
Python standard library — which
includes pure Python modules, dynamically loaded extension modules,
hard-linked extension modules, and the builtins. The `VERSIONS` file lists
the versions of Python where the module is available.

We accept changes for future versions of Python after the first beta for that
version was released. We drop support for a Python version three months
after it reaches [end-of-life](https://devguide.python.org/versions/). This
means that we will no longer actively test the stubs against that version.
After six months, we will remove the stubs for that version and start
to use syntax and typing features not supported by that version.

### Third-party library stubs

We accept stubs for third-party packages into typeshed as long as:
* the package is publicly available on the [Python Package Index](https://pypi.org/);
* the package supports any Python version supported by typeshed; and
* the package does not ship with its own stubs or type annotations.

The fastest way to generate new stubs is to use `scripts/create_baseline_stubs.py` (see below).

Stubs for third-party packages go into the `stubs` directory. Each subdirectory
there represents a PyPI distribution, and contains the following:
* `METADATA.toml`, describing the package. See below for details.
* Stubs (i.e. `*.pyi` files) for packages and modules that are shipped in the
  source distribution.
* (Rarely) some docs specific to a given type stub package in `README` file.

When a third-party stub is added or
modified, an updated version of the corresponding distribution will be
automatically uploaded to PyPI within a few hours.
Each time this happens the least significant
version level is incremented. For example, if `stubs/foo/METADATA.toml` has
`version = "x.y"` the package on PyPI will be updated from `types-foo-x.y.n`
to `types-foo-x.y.n+1`.

*Note:* In its current implementation, typeshed cannot contain stubs for
multiple versions of the same third-party library.  Prefer to generate
stubs for the latest version released on PyPI at the time of your
stubbing.

#### The `METADATA.toml` file

Each third-party stub package must have a metadata file to describe the
package. For example, the metadata for a package `parrot` lives in
`stubs/parrot/METADATA.toml`. See
[docs/metadata-files.md](./docs/metadata-files.md) for a full description.

### Dependencies

When a third-party stub package depends on another package, there are several
strategies available, depending on whether the other package is typed.

1. If the other package is typed and includes a `py.typed` marker, add that
    package to the `dependencies` key in `METADATA.toml`. This might fail the
    stub uploader checks, in which case you can ask the maintainers for help.
2. Otherwise, if a type package is available, add that package to the
    `dependencies` key. If the type package originates from typeshed, the
    stub uploader checks should succeed.
3. In case the dependency in untyped and no stubs are available, you may stub
    the dependency in your type stubs. For example:

    ```python
    from typing import Any
    # from fruzzle import Frobnicator  # won't work

    _Frobnicator: TypeAlias = Any  # actually fruzzle.Frobnicator
    ```

    In more complex or advanced cases you may instead opt to add a stubs
    is a separate helper package:

    ```python
    # stubs/my-stubs/my_stubs/_fruzzle.pyi

    # Utility stubs for the untyped "fruzzle" package.

    from typing import Any, Protocol

    Frobnicator: TypeAlias = Any

    class Flubberer(Protocol):
        def flubb_it(self, x: int, /) -> str: ...
    ```

## Making Changes

### Before you begin

If your change will be a significant amount of work to write, we highly
recommend starting by opening an issue laying out what you want to do.
That lets a conversation happen early in case other contributors disagree
with what you'd like to do or have ideas that will help you do it.

### Stub Content and Style

Each Python module is represented by a .pyi "stub file". This is a syntactically valid Python file, where all methods are empty and [type annotations](https://typing.readthedocs.io/en/latest/spec/annotations.html) are used to describe function signatures and variable types.

Typeshed follows the standard type system guidelines for [stub content](https://typing.readthedocs.io/en/latest/guides/writing_stubs.html#stub-content) and [coding style](https://typing.readthedocs.io/en/latest/guides/writing_stubs.html#style-guide).

The code is formatted using [`Black`](https://github.com/psf/black).
Various other autofixes and lint rules are
also performed by [`Ruff`](https://github.com/astral-sh/ruff) and
[`Flake8`](https://github.com/pycqa/flake8),
with plugin [`flake8-pyi`](https://github.com/pycqa/flake8-pyi).

The repository is equipped with a [pre-commit.ci](https://pre-commit.ci/)
configuration file. This means that you don't *need* to do anything yourself to
run the code formatters or linters. When you push a commit, a bot will run
those for you right away and add any autofixes to your PR. Anything
that can't be autofixed will show up as a CI failure, hopefully with an error
message that will make it clear what's gone wrong.

That being said, if you *want* to run the formatters and linters locally
when you commit, you're free to do so. To use the same configuration as we use
in CI, we recommend doing this via pre-commit:

```bash
(.venv)$ pre-commit run --all-files
```

### What to include

Stubs should include the complete interface (classes, functions,
constants, etc.) of the module they cover, but it is not always
clear exactly what is part of the interface.

The following should always be included:
- All objects listed in the module's documentation.
- All objects included in ``__all__`` (if present).

Other objects may be included if they are being used in practice
or if they are not prefixed with an underscore. This means
that typeshed will generally accept contributions that add missing
objects, even if they are undocumented. Undocumented objects should
be marked with a comment of the form ``# undocumented``.

### Incomplete Annotations

When submitting new stubs, it is not necessary to annotate all arguments,
return types, and fields. Such items should either be left unannotated or
use `_typeshed.Incomplete` if this is not possible:

```python
from _typeshed import Incomplete

field: Incomplete  # unannotated

def foo(x): ...  # unannotated argument and return type
```

`Incomplete` can also be used for partially known types:

```python
def foo(x: Incomplete | None) -> list[Incomplete]: ...
```

### What to do when a project's documentation and implementation disagree

Type stubs are meant to be external type annotations for a given
library.  While they are useful documentation in their own right, they
augment the project's concrete implementation, not the project's
documentation.  Whenever you find them disagreeing, model the type
information after the actual implementation and file an issue on the
project's tracker to fix their documentation.

### Byte Types

[PEP 688](https://www.python.org/dev/peps/pep-0688/) removes
the implicit promotion from `bytearray` and `memoryview` to `bytes`.
Typeshed stubs should be written assuming that these promotions
do not happen, so a parameter that accepts either `bytes` or
`bytearray` should be typed as `bytes | bytearray`.
Often one of the aliases from `_typeshed`, such as
`_typeshed.ReadableBuffer`, can be used instead.

### Deprecations (using the `@deprecated` decorator)

Generally deprecactions using the `@deprecated` decorator are added more
liberally in typeshed than runtime deprecation warnings. Here are some
guidelines that can be deviated from in special cases.

Use `@deprecated` if and only if

- a feature is deprecated at runtime (either using `@deprecated` or with a
  runtime warning); or
- a feature is documented to be deprecated (e.g. in API documentation,
  docstrings, or comments).

For standard library features that are not deprecated in all Python versions
currently supported by typeshed use `@deprecated` for

- all versions starting with the "Deprecated since" version, plus
- all versions for which an alternative is available.

### Docstrings

Typeshed stubs should not include duplicated docstrings from the source code.

### Auto-generating stub files

Typeshed includes `scripts/create_baseline_stubs.py`.
It generates stubs automatically using a tool called
[stubgen](https://mypy.readthedocs.io/en/latest/stubgen.html) that comes with mypy.

To get started, fork typeshed, clone your fork, and then
[create a virtualenv](#-or-create-a-local-development-environment).
You can then install the library with `pip` into the virtualenv and run the script below,
replacing `$INSERT_LIBRARY_NAME_HERE` with the name of the library:

```bash
(.venv)$ pip install $INSERT_LIBRARY_NAME_HERE
(.venv)$ python3 scripts/create_baseline_stubs.py $INSERT_LIBRARY_NAME_HERE
```

When the script has finished running, it will print instructions telling you what to do next.

If it has been a while since you set up the virtualenv, make sure you have
the latest mypy (`pip install -r requirements-tests.txt`) before running the script.

### Unsupported Type System Features

Unless listed here, all type system features that have been added to the
[Python typing specification](https://typing.python.org/en/latest/spec/)
can be used. The following features are *not* supported:

- [PEP 695](https://peps.python.org/pep-0695/) type parameter syntax.
  (See [issue #10869](https://github.com/python/typeshed/issues/10869).) Use
  explicit `TypeVar` definitions.
- [PEP 695](https://peps.python.org/pep-0695/) type statement for aliases.
  (See [issue #10870](https://github.com/python/typeshed/issues/10870).) Use
  `TypeAlias` annotations.

Features from the `typing` module that are not present in all
supported Python versions must be imported from `typing_extensions`
instead in typeshed stubs. This currently affects:

- `Self` (new in Python 3.11)
- `Never` (new in Python 3.11)
- `LiteralString` (new in Python 3.11)
- `TypeVarTuple` and `Unpack` (new in Python 3.11)
- `Required` and `NotRequired` (new in Python 3.11)
- `Buffer` (new in Python 3.12; in the `collections.abc` module)
- `@deprecated` (new in Python 3.13; in the `warnings` module)
- `TypeForm` (new in Python 3.15)

## Submitting Changes

Even more excellent than a good bug report is a fix for a bug, or the
implementation of a much-needed stub. We'd love to have
your contributions.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the
mechanics, see [Mypy's git and GitHub workflow help page](https://github.com/python/mypy/wiki/Using-Git-And-GitHub),
or [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

Anyone interested in type stubs may review your code.  One of the
maintainers will merge your pull request when they think it's ready.
For every pull request, we aim to promptly either merge it or say why
it's not yet ready; if you go a few days without a reply, please feel
free to ping the thread by adding a new comment.

To get your pull request merged sooner, you should explain why you are
making the change. For example, you can point to a code sample that is
processed incorrectly by a type checker. It is also helpful to add
links to online documentation or to the implementation of the code
you are changing.

As the author of the pull request, it is your responsibility to make
sure all CI tests pass and that any feedback is addressed. The typeshed
maintainers will probably provide some help and may even push changes
to your PR to fix any minor issues, but this is not always possible.
If a PR lingers with unresolved problems for too long, we may close it
([see below](#closing-stale-prs)).

Also, do not squash your commits, force push, or use `git commit --amend` after
you have submitted a pull request, as this
erases context during review. We will squash commits when the pull request is merged.
This way, your pull request will appear as a single commit in our git history, even
if it consisted of several smaller commits.

## Third-party library removal policy

Third-party stubs are generally removed from typeshed when one of the
following criteria is met:

* The upstream package ships a `py.typed` file for at least six months,
  and the upstream type annotations are of a comparable standard to those in
  typeshed, or
* the upstream package was declared or appears to be unmaintained, and
  retaining the stubs causes maintenance issues in typeshed.

Case 1: If a package ships its own `py.typed` file, please follow these steps:

1. Make sure **stubsabot** open a PR that sets the `obsolete-since` field in the
   `METADATA.toml` file to the first version of the package that shipped `py.typed`.
2. After at least six months, make sure **stubsabot** open a PR to remove the stubs.

Case 2: If third-party stubs should be removed for other reasons, please follow
these steps:

1. Open an issue explaining why the stubs should be removed.
2. A maintainer will add the
   ["stubs: removal" label](https://github.com/python/typeshed/labels/stubs%3A%20removal).
3. Open a PR that sets the `no-longer-updated` field in the `METADATA.toml`
   file to `true`.
4. When a new version of the package was automatically uploaded to PyPI (which
   can take up to a day), make sure **stubsabot** open a PR to remove the stubs.

If feeling kindly, please update [mypy](https://github.com/python/mypy/blob/master/mypy/stubinfo.py)
for any stub obsoletions or removals.

### Marking PRs as "deferred"

We sometimes use the ["status: deferred" label](https://github.com/python/typeshed/labels/status%3A%20deferred)
to mark PRs and issues that we'd like to accept, but that are blocked by some
external factor. Blockers can include:

- An unambiguous bug in a type checker (i.e., a case where the
  type checker is not implementing [the typing spec](https://typing.readthedocs.io/en/latest/spec/index.html)).
- A dependency on a typing PEP that is still under consideration.
- A pending change in a related project, such as stub-uploader.

### Closing stale PRs

To keep the number of open PRs manageable, we may close PRs when they have been
open for too long. Specifically, we close open PRs that either have failures in CI,
serious merge conflicts or unaddressed feedback, and that have not seen any
activity in three months.

## Further Documentation

See [docs/README.md](./docs/README.md) for an overview of all documentation
available for typeshed.
