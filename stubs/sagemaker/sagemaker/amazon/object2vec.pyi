from typing import Optional

from sagemaker.amazon.amazon_estimator import AmazonAlgorithmEstimatorBase
from sagemaker.amazon.hyperparameter import Hyperparameter as hp
from sagemaker.model import Model
from sagemaker.session import Session
from sagemaker.workflow.entities import PipelineVariable

class Object2Vec(AmazonAlgorithmEstimatorBase):
    repo_name: str
    repo_version: str
    MINI_BATCH_SIZE: int
    enc_dim: hp
    mini_batch_size: hp
    epochs: hp
    early_stopping_patience: hp
    early_stopping_tolerance: hp
    dropout: hp
    weight_decay: hp
    bucket_width: hp
    num_classes: hp
    mlp_layers: hp
    mlp_dim: hp
    mlp_activation: hp
    output_layer: hp
    optimizer: hp
    learning_rate: hp
    negative_sampling_rate: hp
    comparator_list: hp
    tied_token_embedding_weight: hp
    token_embedding_storage_type: hp
    enc0_network: hp
    enc1_network: hp
    enc0_cnn_filter_width: hp
    enc1_cnn_filter_width: hp
    enc0_max_seq_len: hp
    enc1_max_seq_len: hp
    enc0_token_embedding_dim: hp
    enc1_token_embedding_dim: hp
    enc0_vocab_size: hp
    enc1_vocab_size: hp
    enc0_layers: hp
    enc1_layers: hp
    enc0_freeze_pretrained_embedding: hp
    enc1_freeze_pretrained_embedding: hp
    def __init__(
        self,
        role: str | PipelineVariable | None = None,
        instance_count: int | PipelineVariable | None = None,
        instance_type: str | PipelineVariable | None = None,
        epochs: int | None = None,
        enc0_max_seq_len: int | None = None,
        enc0_vocab_size: int | None = None,
        enc_dim: int | None = None,
        mini_batch_size: int | None = None,
        early_stopping_patience: int | None = None,
        early_stopping_tolerance: float | None = None,
        dropout: float | None = None,
        weight_decay: float | None = None,
        bucket_width: int | None = None,
        num_classes: int | None = None,
        mlp_layers: int | None = None,
        mlp_dim: int | None = None,
        mlp_activation: str | None = None,
        output_layer: str | None = None,
        optimizer: str | None = None,
        learning_rate: float | None = None,
        negative_sampling_rate: int | None = None,
        comparator_list: str | None = None,
        tied_token_embedding_weight: bool | None = None,
        token_embedding_storage_type: str | None = None,
        enc0_network: str | None = None,
        enc1_network: str | None = None,
        enc0_cnn_filter_width: int | None = None,
        enc1_cnn_filter_width: int | None = None,
        enc1_max_seq_len: int | None = None,
        enc0_token_embedding_dim: int | None = None,
        enc1_token_embedding_dim: int | None = None,
        enc1_vocab_size: int | None = None,
        enc0_layers: int | None = None,
        enc1_layers: int | None = None,
        enc0_freeze_pretrained_embedding: bool | None = None,
        enc1_freeze_pretrained_embedding: bool | None = None,
        **kwargs,
    ) -> None: ...
    def create_model(self, vpc_config_override="VPC_CONFIG_DEFAULT", **kwargs): ...

class Object2VecModel(Model):
    def __init__(
        self,
        model_data: str | PipelineVariable,
        role: str | None = None,
        sagemaker_session: Session | None = None,
        **kwargs,
    ) -> None: ...
