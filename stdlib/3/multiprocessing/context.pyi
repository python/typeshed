from multiprocessing import Event

class BaseContext(object):
    def Event(self) -> Event: ...