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
  **Assumption:** This doesn't affect mypy; I do want this for
  typing.py (also for generic types).

* ``None`` should only be acceptable if an annotation explicitly uses
  ``Optional[...]`` or if there is an explicit default ``= None``.

* I (Guido) would like type aliases in mypy to be more powerful.  A
  type alias should be allowed to be e.g. a ``Union[...]``.

* Implement `Tuple[t1, ...]` for variable-length homogeneous tuples.
  See https://github.com/JukkaL/mypy/issues/184


Open issues
-----------

* Introducing ``cast`` and stub files.  **TODO:** Update the PEP.

* How to make the union type land in __annotations__ for the ``x: str
  = None`` case?  **Resolution:** Add a function to typing.py that
  retrieves a function's type annotations.  This should also expand
  forward references and honor ``@no_type_check`` decorators.

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?  **TODO:** Lukasz to
  update PEP 482.


Work in progress notes
----------------------

* Perhaps ``IO``, ``BinaryIO`` and ``TextIO``
  should simply be new abstract base classes, usable with or without type
  hinting.  **Proposed resolution:** ``IO`` is generic over ``AnyStr``,
  the other two are concrete (subclassing ``IO[bytes]`` and ``IO[str]``
  respectively).

* The current implementation of ``*IO`` is quite un-ducktyped (specifies
  both reading and writing as one protocol)
  **What does this mean???**

* Co/contravariance and type variables.

* Pick a definitive syntax to put in `# type: ...` comments to disable
  type checking.  **Proposal:** `# type: OFF` and `# type: ON`.

* Decide on the fate of `AbstractGeneric`.
  See https://github.com/ambv/typehinting/issues/41

Editing tasks
-------------

* Note that type checkers ought to provide config options to
  selectively skip specific modules/packages.
  See https://github.com/ambv/typehinting/issues/53

* Explain `@no_type_check` and also how to define a new decorator that
  implies the same.  See https://github.com/ambv/typehinting/issues/51

* Describe how to declare a generic class.
  See https://github.com/ambv/typehinting/issues/41

* Make a list of things we're explicitly punting (see above).

* Explain namedtuple.  (Does this go in PEP 483 perhaps?)

* Describe the ``typing.re`` and ``typing.io`` subpackages, and how to
  add others.

* Clarify type aliasing (what is allowed on the RHS, if only by example).

* Clarify the limits of expressions the type checker should be able to
  evaluate (as opposed to typecheck).  (Maybe only through examples.)

* See also the list of github issues.  (https://github.com/ambv/typehinting/issues)
