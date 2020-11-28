import sys

from paramiko.kex_group1 import KexGroup1 as KexGroup1

if sys.version_info < (3, 0):
    from hashlib import _hash as _Hash
else:
    from hashlib import _Hash

class KexGroup14(KexGroup1):
    P: int
    G: int
    name: str
    hash_algo: _Hash
