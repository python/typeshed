from datadog.api.resources import (
    ActionAPIResource,
    ActionAPISyntheticsResource,
    CreateableAPIResource,
    GetableAPIResource,
    UpdatableAPISyntheticsResource,
    UpdatableAPISyntheticsSubResource,
)

class Synthetics(
    ActionAPIResource,
    ActionAPISyntheticsResource,
    CreateableAPIResource,
    GetableAPIResource,
    UpdatableAPISyntheticsResource,
    UpdatableAPISyntheticsSubResource,
):
    @classmethod
    def get_test(cls, id, **params): ...
    @classmethod
    def get_all_tests(cls, **params): ...
    @classmethod
    def get_devices(cls, **params): ...
    @classmethod
    def get_locations(cls, **params): ...
    @classmethod
    def get_results(cls, id, **params): ...
    @classmethod
    def get_result(cls, id, result_id, **params): ...
    @classmethod
    def create_test(cls, **params): ...
    @classmethod
    def edit_test(cls, id, **params): ...
    @classmethod
    def start_or_pause_test(cls, id, **body): ...
    @classmethod
    def delete_test(cls, **body): ...
