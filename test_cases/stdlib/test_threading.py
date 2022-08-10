import threading
import _threading_local

l = threading.local()
l.foo = 42
del l.foo
l.baz = ["spam", "eggs"]
del l.baz

l2 = _threading_local.local()
l2.asdfasdf = 56
del l2.asdfasdf
