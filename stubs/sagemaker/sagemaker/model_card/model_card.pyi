from _typeshed import Incomplete
from datetime import datetime
from typing import List, Optional

from boto3.session import Session as boto3_Session
from sagemaker.model_card.evaluation_metric_parsers import EvaluationMetricTypeEnum
from sagemaker.model_card.helpers import _DefaultFromDict, _DefaultToRequestDict
from sagemaker.model_card.schema_constraints import (
    FacetEnum,
    MetricTypeEnum,
    ModelCardStatusEnum,
    ObjectiveFunctionEnum,
    RiskRatingEnum,
)
from sagemaker.session import Session

logger: Incomplete

class Environment(_DefaultToRequestDict, _DefaultFromDict):
    container_image: Incomplete
    def __init__(self, container_image: list[str]) -> None: ...

class ModelOverview(_DefaultToRequestDict, _DefaultFromDict):
    model_artifact: Incomplete
    inference_environment: Incomplete
    model_id: Incomplete
    model_name: Incomplete
    model_description: Incomplete
    model_version: Incomplete
    problem_type: Incomplete
    algorithm_type: Incomplete
    model_creator: Incomplete
    model_owner: Incomplete
    def __init__(
        self,
        model_id: str | None = None,
        model_name: str | None = None,
        model_description: str | None = None,
        model_version: int | float | None = None,
        problem_type: str | None = None,
        algorithm_type: str | None = None,
        model_creator: str | None = None,
        model_owner: str | None = None,
        model_artifact: list[str] | None = None,
        inference_environment: Environment | None = None,
    ) -> None: ...
    @classmethod
    def from_model_name(cls, model_name: str, sagemaker_session: Session | None = None, **kwargs): ...

class IntendedUses(_DefaultToRequestDict, _DefaultFromDict):
    risk_rating: Incomplete
    purpose_of_model: Incomplete
    intended_uses: Incomplete
    factors_affecting_model_efficiency: Incomplete
    explanations_for_risk_rating: Incomplete
    def __init__(
        self,
        purpose_of_model: str | None = None,
        intended_uses: str | None = None,
        factors_affecting_model_efficiency: str | None = None,
        risk_rating: RiskRatingEnum | str | None = ...,
        explanations_for_risk_rating: str | None = None,
    ) -> None: ...

class BusinessDetails(_DefaultToRequestDict, _DefaultFromDict):
    business_problem: Incomplete
    business_stakeholders: Incomplete
    line_of_business: Incomplete
    def __init__(
        self,
        business_problem: str | None = None,
        business_stakeholders: str | None = None,
        line_of_business: str | None = None,
    ) -> None: ...

class Function(_DefaultToRequestDict, _DefaultFromDict):
    function: Incomplete
    facet: Incomplete
    condition: Incomplete
    def __init__(
        self,
        function: ObjectiveFunctionEnum | str | None = None,
        facet: FacetEnum | str | None = None,
        condition: str | None = None,
    ) -> None: ...

class ObjectiveFunction(_DefaultToRequestDict, _DefaultFromDict):
    function: Incomplete
    notes: Incomplete
    def __init__(self, function: Function, notes: str | None = None) -> None: ...

class Metric(_DefaultToRequestDict, _DefaultFromDict):
    type: Incomplete
    name: Incomplete
    notes: Incomplete
    x_axis_name: Incomplete
    y_axis_name: Incomplete
    def __init__(
        self,
        name: str,
        type: MetricTypeEnum | str,
        value: int | float | str | bool | list,
        notes: str | None = None,
        x_axis_name: str | list | None = None,
        y_axis_name: str | list | None = None,
    ) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, val: int | float | str | bool | list): ...

class TrainingMetric(_DefaultToRequestDict, _DefaultFromDict):
    name: Incomplete
    value: Incomplete
    notes: Incomplete
    def __init__(self, name: str, value: int | float, notes: str | None = None) -> None: ...

class HyperParameter(_DefaultToRequestDict, _DefaultFromDict):
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: str) -> None: ...

class TrainingJobDetails(_DefaultToRequestDict, _DefaultFromDict):
    training_datasets: Incomplete
    training_metrics: Incomplete
    user_provided_training_metrics: Incomplete
    hyper_parameters: Incomplete
    user_provided_hyper_parameters: Incomplete
    training_environment: Incomplete
    training_arn: Incomplete
    def __init__(
        self,
        training_arn: str | None = None,
        training_datasets: list[str] | None = None,
        training_environment: Environment | None = None,
        training_metrics: list[TrainingMetric] | None = None,
        user_provided_training_metrics: list[TrainingMetric] | None = None,
        hyper_parameters: list[HyperParameter] | None = None,
        user_provided_hyper_parameters: list[HyperParameter] | None = None,
    ) -> None: ...

class TrainingDetails(_DefaultToRequestDict, _DefaultFromDict):
    objective_function: Incomplete
    training_job_details: Incomplete
    training_observations: Incomplete
    def __init__(
        self,
        objective_function: ObjectiveFunction | None = None,
        training_observations: str | None = None,
        training_job_details: TrainingJobDetails | None = None,
    ) -> None: ...
    @classmethod
    def from_model_overview(cls, model_overview: ModelOverview, sagemaker_session: Session | None = None, **kwargs): ...
    @classmethod
    def from_training_job_name(cls, training_job_name: str, sagemaker_session: Session | None = None, **kwargs): ...
    def add_metric(self, metric: TrainingMetric): ...
    def add_parameter(self, parameter: HyperParameter): ...

class MetricGroup(_DefaultToRequestDict, _DefaultFromDict):
    metric_data: Incomplete
    name: Incomplete
    def __init__(self, name: str, metric_data: list[Metric] | None = None) -> None: ...
    def add_metric(self, metric: Metric): ...

class EvaluationJob(_DefaultToRequestDict, _DefaultFromDict):
    datasets: Incomplete
    metric_groups: Incomplete
    name: Incomplete
    evaluation_observation: Incomplete
    evaluation_job_arn: Incomplete
    metadata: Incomplete
    def __init__(
        self,
        name: str,
        evaluation_observation: str | None = None,
        evaluation_job_arn: str | None = None,
        datasets: list[str] | None = None,
        metadata: dict | None = None,
        metric_groups: list[MetricGroup] | None = None,
    ) -> None: ...
    def get_metric_group(self, group_name): ...
    def add_metric_group(self, group_name: str): ...
    def add_metric_group_from_json(self, json_path: str, metric_type: EvaluationMetricTypeEnum = ...): ...
    def add_metric_group_from_s3(self, session: boto3_Session, s3_url: str, metric_type: EvaluationMetricTypeEnum = ...): ...

class AdditionalInformation(_DefaultToRequestDict, _DefaultFromDict):
    ethical_considerations: Incomplete
    caveats_and_recommendations: Incomplete
    custom_details: Incomplete
    def __init__(
        self,
        ethical_considerations: str | None = None,
        caveats_and_recommendations: str | None = None,
        custom_details: dict | None = None,
    ) -> None: ...

class ModelCard:
    DECODER_ATTRIBUTE_MAP: Incomplete
    CREATE_MODEL_CARD_REQUIRED: Incomplete
    INITIAL_VERSION: int
    status: Incomplete
    model_overview: Incomplete
    intended_uses: Incomplete
    business_details: Incomplete
    training_details: Incomplete
    evaluation_details: Incomplete
    additional_information: Incomplete
    name: Incomplete
    arn: Incomplete
    version: Incomplete
    created_time: Incomplete
    created_by: Incomplete
    last_modified_time: Incomplete
    last_modified_by: Incomplete
    sagemaker_session: Incomplete
    def __init__(
        self,
        name: str,
        status: ModelCardStatusEnum | str | None = ...,
        arn: str | None = None,
        version: int | None = None,
        created_time: datetime | None = None,
        created_by: dict | None = None,
        last_modified_time: datetime | None = None,
        last_modified_by: dict | None = None,
        model_overview: ModelOverview | None = None,
        intended_uses: IntendedUses | None = None,
        business_details: BusinessDetails | None = None,
        training_details: TrainingDetails | None = None,
        evaluation_details: list[EvaluationJob] | None = None,
        additional_information: AdditionalInformation | None = None,
        sagemaker_session: Session | None = None,
    ) -> None: ...
    def create(self): ...
    @classmethod
    def load(cls, name: str, version: int | None = None, sagemaker_session: Session | None = None): ...
    def update(self, **kwargs): ...
    def delete(self): ...
    def export_pdf(
        self, s3_output_path: str, export_job_name: str | None = None, model_card_version: int | None = None
    ): ...
    def list_export_jobs(self, **kwargs): ...
    def get_version_history(self, **kwargs): ...

class ModelCardExportJob:
    EXPORT_JOB_POLLING_FREQUENCY: int
    export_job_name: Incomplete
    model_card_name: Incomplete
    model_card_version: Incomplete
    s3_output_path: Incomplete
    s3_export_artifacts: Incomplete
    sagemaker_session: Incomplete
    export_job_arn: Incomplete
    status: Incomplete
    failure_reason: Incomplete
    def __init__(
        self,
        export_job_name: str,
        model_card_name: str,
        model_card_version: int,
        s3_output_path: str,
        s3_export_artifacts: str | None = None,
        export_job_arn: str | None = None,
        sagemaker_session: Session | None = None,
        status: str | None = None,
        failure_reason: str | None = None,
    ) -> None: ...
    def create(self): ...
    @classmethod
    def load(cls, export_job_arn: str, sagemaker_session: Session | None = None): ...
    @staticmethod
    def list_export_jobs(model_card_name: str, sagemaker_session: Session | None = None, **kwargs): ...
