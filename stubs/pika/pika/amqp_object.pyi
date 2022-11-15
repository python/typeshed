from _typeshed import Incomplete

class AMQPObject:
    NAME: str
    INDEX: Incomplete
    def __eq__(self, other): ...

class Class(AMQPObject):
    NAME: str

class Method(AMQPObject):
    NAME: str
    synchronous: bool
    def get_properties(self): ...
    def get_body(self): ...

class Properties(AMQPObject):
    NAME: str
