class DefaultStreaming:
    def __init__(self, streaming_threshold: int = 30) -> None: ...
    def is_eligible(self, segment): ...
    def stream(self, entity, callback) -> None: ...
    @property
    def streaming_threshold(self): ...
    @streaming_threshold.setter
    def streaming_threshold(self, value) -> None: ...
