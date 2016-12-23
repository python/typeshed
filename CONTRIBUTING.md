# Contributing to typeshed

Welcome!  typeshed is a community project that aims to work for a wide
range of Python users and Python codebases.  If you're trying a type
checker on your Python code, your experience and what you can contribute
are important to the project's success.


## Getting started, building, and testing

If you haven't already, take a look at the project's
[README.md file](README.md)
and try adding type annotations to your file and type-checking it with
a tool like [Mypy](http://www.mypy-lang.org/),
[pytype](https://github.com/google/pytype), or
[PyCharm](https://www.jetbrains.com/pycharm/).


## Discussion

If you've run into behavior in the type checker that suggests the type
stubs for a given library are incorrect or incomplete, or a library you
depend on is missing type annotations, we want to hear from you!

Our main forum for discussion is the project's [GitHub issue
tracker](https://github.com/python/typeshed/issues).  This is the right
place to start a discussion of any of the above or most any other
topic concerning the project.

For less formal discussion, try the Mypy chat room on
[gitter.im](https://gitter.im/python/mypy).  Some Mypy core developers
are almost always present; feel free to find us there and we're happy
to chat.  Substantive technical discussion will be directed to the
issue tracker.

### Code of Conduct

Everyone participating in the typeshed community, and in particular in
our issue tracker, pull requests, and IRC channel, is expected to treat
other people with respect and more generally to follow the guidelines
articulated in the [Python Community Code of
Conduct](https://www.python.org/psf/codeofconduct/).


## Submitting Changes

Even more excellent than a good bug report is a fix for a bug, or the
implementation of a much-needed stub. We'd love to have
your contributions.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the
mechanics, see [Mypy's git and GitHub workflow help page](https://github.com/python/mypy/wiki/Using-Git-And-GitHub),
or [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

Anyone interested in type stubs may review your code.  One of the core
developers will merge your pull request when they think it's ready.
For every pull request, we aim to promptly either merge it or say why
it's not yet ready; if you go a few days without a reply, please feel
free to ping the thread by adding a new comment.

At present the core developers are (alphabetically):
* David Fisher (@ddfisher)
* Łukasz Langa (@ambv)
* Jukka Lehtosalo (@JukkaL)
* Matthias Kramm (@matthiaskramm)
* Greg Price (@gnprice)
* Guido van Rossum (@gvanrossum)


## Preparing Changes

Before you begin: if your change will be a significant amount of work
to write, we highly recommend starting by opening an issue laying out
what you want to do.  That lets a conversation happen early in case
other contributors disagree with what you'd like to do or have ideas
that will help you do it.

If you want to submit type stubs for a new library, you need to
**contact the maintainers of the original library** first to let them
know and **get their permission**.  Do it by opening an issue on their
project's bug tracker.  This gives them the opportunity to
consider adopting type hints directly in their codebase (which you
should prefer to external type stubs).  When the project owners agree
for you to submit stubs here, open a pull request **referencing the
message where you received permission**.

Make sure your changes pass tests by running ``runtests.sh`` (the
[README](README.md) has more information).

### Using stubgen

Mypy includes a tool called [stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py)
that you can use as a starting point for your stubs.  Note that this
generator is currently unable to determine most argument and return
types and omits them or uses ``Any`` in their place.  Fill out the types
that you know.  Leave out modules that you are not using at all.  It's
strictly better to provide partial stubs that have detailed type
information than to submit unmodified ``stubgen`` output for an entire
library.

### Stub file coding style

Stub files are *like* Python files and you should generally expect them
to look the same.  Your tools should be able to successfully treat them
as regular Python files.  However, there are a few important differences
you should know about.

Style conventions for stub files are different from PEP 8. The general
rule is that they should be as concise as possible.  Specifically:
* there is no line length limit;
* prefer long lines over elaborate indentation;
* prefer ``...`` over ``pass``;
* prefer ``...`` on the same line as the class/function signature;
* avoid vertical whitespace between consecutive module-level functions,
  names, or methods and fields within a single class;
* prefer type comments over variable annotations unless your stubs are
  exclusively targeting Python 3.6.

Imports in stubs are considered private (not part of the exported API)
unless:
* they use the form ``from library import name as name`` (sic, using
  explicit ``as`` even if the name stays the same); or
* they use the form ``from library import *`` which means all names
  from that library are exported.

Stub files support forward references natively.  In other words, the
order of class declarations and type aliases does not matter in
a stub file.  You can also use the name of the class within its own
body.  Focus on making your stubs clear to the reader.  Avoid using
string literals in type annotations.

Finally, remember to include a comment on the top of your file about the
version of the Python language your stubs were tested against and
version of the library they were built for.  This makes it easier to
maintain the stubs in the future.

NOTE: there are stubs in this repository that don't conform to the
style described above.  Fixing them is a great starting point for new
contributors.

### What to do when a project's documentation and implementation disagree

Type stubs are meant to be external type annotations for a given
library.  While they are useful documentation in its own merit, they
augment the project's concrete implementation, not the project's
documentation.  Whenever you find them disagreeing, model the type
information after the actual implementation and file an issue on the
project's tracker to fix their documentation.

## Issue-tracker conventions

We aim to reply to all new issues promptly.  We'll assign a milestone
to help us track which issues we intend to get to when, and may apply
labels to carry some other information.  Here's what our milestones
and labels mean.

### Labels

* **needs discussion**: This issue needs agreement on some kind of
  design before it makes sense to implement it, and it either doesn't
  yet have a design or doesn't yet have agreement on one.
* **help wanted**: This issue could use a volunteer willing to implement
  it. Those issues can be great starting points for new contributors!
* **enhancement**, **bug**, **refactoring**: These classify the
  user-facing impact of the change.  Specifically "refactoring" means
  there should be no user-facing effect.
* **duplicate**, **wontfix**: These identify issues that we've closed
  for the respective reasons.
