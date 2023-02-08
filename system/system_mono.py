from .system import ISystem
from agent import create_agent
from actor import create_actor
from actor import EActorType

class SystemMono(ISystem):
    def __init__(self,
        actor_type:EActorType=EActorType.NORMAL,
        actor_num:int=1,
        env_num:int=1):

        super().__init__(
            actor_type=actor_type,
            actor_num=actor_num,
            env_num=env_num
        )

        assert actor_type == EActorType.NORMAL, "SystemMono must have a normal actor"
        assert actor_num == 1, "SystemMono must have a single actor"

        self._actors = [ create_actor(
            actor_type=actor_type,
            env_num=env_num
        ) for _ in range(self._actor_num) ]

        self._main_agent = self._actors[0].get_agent()


    def train(self,
        episode:int=100,
        explore_rate=None) -> None:

        get_explore_rate = self._get_explore_rate(explore_rate)

        for epi in range(1, episode+1):
            self._actors[0].run(explore_rate=get_explore_rate(epi))

        pass
