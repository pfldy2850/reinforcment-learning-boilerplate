from .system import ISystem
from .system_mono import SystemMono
from actor import EActorType

def create_system(
    actor_type:EActorType=EActorType.NORMAL,
    actor_num:int=1,
    env_num:int=1,
    ) -> ISystem:

    assert actor_num > 0,       "actor_num must be greater than 1"
    assert env_num > 0,         "env_num must be greater than 1"

    if actor_num == 1:
        return SystemMono(
            actor_type=actor_type,
            actor_num=actor_num,
            env_num=env_num
        )




    pass
