from _typeshed import Incomplete

from .util import *

SUN_JKS_ALGO_ID: Incomplete
SUN_JCE_ALGO_ID: Incomplete

def jks_pkey_encrypt(key, password_str): ...
def jks_pkey_decrypt(data, password_str): ...
def jce_pbe_decrypt(data, password, salt, iteration_count): ...
