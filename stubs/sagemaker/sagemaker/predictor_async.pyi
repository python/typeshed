from _typeshed import Incomplete

class AsyncPredictor:
    predictor: Incomplete
    endpoint_name: Incomplete
    sagemaker_session: Incomplete
    s3_client: Incomplete
    serializer: Incomplete
    deserializer: Incomplete
    name: Incomplete
    def __init__(self, predictor, name: Incomplete | None = None) -> None: ...
    def predict(
        self,
        data: Incomplete | None = None,
        input_path: Incomplete | None = None,
        initial_args: Incomplete | None = None,
        inference_id: Incomplete | None = None,
        waiter_config=...,
    ): ...
    def predict_async(
        self,
        data: Incomplete | None = None,
        input_path: Incomplete | None = None,
        initial_args: Incomplete | None = None,
        inference_id: Incomplete | None = None,
    ): ...
    def update_endpoint(
        self,
        initial_instance_count: Incomplete | None = None,
        instance_type: Incomplete | None = None,
        accelerator_type: Incomplete | None = None,
        model_name: Incomplete | None = None,
        tags: Incomplete | None = None,
        kms_key: Incomplete | None = None,
        data_capture_config_dict: Incomplete | None = None,
        wait: bool = True,
    ) -> None: ...
    def delete_endpoint(self, delete_endpoint_config: bool = True) -> None: ...
    def delete_model(self) -> None: ...
    def enable_data_capture(self) -> None: ...
    def disable_data_capture(self) -> None: ...
    def update_data_capture_config(self, data_capture_config) -> None: ...
    def list_monitors(self): ...
    def endpoint_context(self): ...
