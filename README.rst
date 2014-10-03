=====================
PEP 500: Type hinting
=====================

This is a work-in-progress repository for the draft of the Type Hinting
PEP for Python 3.5.

Authors
-------

* Guido van Rossum

* Jukka Lehtosalo

* Łukasz Langa


Work in progress notes
----------------------

* Putting new things in ``collections.abc`` seems fine as long those new
  elements are actual abstract base classes that are collections.
  I lessened this latter requirement since there's non-collection
  precedent in ``abc``, namely ``ByteString``, ``Callable``, and
  ``Hashable``.

* ``Var('T')`` is put in ``collections.abc`` as a helper with generics
  and covariance/contravariance in ABCs

* ``AnyStr`` (and consequently ``IO``) smells like basestring in
  disguise

* ``Undefined`` smells like JavaScript

* The addition of ``Match`` and ``Pattern`` seems arbitrary and should
  rather be fixed in ``re`` directly, with the types just imported in
  ``typing``. If so, are there any other potentially useful types we'd
  like?

* I left out ``overload`` because I don't understand its purpose. If we
  need generic dispatch, we should add it to ``functools``

* I left out specifying protocols as they are an ABC implementation
  detail from the perspective of this PEP. However, they should be
  defined in a separate PEP because making ``__subclasshook__`` less
  dynamic when possible (which is often) would make ABCs much better
  behaved in static analysis contexts

* Having the last thing in mind, ``IO``, ``BinaryIO`` and ``TextIO``
  would simply be new abstract base classes, usable with or without type
  hinting

* the current implementation of ``*IO`` is quite un-ducktyped (specifies
  both reading and writing as one protocol)

* I left out ``cast`` because it can be more consistently expressed as::

  bad_typed_list = [1, 2, 3]        # type: list
  ...
  well_typed_list = bad_typed_list  # type: List[int]

* I removed ``mypy`` from the listed "existing approaches" since we
  basically describe what MyPy is

* I thought if introducing optional contravariance/invariance to ``Var``
  has merit but I'm undecided; definitely complicates the type checker


Changes to MyPy coming from this proposal
-----------------------------------------

* ``typevar`` becomes ``Var('T')`` and its semantics support specifying
  base type constraints. If we decide to add optional invariance or
  contravariance, this will be the place, too.

* ``collections.abc.Union`` behaves differently, it holds the defined
  types to be able to actually respond to issubclass. Consequently,
  ``typing.AnyStr`` becomes an ``Union`` instead of ``typevar('AnyStr',
  values=(str, bytes))`` (which is consciously impossible to express in
  the ``Var`` notation, unless you're using a Union as ``base=``)

* ``typing.Function`` becomes ``typing.Callable``, which is equivalent
  to ``collections.abc.Callable``


Open issues
-----------

* How to make the union type land in __annotations__ for the ``x:str
  = None`` case?

* State of the art: should we list decorator-based approaches
  (PyContracts?) and docstring-based approaches?

* should we recommend the use of ABCs over builtin types when possible?

* should we provide type shortcuts so that MutableMapping is not 3.5x
  longer to type than dict?

* is multiple dispatch using type hints in scope for this PEP?

* should we mention platform- or Python-specific typing? Guido mentioned
  Windows vs. POSIX during the Skype meeting.

* it would be useful to have a ``Subclass[]`` factory that would be
  equivalent to "any class that has the all the following classes in its
  MRO".  Maybe we'd want to rename union to ``Any[]`` and this new
  proposed type to ``All[]``?
