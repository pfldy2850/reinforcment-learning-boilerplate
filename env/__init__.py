from enum import Enum, unique

from .env import Env


@unique
class EnvType(Enum):
    DEFAULT = "default"
    CARTPOLE = "cartpole"


# Factory
def create_env(env_type: EnvType, *args, **kwargs) -> Env:
    from .env_gym import GymEnv

    if env_type == EnvType.CARTPOLE:
        return GymEnv("CartPole-v0")

    return Env(*args, **kwargs)
