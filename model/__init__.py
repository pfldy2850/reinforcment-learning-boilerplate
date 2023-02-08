from enum import Enum, unique

from .model import Model


@unique
class ModelType(Enum):
    DENSE = "dense"


# Factory
def create_model(model_type: ModelType, *args, **kwargs) -> Model:
    if model_type == ModelType.DENSE:
        from .model_dense import DenseModel

        return DenseModel(*args, **kwargs)

    return Model(*args, **kwargs)
