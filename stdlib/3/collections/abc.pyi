# Stubs for collections.abc (introduced from Python 3.3)
#
# https://docs.python.org/3.3/whatsnew/3.3.html#collections
import sys

if sys.version_info >= (3, 3):
    from . import (
        Container as Container,
        MutableMapping as MutableMapping,
        Sequence as Sequence,
        MutableSequence as MutableSequence,
        Set as Set,
        MutableSet as MutableSet,
    )
