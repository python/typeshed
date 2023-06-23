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
    def __init__(self, container_image: List[str]) -> None: ...

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
        model_id: Optional[str] = None,
        model_name: Optional[str] = None,
        model_description: Optional[str] = None,
        model_version: Optional[int | float] = None,
        problem_type: Optional[str] = None,
        algorithm_type: Optional[str] = None,
        model_creator: Optional[str] = None,
        model_owner: Optional[str] = None,
        model_artifact: Optional[List[str]] = None,
        inference_environment: Optional[Environment] = None,
    ) -> None: ...
    @classmethod
    def from_model_name(cls, model_name: str, sagemaker_session: Session = None, **kwargs): ...

class IntendedUses(_DefaultToRequestDict, _DefaultFromDict):
    risk_rating: Incomplete
    purpose_of_model: Incomplete
    intended_uses: Incomplete
    factors_affecting_model_efficiency: Incomplete
    explanations_for_risk_rating: Incomplete
    def __init__(
        self,
        purpose_of_model: Optional[str] = None,
        intended_uses: Optional[str] = None,
        factors_affecting_model_efficiency: Optional[str] = None,
        risk_rating: Optional[RiskRatingEnum | str] = ...,
        explanations_for_risk_rating: Optional[str] = None,
    ) -> None: ...

class BusinessDetails(_DefaultToRequestDict, _DefaultFromDict):
    business_problem: Incomplete
    business_stakeholders: Incomplete
    line_of_business: Incomplete
    def __init__(
        self,
        business_problem: Optional[str] = None,
        business_stakeholders: Optional[str] = None,
        line_of_business: Optional[str] = None,
    ) -> None: ...

class Function(_DefaultToRequestDict, _DefaultFromDict):
    function: Incomplete
    facet: Incomplete
    condition: Incomplete
    def __init__(
        self,
        function: Optional[ObjectiveFunctionEnum | str] = None,
        facet: Optional[FacetEnum | str] = None,
        condition: Optional[str] = None,
    ) -> None: ...

class ObjectiveFunction(_DefaultToRequestDict, _DefaultFromDict):
    function: Incomplete
    notes: Incomplete
    def __init__(self, function: Function, notes: Optional[str] = None) -> None: ...

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
        value: int | float | str | bool | List,
        notes: Optional[str] = None,
        x_axis_name: Optional[str | list] = None,
        y_axis_name: Optional[str | list] = None,
    ) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, val: int | float | str | bool | List): ...

class TrainingMetric(_DefaultToRequestDict, _DefaultFromDict):
    name: Incomplete
    value: Incomplete
    notes: Incomplete
    def __init__(self, name: str, value: int | float, notes: Optional[str] = None) -> None: ...

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
        training_arn: Optional[str] = None,
        training_datasets: Optional[List[str]] = None,
        training_environment: Optional[Environment] = None,
        training_metrics: Optional[List[TrainingMetric]] = None,
        user_provided_training_metrics: Optional[List[TrainingMetric]] = None,
        hyper_parameters: Optional[List[HyperParameter]] = None,
        user_provided_hyper_parameters: Optional[List[HyperParameter]] = None,
    ) -> None: ...

class TrainingDetails(_DefaultToRequestDict, _DefaultFromDict):
    objective_function: Incomplete
    training_job_details: Incomplete
    training_observations: Incomplete
    def __init__(
        self,
        objective_function: Optional[ObjectiveFunction] = None,
        training_observations: Optional[str] = None,
        training_job_details: Optional[TrainingJobDetails] = None,
    ) -> None: ...
    @classmethod
    def from_model_overview(cls, model_overview: ModelOverview, sagemaker_session: Session = None, **kwargs): ...
    @classmethod
    def from_training_job_name(cls, training_job_name: str, sagemaker_session: Session = None, **kwargs): ...
    def add_metric(self, metric: TrainingMetric): ...
    def add_parameter(self, parameter: HyperParameter): ...

class MetricGroup(_DefaultToRequestDict, _DefaultFromDict):
    metric_data: Incomplete
    name: Incomplete
    def __init__(self, name: str, metric_data: Optional[List[Metric]] = None) -> None: ...
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
        evaluation_observation: Optional[str] = None,
        evaluation_job_arn: Optional[str] = None,
        datasets: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
        metric_groups: Optional[List[MetricGroup]] = None,
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
        ethical_considerations: Optional[str] = None,
        caveats_and_recommendations: Optional[str] = None,
        custom_details: Optional[dict] = None,
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
        status: Optional[ModelCardStatusEnum | str] = ...,
        arn: Optional[str] = None,
        version: Optional[int] = None,
        created_time: Optional[datetime] = None,
        created_by: Optional[dict] = None,
        last_modified_time: Optional[datetime] = None,
        last_modified_by: Optional[dict] = None,
        model_overview: Optional[ModelOverview] = None,
        intended_uses: Optional[IntendedUses] = None,
        business_details: Optional[BusinessDetails] = None,
        training_details: Optional[TrainingDetails] = None,
        evaluation_details: Optional[List[EvaluationJob]] = None,
        additional_information: Optional[AdditionalInformation] = None,
        sagemaker_session: Optional[Session] = None,
    ) -> None: ...
    def create(self): ...
    @classmethod
    def load(cls, name: str, version: Optional[int] = None, sagemaker_session: Session = None): ...
    def update(self, **kwargs): ...
    def delete(self): ...
    def export_pdf(
        self, s3_output_path: str, export_job_name: Optional[str] = None, model_card_version: Optional[int] = None
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
        s3_export_artifacts: Optional[str] = None,
        export_job_arn: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        status: Optional[str] = None,
        failure_reason: Optional[str] = None,
    ) -> None: ...
    def create(self): ...
    @classmethod
    def load(cls, export_job_arn: str, sagemaker_session: Session = None): ...
    @staticmethod
    def list_export_jobs(model_card_name: str, sagemaker_session: Optional[Session] = None, **kwargs): ...
