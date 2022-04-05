# Contributing to typeshed

Welcome!  typeshed is a community project that aims to work for a wide
range of Python users and Python codebases.  If you're trying a type
checker on your Python code, your experience and what you can contribute
are important to the project's success.


## The contribution process at a glance

1. [Prepare your environment](#preparing-the-environment).
2. Find out [where to make your changes](#where-to-make-changes).
3. [Prepare your changes](#preparing-changes):
    * Small fixes and additions can be submitted directly as pull requests,
      but [contact us](README.md#discussion) before starting significant work.
    * Create your stubs, considering [what to include](#what-to-include) and
      conforming to the [coding style](#stub-file-coding-style).
4. [Format and check your stubs](#formatting-stubs).
5. Optionally [run the tests](tests/README.md).
6. [Submit your changes](#submitting-changes) by opening a pull request.

You can expect a reply within a few days, but please be patient when
it takes a bit longer. For more details, read below.

## Preparing the environment

### Code away!

Typeshed runs continuous integration (CI) on all pull requests. This will
automatically fix formatting (using `black`, `isort`) and run tests.
It means you can ignore all local setup on your side, focus on the
code and rely on the CI to fix everything, or point you to the places that
need fixing.

### ... Or create a local development environment

If you prefer to run the tests & formatting locally, it's
possible too. Follow platform-specific instructions below.
For more information about our available tests, see
[tests/README.md](tests/README.md).

Whichever platform you're using, you will need a
virtual environment. If you're not familiar with what it is and how it works,
please refer to this
[documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

### Linux/Mac OS

On Linux and Mac OS, you will be able to run the full test suite on Python 3.8
or 3.9. Running the tests on <=3.7 is not supported, and the pytype tests
[cannot currently be run on Python 3.10](https://github.com/google/pytype/issues/1022).

To install the necessary requirements, run the following commands from a
terminal window:

```
$ python3 -m venv .venv3
$ source .venv3/bin/activate
(.venv3)$ pip install -U pip
(.venv3)$ pip install -r requirements-tests.txt
```

### Windows

If you are using a Windows operating system, you will not be able to run the
full test suite. One option is to install
[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/faq),
which will allow you to run the full suite of tests. If you choose to install
WSL, follow the Linux/Mac OS instructions above.

If you do not wish to install WSL, you will not be able to run the pytype
tests, as pytype
[does not currently support running on Windows](https://github.com/google/pytype#requirements).
However, the upside of this is that you will be able to run all
Windows-compatible tests on Python 3.9, 3.8 or 3.10, as it is only the pytype
tests that cannot currently be run on 3.10.

To install all non-pytype requirements on Windows without WSL, run the
following commands from a Windows terminal:

```
> python3 -m venv .venv3
> ".venv3/Scripts/activate"
(.venv3) > python -m pip install -U pip
(.venv3) > python -m pip install -r requirements-tests.txt
```

## Code formatting

The code is formatted by `black` and `isort`.

The repository is equipped with a [`pre-commit.ci`](https://pre-commit.ci/)
configuration file. This means that you don't *need* to do anything yourself to
run the code formatters. When you push a commit, a bot will run those for you
right away and add a commit to your PR. Neat, no?

That being said, if you *want* to run the checks locally when you commit, you
can install the hooks: please refer to the [pre-commit](https://pre-commit.com/)
documentation.

## Where to make changes

### Standard library stubs

The `stdlib` directory contains stubs for modules in the
Python 3 standard library — which
includes pure Python modules, dynamically loaded extension modules,
hard-linked extension modules, and the builtins. The `VERSIONS` file lists
the versions of Python where the module is available.

Stubs for Python 2 are available in the `stdlib/@python2` subdirectory.
Modules that are only available for Python 2 are not listed in `VERSIONS`.

### Third-party library stubs

We accept stubs for third-party packages into typeshed as long as:
* the package is publicly available on the [Python Package Index](https://pypi.org/);
* the package supports any Python version supported by typeshed; and
* the package does not ship with its own stubs or type annotations.

The fastest way to generate new stubs is to use `scripts/create_baseline_stubs.py` (see below).

Stubs for third-party packages
go into `stubs`. Each subdirectory there represents a PyPI distribution, and
contains the following:
* `METADATA.toml`, describing the package. See below for details.
* Stubs (i.e. `*.pyi` files) for packages and modules that are shipped in the
  source distribution.
* (Rarely) some docs specific to a given type stub package in `README` file.

When a third party stub is added or
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

The metadata file describes the stubs package using the
[TOML file format](https://toml.io/en/). Currently, the following keys are
supported:

* `version`: The versions of the library that the stubs support. Two
  formats are supported:
    - A concrete version. This is especially suited for libraries that
      use [Calendar Versioning](https://calver.org/).
    - A version range ending in `.*`. This is suited for libraries that
      reflect API changes in the version number only, where the API-independent
      part is represented by the asterisk. In the case
      of [Semantic Versioning](https://semver.org/), this version could look
      like this: `2.7.*`.
  When the stubs are updated to a newer version
  of the library, the version of the stub should be bumped (note that
  previous versions are still available on PyPI).
* `python2` (default: `false`): If set to `true`, the top-level stubs
  support both Python 2 and Python 3.
* `requires` (optional): A list of other stub packages or packages with type
  information that are imported by the stubs in this package. Only packages
  generated by typeshed or required by the upstream package are allowed to
  be listed here, for security reasons.
* `extra_description` (optional): Can be used to add a custom description to
  the package's long description. It should be a multi-line string in
  Markdown format.
* `obsolete_since` (optional): This field is part of our process for
  [removing obsolete third-party libraries](#third-party-library-removal-policy).
  It contains the first version of the corresponding library that ships
  its own `py.typed` file.
* `stubtest` (default: `true`): Whether stubtest should be run against this
  package. Please avoid setting this to `false`, and add a comment if you have
  to.
* `stubtest_apt_dependencies` (default: `[]`): A list of Ubuntu APT packages
  that need to be installed for stubtest to run successfully. These are
  usually packages needed to pip install the implementation distribution.

The format of all `METADATA.toml` files can be checked by running
`python3 ./tests/check_consistent.py`.


## Preparing Changes

### Before you begin

If your change will be a significant amount of work to write, we highly
recommend starting by opening an issue laying out what you want to do.
That lets a conversation happen early in case other contributors disagree
with what you'd like to do or have ideas that will help you do it.

### Format

Each Python module is represented by a `.pyi` "stub file".  This is a
syntactically valid Python file, although it usually cannot be run by
Python 3 (since forward references don't require string quotes).  All
the methods are empty.

Python function annotations ([PEP 3107](https://www.python.org/dev/peps/pep-3107/))
are used to describe the signature of each function or method.

See [PEP 484](http://www.python.org/dev/peps/pep-0484/) for the exact
syntax of the stub files and [below](#stub-file-coding-style) for the
coding style used in typeshed.

### Auto-generating stub files

Typeshed includes `scripts/create_baseline_stubs.py`.
It generates stubs automatically using a tool called
[stubgen](https://mypy.readthedocs.io/en/latest/stubgen.html) that comes with mypy.

To get started, fork typeshed, clone your fork, and then
[create a virtualenv](#-or-create-a-local-development-environment).
You can then install the library with `pip` into the virtualenv and run the script,
replacing `libraryname` with the name of the library below:

```
(.venv3)$ pip install libraryname
(.venv3)$ python3 scripts/create_baseline_stubs.py libraryname
```

When the script has finished running, it will print instructions telling you what to do next.

If it has been a while since you set up the virtualenv, make sure you have
the latest mypy (`pip install -r requirements-tests.txt`) before running the script.

## Stub Content

Please see [the typing documentation](https://typing.readthedocs.io/en/latest/source/stubs.html)
for type system features supported in stubs, best practices, and our
style guide.

## Formatting stubs

Stubs should be reformatted with the formatters
[black](https://github.com/psf/black) and
[isort](https://github.com/PyCQA/isort) before submission. They
should also be checked for common problems by using
[flake8](https://flake8.pycqa.org/en/latest/) and the flake8 plugins
[flake8-pyi](https://github.com/ambv/flake8-pyi) and
[flake8-bugbear](https://github.com/PyCQA/flake8-bugbear).
All of these packages have been installed if you followed the
[setup instructions above](#preparing-the-environment).

To format and check your stubs, run the following commands:

```
(.venv3)$ black stdlib stubs
(.venv3)$ isort stdlib stubs
(.venv3)$ flake8
```


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

Also, do not squash your commits or use `git commit --amend` after you have submitted a pull request, as this
erases context during review. We will squash commits when the pull request is merged.
This way, your pull request will appear as a single commit in our git history, even
if it consisted of several smaller commits.

## Third-party library removal policy

Third-party packages are generally removed from typeshed when one of the
following criteria is met:

* The upstream package ships a `py.typed` file for at least six months, or
* the package does not support any of the Python versions supported by
  typeshed.

If a package ships its own `py.typed` file, please follow these steps:

1. Open an issue with the earliest month of removal in the subject.
2. A maintainer will add the
   ["removal" label](https://github.com/python/typeshed/labels/removal).
3. Open a PR that sets the `obsolete_since` field in the `METADATA.toml`
   file to the first version of the package that shipped `py.typed`.

## Maintainer guidelines

The process for preparing and submitting changes also applies to
maintainers.  This ensures high quality contributions and keeps
everybody on the same page.  Avoid direct pushes to the repository.

When reviewing pull requests, follow these guidelines:

* Typing is hard. Try to be helpful and explain issues with the PR,
  especially to new contributors.
* When reviewing auto-generated stubs, just scan for red flags and obvious
  errors. Leave possible manual improvements for separate PRs.
* When reviewing large, hand-crafted PRs, you only need to look for red flags
  and general issues, and do a few spot checks.
* Review smaller, hand-crafted PRs thoroughly.

When merging pull requests, follow these guidelines:

* Always wait for tests to pass before merging PRs.
* Use "[Squash and merge](https://github.com/blog/2141-squash-your-commits)" to merge PRs.
* Make sure the commit message is meaningful. For example, remove irrelevant
  intermediate commit messages.
* The commit message for third-party stubs is used to generate the changelog.
  It should be valid Markdown, be comprehensive, read like a changelog entry,
  and assume that the reader has no access to the diff.
* Delete branches for merged PRs (by maintainers pushing to the main repo).
