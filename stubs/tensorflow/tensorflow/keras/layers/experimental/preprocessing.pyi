import abc

from tensorflow._aliases import TensorLike
from tensorflow.keras.layers import Layer

class PreprocessingLayer(Layer[TensorLike, TensorLike], metaclass=abc.ABCMeta): ...
