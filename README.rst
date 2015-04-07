===================
PEP 484: Type Hints
===================

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

* Multiple dispatch (but ``@overload`` will be allowed in stubs).

* Protocols or a different structural typing solution.

* Keyword argument support in ``Callable``.

* Probably other things.  Should we try to list them all here, or get
  rid of this list?


Changes to MyPy coming from this proposal
-----------------------------------------

(Omitting things implemented in mypy 0.2; See
http://mypy-lang.blogspot.com/2015/04/mypy-02-released.html.)

* ``None`` should only be acceptable if an annotation explicitly uses
  ``Optional[...]`` or if there is an explicit default ``= None``.
  See https://github.com/JukkaL/mypy/issues/359

* Implement `Tuple[t1, ...]` for variable-length homogeneous tuples.
  See https://github.com/JukkaL/mypy/issues/184

* The full list of mypy issues marked as PEP 484 compatibility issues
  is here: https://github.com/JukkaL/mypy/labels/pep484

PEP 482 TO DO
-------------

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?  **TODO:** Lukasz to
  update PEP 482.

PEP 483 TO DO
-------------

* Explain generics better.

* Drop definition of ``Intersection``?


PEP 484 TO DO
-------------

* Explain generics better.

* Co/contravariance and type variables.

* Note that type checkers ought to provide config options to
  selectively skip specific modules/packages.
  See https://github.com/ambv/typehinting/issues/53

* Describe how to declare a generic class.
  See https://github.com/ambv/typehinting/issues/41

* Make a list of things we're explicitly punting (see above).

* Clarify the limits of constant expressions (expressions the type
  checker should be able to evaluate, as opposed to typecheck).
  (Maybe only through examples.)

* Decide the fate of Undefined; see
  https://github.com/ambv/typehinting/issues/20

* See also the list of github issues:
  https://github.com/ambv/typehinting/issues
