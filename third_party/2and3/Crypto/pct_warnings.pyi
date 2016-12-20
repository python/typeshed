# Stubs for Crypto.pct_warnings (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

class CryptoWarning(Warning): ...
class CryptoDeprecationWarning(DeprecationWarning, CryptoWarning): ...
class CryptoRuntimeWarning(RuntimeWarning, CryptoWarning): ...
class RandomPool_DeprecationWarning(CryptoDeprecationWarning): ...
class ClockRewindWarning(CryptoRuntimeWarning): ...
class GetRandomNumber_DeprecationWarning(CryptoDeprecationWarning): ...
class PowmInsecureWarning(CryptoRuntimeWarning): ...
