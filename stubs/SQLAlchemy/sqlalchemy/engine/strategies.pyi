from .mock import MockConnection as _MockConnection

class MockEngineStrategy:
    MockConnection: type[_MockConnection]
