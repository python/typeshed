# Stubs for _operator (Python 3.5)

# fmt: off
import sys
# In reality the import is the other way around, but this way we can keep the operator stub in 2and3
from operator import abs as abs
from operator import add as add
from operator import and_ as and_
from operator import attrgetter as attrgetter
from operator import concat as concat
from operator import contains as contains
from operator import countOf as countOf
from operator import delitem as delitem
from operator import eq as eq
from operator import floordiv as floordiv
from operator import ge as ge
from operator import getitem as getitem
from operator import gt as gt
from operator import iadd as iadd
from operator import iand as iand
from operator import iconcat as iconcat
from operator import ifloordiv as ifloordiv
from operator import ilshift as ilshift
from operator import imod as imod
from operator import imul as imul
from operator import index as index
from operator import indexOf as indexOf
from operator import inv as inv
from operator import invert as invert
from operator import ior as ior
from operator import ipow as ipow
from operator import irshift as irshift
from operator import is_ as is_
from operator import is_not as is_not
from operator import isub as isub
from operator import itemgetter as itemgetter
from operator import itruediv as itruediv
from operator import ixor as ixor
from operator import le as le
from operator import length_hint as length_hint
from operator import lshift as lshift
from operator import lt as lt
from operator import methodcaller as methodcaller
from operator import mod as mod
from operator import mul as mul
from operator import ne as ne
from operator import neg as neg
from operator import not_ as not_
from operator import or_ as or_
from operator import pos as pos
from operator import pow as pow
from operator import rshift as rshift
from operator import setitem as setitem
from operator import sub as sub
from operator import truediv as truediv
from operator import truth as truth
from operator import xor as xor
from typing import AnyStr

# fmt: on

if sys.version_info >= (3, 5):
    from operator import matmul as matmul, imatmul as imatmul

def _compare_digest(a: AnyStr, b: AnyStr) -> bool: ...
