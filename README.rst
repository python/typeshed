======================
PEP NNNN: Type hinting
======================

This is a work-in-progress repository for the draft of the Type Hinting
PEP for Python 3.5.  An explanation of the theory behind type hinting
can be found in https://www.python.org/dev/peps/pep-0483/.

Authors
-------

* Guido van Rossum

* Jukka Lehtosalo

* Łukasz Langa


Things consciously left out for now
-----------------------------------

* Multiple dispatch

* Protocols or a different structural typing solution (Zope
  interfaces?).

* Keyword argument support in ``Callable``.


Changes to MyPy coming from this proposal
-----------------------------------------

* ``typevar`` becomes ``TypeVar('T')`` and its semantics support
  specifying base type constraints. If we decide to add optional
  invariance or contravariance, this will be the place, too. See
  https://github.com/JukkaL/mypy/issues/539 and
  https://github.com/ambv/typehinting/issues/1 and
  https://github.com/ambv/typehinting/issues/2 and maybe others.

* ``Union`` behaves differently, it holds the defined types in order
  to be able to actually respond to issubclass.
  **Proposed resolution:** This doesn't affect mypy; I do want this for
  typing.py (also for generic types).

* ``typing.Function`` becomes ``typing.Callable``, which is equivalent
  to ``collections.abc.Callable``.  (Has now been implemented in mypy.)


Open issues
-----------

* Introducing ``cast`` and stubs

* How to make the union type land in __annotations__ for the ``x: str
  = None`` case?

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?

* Should we recommend the use of ABCs over builtin types when possible?

* Is multiple dispatch using type hints in scope for this PEP?
  **Proposed resolution:** let's wait, allow @overload only in stubs.


Work in progress notes
----------------------

* I (Łukasz) left out ``overload`` because I don't understand its
  purpose. If we need generic dispatch, we should add it to
  ``functools``.  Perhaps ``overload`` should only be allowed in stub
  modules?  See https://github.com/ambv/typehinting/issues/14 **Proposed
  resolution:** support the syntax but only in stub files.

* Having the last thing in mind, ``IO``, ``BinaryIO`` and ``TextIO``
  would simply be new abstract base classes, usable with or without type
  hinting.  **Proposed resolution:** ``IO`` is generic over ``AnyStr``,
  the other two are concrete (subclassing ``IO[bytes]`` and ``IO[str]``
  respectively).

* The current implementation of ``*IO`` is quite un-ducktyped (specifies
  both reading and writing as one protocol)
  **Help???**

* I (Łukasz) thought if introducing optional contravariance/invariance
  to ``TypeVar`` has merit but I'm undecided; definitely complicates the
  type checker.  See https://github.com/ambv/typehinting/issues/2
  **Help???**
