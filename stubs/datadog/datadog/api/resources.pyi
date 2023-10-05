from _typeshed import Incomplete

class CreateableAPIResource:
    @classmethod
    def create(
        cls,
        attach_host_name: bool = False,
        method: str = "POST",
        id: Incomplete | None = None,
        params: Incomplete | None = None,
        **body,
    ): ...

class SendableAPIResource:
    @classmethod
    def send(cls, attach_host_name: bool = False, id: Incomplete | None = None, compress_payload: bool = False, **body): ...

class UpdatableAPIResource:
    @classmethod
    def update(cls, id, params: Incomplete | None = None, **body): ...

class CustomUpdatableAPIResource:
    @classmethod
    def update(cls, method: Incomplete | None = None, id: Incomplete | None = None, params: Incomplete | None = None, **body): ...

class DeletableAPIResource:
    @classmethod
    def delete(cls, id, **params): ...

class GetableAPIResource:
    @classmethod
    def get(cls, id, **params): ...

class ListableAPIResource:
    @classmethod
    def get_all(cls, **params): ...

class ListableAPISubResource:
    @classmethod
    def get_items(cls, id, **params): ...

class AddableAPISubResource:
    @classmethod
    def add_items(cls, id, params: Incomplete | None = None, **body): ...

class UpdatableAPISubResource:
    @classmethod
    def update_items(cls, id, params: Incomplete | None = None, **body): ...

class DeletableAPISubResource:
    @classmethod
    def delete_items(cls, id, params: Incomplete | None = None, **body): ...

class SearchableAPIResource: ...
class ActionAPIResource: ...

class UpdatableAPISyntheticsSubResource:
    @classmethod
    def update_synthetics_items(cls, id, params: Incomplete | None = None, **body): ...

class UpdatableAPISyntheticsResource:
    @classmethod
    def update_synthetics(cls, id, params: Incomplete | None = None, **body): ...

class ActionAPISyntheticsResource: ...
