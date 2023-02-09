from enum import Enum, unique
from functools import reduce

from gym import Space

from .model import Model


@unique
class ModelType(Enum):
    DENSE = "dense"


# Factory
def create_model(model_type: ModelType, *args, **kwargs) -> Model:
    observation_space: Space = kwargs.get("observation_space")
    action_space: Space = kwargs.get("action_space")

    if model_type == ModelType.DENSE:
        from .model_dense import DenseModel

        return DenseModel(
            observation_space_size=reduce(lambda x, y: x * y, observation_space.shape),
            action_space_size=reduce(lambda x, y: x * y, action_space.shape)
            if action_space.shape
            else action_space.n,
        )

    return Model(*args, **kwargs)
