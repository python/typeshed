======================
PEP NNNN: Type hinting
======================

This is a work-in-progress repository for the draft of the Type Hinting
PEP for Python 3.5.

Authors
-------

* Guido van Rossum

* Jukka Lehtosalo

* Łukasz Langa


Work in progress notes
----------------------

* An explanation of the theory is here: https://quip.com/r69HA9GhGa7J

* Putting new things in ``collections.abc`` seems fine as long as those
  new elements are actual abstract base classes that are collections.
  I (Łukasz) lessened this latter requirement since there's non-collection
  precedent in ``abc``, namely ``Callable``, and ``Hashable``.
  However, attempts at implementing reasonable runtime behavior
  suggests that it may be better to leave ``collections.abc`` alone.
  **Proposed resolution:** Leave ``collections.abc`` alone.

* ``Var('T')`` is put in ``collections.abc`` as a helper with generics
  and covariance/contravariance in ABCs.  May be renamed to ``TypeVar``.
  The co-/contravariance behavior requires more thinking.
  **Proposed resolution:** Use ``TypeVar``, with mypy's semantics mapped:
  ``typevar('T', values=(str, bytes)`` becomes ``TypeVar('T', str, bytes)``.

* ``AnyStr`` (and consequently ``IO``) smells like basestring in
  disguise, what is the use case for Python 3?  Answer: There are
  lots of things in the stdlib that are essentially overloaded as
  str-in-str-out and bytes-in-bytes-out; ``AnyStr`` has exactly the
  right behavior for this (unlike ``Union[str, bytes]``).
  **Proposed resolution:** Keep ``AnyStr``, ``IO`` and its subclasses,
  in typing.py.

* ``Undefined`` smells like JavaScript, I (Łukasz) left it out for now.
  However, mypy needs it.  See https://github.com/ambv/typehinting/issues/20
  **Help???**

* The addition of ``Match`` and ``Pattern`` seems arbitrary and should
  rather be fixed in ``re`` directly, with the types just imported in
  ``typing``. If so, are there any other potentially useful types we'd
  like?  See https://github.com/ambv/typehinting/issues/23
  **Proposed resolution:** Keep these two in typing.py for convenience.

* I (Łukasz) left out ``overload`` because I don't understand its purpose. If we
  need generic dispatch, we should add it to ``functools``.
  Perhaps ``overload`` should only be allowed in stub modules?
  See https://github.com/ambv/typehinting/issues/14
  **Proposed resolution:** support the syntax but only in stub files.

* I (Łukasz) left out specifying protocols as they are an ABC implementation
  detail from the perspective of this PEP. However, they should be
  defined in a separate PEP because making ``__subclasshook__`` less
  dynamic when possible (which is often) would make ABCs much better
  behaved in static analysis contexts.
  See https://github.com/ambv/typehinting/issues/11
  **Help???**

* Having the last thing in mind, ``IO``, ``BinaryIO`` and ``TextIO``
  would simply be new abstract base classes, usable with or without type
  hinting.
  **Proposed resolution:** ``IO`` is generic over ``AnyStr``, the other two
  are concrete (subclassing ``IO[bytes]`` and ``IO[str]`` respectively).

* The current implementation of ``*IO`` is quite un-ducktyped (specifies
  both reading and writing as one protocol)
  **Help???**

* I (Łukasz) left out ``cast`` because it can be more consistently expressed as::

    bad_typed_list = [1, 2, 3]        # type: list
    ...
    well_typed_list = bad_typed_list  # type: List[int]

  See https://github.com/ambv/typehinting/issues/15
  **Proposed resolution:** Add ``cast(type, value)`` back in.

* I (Łukasz) removed ``mypy`` from the listed "existing approaches" since we
  basically describe what mypy is.  **Proposed resolution:** Fine.

* I (Łukasz) thought if introducing optional contravariance/invariance to ``Var``
  has merit but I'm undecided; definitely complicates the type checker.
  See https://github.com/ambv/typehinting/issues/2
  **Help???**


Changes to MyPy coming from this proposal
-----------------------------------------

* ``typevar`` becomes ``Var('T')`` and its semantics support specifying
  base type constraints. If we decide to add optional invariance or
  contravariance, this will be the place, too.
  Or perhaps ``TypeVar('T')``.  See
  https://github.com/JukkaL/mypy/issues/539 and
  https://github.com/ambv/typehinting/issues/1 and
  https://github.com/ambv/typehinting/issues/2 and maybe others.
  **Proposed resolution:** ``TypeVar`` (see above).

* ``Union`` behaves differently, it holds the defined types in order
  to be able to actually respond to issubclass.
  **Proposed resolution:** This doesn't affect mypy; I do want this for
  typing.py (also for generic types).

* ``typing.Function`` becomes ``typing.Callable``, which is equivalent
  to ``collections.abc.Callable``.  (Has now been implemented in mypy.)


Open issues
-----------

* How to make the union type land in __annotations__ for the ``x: str
  = None`` case?

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?

* Should we recommend the use of ABCs over builtin types when possible?

* Should we provide type shortcuts so that MutableMapping is not 3.5x
  longer to type than dict?

* Is multiple dispatch using type hints in scope for this PEP?
  **Proposed resolution:** let's wait, allow @overload only in stubs.

* Should we mention platform- or version-specific typing? Guido mentioned
  Windows vs. POSIX during the Skype meeting.
  **Proposed resolution:** Let typing.py export a few specific constants;
  PY3, PY2, PY3_x (for x in 2, 3, 4, 5).

* It would be useful to have a ``Subclass[]`` factory that would be
  equivalent to "any class that has the all the following classes in its
  MRO".  Maybe we'd want to rename union to ``Any[]`` and this new
  proposed type to ``All[]``?  See https://github.com/ambv/typehinting/issues/18
  **Proposed resolution:** Let's just have ``Union[T1, T2, ...]`` and ``Any``.

* Callable signature definition should be explained and support all
  valid function signatures.
  **Proposed resolution:** ``Callable[[T1, T2, ...], Tr]``.

* What about all other collections available in the ``collections``
  module?
  **Proposed resolution:** Make Generic types retain their argument type(s).
