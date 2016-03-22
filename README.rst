===================
PEP 484: Type Hints
===================

This GitHub repo is used for drafting PEP 484: Type Hints, slated for
inclusion in Python 3.5.

Authors
-------

* Guido van Rossum

* Jukka Lehtosalo

* Łukasz Langa

BDFL-Delegate
-------------

The BDFL-Delegate is Mark Shannon.  This means he gets to be the final
reviewer of the PEP and ultimately gets to accept or reject it -- see
PEP 1 (https://www.python.org/dev/peps/pep-0001/).

Important dates
---------------

The target dates for inclusion of typing.py in Python 3.5 are derived
from the Python 3.5 release schedule as documented in PEP 478
(https://www.python.org/dev/peps/pep-0478/), and subject to change if
that schedule slips:

* May 24, 2015: Python 3.5.0 beta 1 -- PEP 484 accepted, typing.py
  feature complete and checked into CPython repo

* August 9, 2015: Python 3.5.0 release candidate 1 -- Last chance for
  fixes to typing.py barring emergencies:

* September 13, 2015: Python 3.5.0 final release

Important URLs
--------------

The python.org rendering of the PEP lives at
https://www.python.org/dev/peps/pep-0484/, but the version in this
GitHub repo is typically newer -- the python.org version corresponds
to the most recent draft posted to python-ideas or python-dev.

Two related informational PEPs exist, but are updated by their
respective authors directly in the Hg peps repo:

* An explanation of the theory behind type hints can be found in
  https://www.python.org/dev/peps/pep-0483/.

* A literature review is at https://www.python.org/dev/peps/pep-0482/.

The python.org site automatically updates (with a slight delay,
typically in the order of 5-60 minutes) whenever the Hg peps repo is
updated.

Workflows
---------

Here's some documentation on the workflow we're using for the various
aspects of the PEP.

Workflow for editing PEP 484
----------------------------

* The PEP 484 draft is edited in the GitHub python/typing repo.

* The typing.py module and its unittests are edited in the prototyping
  subdirectory of the same repo.

* Use the GitHub issue tracker for this repo to collect concerns and
  TO DO items for pep-0484.txt as well as for prototyping/typing.py.

* Accumulate changes in the GitHub repo, closing issues as they are
  either decided and described in the PEP, or implemented in
  typing.py, or both, as befits the issue.  (Some issues will be
  closed as "won't fix" after a decision is reached not to take
  action.)

* Make frequent small commits with clear descriptions.  Preferably use
  a separate commit for each functional change, so the edit history is
  clear, merge conflicts are unlikely, and it's easy to roll back a
  change when further discussion reverts an earlier tentative decision
  that was already written up and/or implemented.

* Push to GitHub frequently.

* Pull from GitHub frequently, rebasing conflicts carefully (or
  merging, if a conflicting change was already pushed).

* At reasonable checkpoints: copy pep-0484.txt to the Hg peps repo on
  hg.python.org and post that version as the new draft to python-ideas
  or (in later stages) to python-dev, making sure to update the
  Post-History header in both repos.  This is typically done by Guido.

Tracker labels
--------------

* bug: Needs to be fixed in typing.py.

* to do: Editing task for the PEP itself.

* enhancement: Proposed new feature.

* postponed: Idea up for discussion.

* out of scope: Somebody else's problem.


Workflow for editing PEP 482 and PEP 483
----------------------------------------

* These PEPs only have informational status.

* They are updated directly in the Hg peps repo by their authors
  (Łukasz for PEP 482, Guido for PEP 483).

Workflow for mypy changes
-------------------------

* Use the GitHub issue tracker for the mypy repo (JukkaL/mypy).  Jukka
  accepts GitHub Pull Requests at his discretion.

* At Jukka's discretion, he will from time to time copy typing.py and
  test_typing.py from the python/typing GitHub repo to the mypy repo.

* At Jukka's discretion, he also copies these to the typing repo
  (JukkaL/typing).

Workflow for CPython changes
----------------------------

* TBD: Workflow for copying typing.py and test_typing.py into the
  CPython repo.

Things consciously left out for now
-----------------------------------

* Multiple dispatch (but ``@overload`` will be allowed in stubs).

* A general implementation of structural typing (but some specific
  structural types are included, e.g. ``ImplementsAbs``).

* Keyword argument and varargs support in ``Callable``.

* Probably other things.

Changes to MyPy
---------------

(Omitting things implemented in mypy 0.2; See
http://mypy-lang.blogspot.com/2015/04/mypy-02-released.html.)

* ``None`` should only be acceptable if an annotation explicitly uses
  ``Optional[...]`` or if there is an explicit default ``= None``.
  See https://github.com/JukkaL/mypy/issues/359

* Implement `Tuple[t1, ...]` for variable-length homogeneous tuples.
  See https://github.com/JukkaL/mypy/issues/184

* Drop ``Undefined``.

* Generalized named constants and constant expressions.

* The full list of mypy issues marked as PEP 484 compatibility issues
  is here: https://github.com/JukkaL/mypy/labels/pep484

TO DO Lists
-----------

(Not sure that the TODO lists need to be in here; they don't seem complete.)

PEP 482 TO DO
-------------

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?  **TODO:** Łukasz to
  update PEP 482.

PEP 483 TO DO
-------------

* Explain generics better.

* Drop definition of ``Intersection``?

PEP 484 TO DO
-------------

* Co/contravariance and type variables.  (See VARIANCE.rst)

* Note that type checkers ought to provide config options to
  selectively skip specific modules/packages.
  See https://github.com/python/typing/issues/53

* Describe how to declare a generic class.
  See https://github.com/python/typing/issues/41

* Add a comprehensive list of things we're explicitly punting (see above).

* See also the list of github issues:
  https://github.com/python/typing/issues

README.rst TO DO
----------------

* Drop list of changes to mypy.

* Remove all the TO DO lists, in favor of using the GitHub issue
  tracker for everything.
