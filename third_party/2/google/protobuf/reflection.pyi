class GeneratedProtocolMessageType(type):
    def __new__(cls, name, bases, dictionary): ...
    def __init__(cls, name, bases, dictionary) -> None: ...

def ParseMessage(descriptor, byte_str): ...
def MakeClass(descriptor): ...
