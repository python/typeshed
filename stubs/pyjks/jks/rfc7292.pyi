from _typeshed import Incomplete

from pyasn1.type import univ

PBE_WITH_SHA1_AND_TRIPLE_DES_CBC_OID: Incomplete
PURPOSE_KEY_MATERIAL: int
PURPOSE_IV_MATERIAL: int
PURPOSE_MAC_MATERIAL: int

class Pkcs12PBEParams(univ.Sequence):
    componentType: Incomplete

def derive_key(hashfn, purpose_byte, password_str, salt, iteration_count, desired_key_size): ...
def decrypt_PBEWithSHAAnd3KeyTripleDESCBC(data, password_str, salt, iteration_count): ...
def decrypt_PBEWithSHAAndTwofishCBC(encrypted_data, password, salt, iteration_count): ...
def encrypt_PBEWithSHAAndTwofishCBC(plaintext_data, password, salt, iteration_count): ...
