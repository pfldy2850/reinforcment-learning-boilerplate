from enum import Enum, unique

from .env import Env


@unique
class EnvType(Enum):
    DEFAULT = "default"
    GYM = "GYM"


# Factory
def create_env(env_type: EnvType, *args, **kwargs) -> Env:
    from .env_gym import GymEnv

    if env_type == EnvType.GYM:
        return GymEnv(*args, **kwargs)

    return Env(*args, **kwargs)
