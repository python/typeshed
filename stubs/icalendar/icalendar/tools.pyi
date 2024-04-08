from _typeshed import Incomplete

class UIDGenerator:
    chars: Incomplete
    @staticmethod
    def rnd_string(length: int = 16): ...
    @staticmethod
    def uid(host_name: str = "example.com", unique: str = ""): ...
