from .resource import Collection, Model

class Config(Model):
    id_attribute: str
    @property
    def name(self): ...
    def remove(self): ...

class ConfigCollection(Collection):
    model = Config
    def create(self, **kwargs): ...
    def get(self, config_id): ...
    def list(self, **kwargs): ...
