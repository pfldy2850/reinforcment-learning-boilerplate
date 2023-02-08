from enum import Enum, unique

from .env import Env


@unique
class EnvType(Enum):
    CARTPOLE = 1


# Factory
def create_env(env_type: EnvType, *args, **kwargs) -> Env:
    from .env_cartpole import CartPoleEnv

    if env_type == EnvType.CARTPOLE:
        return CartPoleEnv(*args, **kwargs)
