Generics
--------

The subscript operation on container types is overloaded to support
specifying the item type for the container as part of a type hint.
Example::

  from typing import List

  def space_join(a: List[str]) -> str:
      """Join list items with spaces."""
      return ' '.join(a)

Given this definition, the following code will be flagged as a type
error, because the argument has type ``List[int]`` (list of integers)
rather than ``List[str]`` (list of strings)::

  space_join([1, 2, 3])  # Error

Depending on the definition of the container, multiple type arguments
may be given in this notation::

  from collections import defaultdict
  from typing import Iterable, Dict

  def word_count(words: Iterable[str]) -> Dict[str, int]:
      """Count words in document."""
      res = defaultdict(int)
      for word in words:
          res[word] += 1
      return dict(res)

  print(word_count(['to', 'be', 'or', 'not', 'to', 'be']))
  # {'to': 2, 'be': 2, 'or': 1, 'not': 1}
  

Sometimes we want the type of several arguments and/or the return type
to vary collectively.  We can do this using type variables.  A type
variable must be defined using the ``TypeVar()`` factory, after which
it can be used in mutiple function or method signatures.  This is
called a generic function.  Example::

  from collections import defaultdict
  from typing import Iterable, Mapping, TypeVar

  T = TypeVar('T')

  def thing_count(things: Iterable[T]) -> Dict[T, int]:
      """Count words in document."""
      res = defaultdict(int)
      for thing in things:
          res[thing] += 1
      return dict(res)

  print(thing_count([2, 3, 5, 7, 2, 3])
  # {2: 2, 3: 2, 5: 1, 7: 1}

Note that the argument to ``TypeVar()`` must be a string, and it must
be assigned to a variable with exactly that name.  Type variables
cannot be redefined in the same module.  These constraints are
enforced by the type checker (but not by the runtime implementation of
``TypeVar()``).

We can also define generic classes, as follows::

  from typing import Generic, TypeVar

  T = TypeVar('T')

  class Node(Generic[T]):

      def __init__(self, label: T) -> None:
          self.label = label

      def get_label(self) -> T:
          return self.label

  def mknod(x: int) -> Node[int]:
      return Node(x)

  print(mknod(40).get_label() + 2)
  # 42

This same mechanism is used to define the container classes exported
by ``typing`` (although the implementation is hairier due to the
desire to also emulate collection ABCs).

Type variables have a few more tricks up their sleeves:

* Additional positional arguments must be type expressions that will
  be used to constrain the types that are acceptable substitutions.
  This feature is used for example by the predefined type variable
  ``AnyStr``, which is defined as::

    AnyStr = TypeVar('AnyStr', str, bytes)

  When such a constrained type variable is used in an argument type,
  the actual type must be a subtype of one of the constraints.  When
  used in a return value type, the inferred return type will be
  exactly the corresponding constraint (*not* the inferred argument
  type, which may be a subtype thereof).  For example::

    from typing import AnyStr

    def add_strings(a: AnyStr, b: AnyStr) -> AnyStr:
        return a+b

    add_string('x', 'y')  # 'xy'
    add_string(b'a', b'b')  # b'ab'
    add_string('x', b'z')  # Error

    class MyStr(str):
        pass

    add_string(MyStr('a'), MyStr('b'))  # 'ab', not MyStr('ab')

* Type variables may be declared as covariant or contravariant.  The
  default is invariant.  Covariance is best explained using an
  example::

    from typing import TypeVar

    T = TypeVar('T')
    Tco = TypeVar('Tco', covariant=True)

    class MyTuple(Generic[Tco]):
        ...  # Implements immutable sequence operations

    class MyList(MyTuple[T]):
        ...  # Adds mutable sequence operations

    class Employee:
        ...

    class Manager(Employee):
        ...

    issubclass(MyTuple[Manager], MyTuple[Employee])  # True
    issubclass(MyList[Manager], MyList[Employee])  # False

    def print_employees(emps: MyTuple[Employee]) -> None:
        for emp in emps:
            print(emp)

    def add_employee(emps: MyList[Employee], emp: Employee) -> None:
        emps.append(emp)

    mgrs = MyList[Manager](...)  # Undecided if this is allowed
    print_employees(mgrs)  # OK
    bob = Manager(...)
    add_employee(mgrs, bob)  # Error

  For a good if theoretical explanation of covariance and
  contravariance see the Wikipedia article:
  http://en.wikipedia.org/wiki/Covariance_and_contravariance_%28computer_science%29
