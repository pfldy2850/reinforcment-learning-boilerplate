from enum import Enum, unique
from .actor import IActor
from .actor_normal import ActorNormal
from env import EEnvType

@unique
class EActorType(Enum):
    NORMAL      = 1
    NO_AGENT    = 2
    NO_ENV      = 3


def create_actor(
    actor_type:EActorType=EActorType.NORMAL,
    env_type:EEnvType=EEnvType.CARTPOLE,
    env_num:int=1):

    if actor_type == EActorType.NORMAL:
        return ActorNormal(
            env_type=env_type,
            env_num=env_num
        )

    return IActor()
