Variance
========

Author's note
-------------

In an earlier draft I had swapped the meanings of 'in' and 'out'
(having misremembered what I had read on Wikipedia).  I believe I am
not unique in making this mistake, so we've switched to
covariant=True and contravariant=True.

Discussion
----------

The big question is: If Manager is a subclass of Employee, should
List[Manager] be considered a subclass of List[Employee}?

If we answer "yes", we may encounter a runtime type error in a program
that passes the type check.  I'll show you how.

Let's first consider an innocent example that does not have a problem::

    # Example 1

    def add_employee(emps: List[Employee], new_emp: Employee) -> None:
        emps.append(new_emp)

    def add_manager(mgrs: List[Manager], new_mgr: Manager) -> None:
        add_employee(mgrs, new_mgr)

Suppose we define the type checker so that this passes.  Now let's
make a change to add_employee()::

    # Example 2

    def add_employee(emps: List[Employee], new_emp: Employee) -> None:
        copy_of_new_emp = Employee()
        copy_of_new_emp.name = new_emp.name
        # Etc., copy all known Employee fields
        emps.append(copy_of_new_emp)

    # add_manager() is unchanged

Using the above definition of the type checker (where List[Manager] is
a subclass of List[Employee]), example 2 would also type-check, but it
has a bug that example 1 doesn't have: When add_manager() is called,
it now appends a new Employee to the argument list (mgrs), which
violates its type (List[Manager]) at runtime.

Let's leave aside for now why one would make this change, or how to
fix the bug.  In real software development the two functions may be in
different packages, maintained by different teams, and much more
complicated, and that's exactly where you'd like a type checker to
catch problems -- but the type checker has let us down.

There are languages whose type system has this problem; but they
typically address it in the language by making the append() call in
add_employee() fail at runtime.  IIUC Java does this for Arrays -- an
Array object "knows" the item type from its declaration and rejects
new elements that aren't a subclass of this type.

BTW, the reason why languages introduce such unsound type checks is
that intuitively (i.e. if you haven't considered or encountered cases
like example 2 above) making List[Manager] a subclass of
List[Employee] feels right to many developers.  A sound type system
will make example 1 fail the type check, which is hard to explain to
developers, especially since there is no bug when you run it.

("Sound" is a technical term used for type systems, meaning "won't
pass programs that fail at runtime".  There's also a dual property
whose name escapes me, meaning "won't fail programs that pass at
runtime".  Both properties are equally elusive. :-)

Now, PEP 484 doesn't in general make hard promises of soundness --
there are lots of ways that Python's dynamic typing can do things that
will break a program even though it passes the type check, so why
should we promise soundness for this particular situation (roughly,
defining subclassing of mutable container types based on the item
classes)?

The reason is that example 2 is a pretty gross violation of an
expectation: you have an object whose declared type is List[Manager]
but, without doing anything sneaky, you've managed to add an Employee
object that isn't a Manager to it, while flying under the radar of the
type checked.

The proposed solution gives the developer who writes a container class
a way to tell the type checker whether the container should be
considered mutable or immutable.  For immutable container
types, problems like example 2 cannot happen (proof left as an
exercise for the reader :-), so the type checker can consider
e.g. Tuple[Manager] a subclass of Tuple[Employee], while disallowing
List[Manager] as a subclass of List[Employee].

The proposal adds a way to declare that a type variable follows the
rules for covariance or contravariance, while by default type
variables are invariant::

    X = TypeVar('X')  # Invariant
    Y = TypeVar('Y', covariant=True)  # Covariant
    Z = TypeVar('Z', contravariant=True)  # Contravariant

    class A(Generic[X]):
        ...

    class B(Generic[Y]):
        ...

    class C(Generic[Z]):
        ...

    issubclass(A[Manager], A[Employee])  # False
    issubclass(B[Manager], B[Employee])  # True
    issubclass(B[Employee], B[Manager])  # True (I think)

Unfortunately this still doesn't let us write example 1.  But the
consolation is that this means example 2 won't happen.  So how can we
rewrite example 1 in a way that is type-safe under the new rule?

The solution is perhaps unexpected: We have to write a mutable data
type that's covariant and implements a run-time type check like Java
Array.  Here's a sketch of such a data type::

    T = TypeVar('T', covariant=True)  # Covariant

    class MyList(MutableSequence[T]):
        def __init__(self):
            self._data = []  # type: List[T]
            self._item_type = self.__class__.__parameters__[0]
        ...
        def append(self, item: T):
            if not isinstance(item, self._item_type):
                raise TypeError("item type %r does not match %r" %
                                (item.__class__, self._item_type))
        ...

Reference
---------

http://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29
