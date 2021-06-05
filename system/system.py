import abc
import types
from actor import EActorType

class ISystem(abc.ABC):
    def __init__(self,
        actor_type:EActorType=EActorType.NORMAL,
        actor_num:int=1,
        env_num:int=1):

        self._actor_type = actor_type
        self._actor_num = actor_num
        self._env_num = env_num
        self._actors = []
        pass

    def __str__(self):
        string_buffer = []
        string_buffer.append('-'*100)
        string_buffer.append(f"[{self.__class__.__name__} at {hex(id(self))}]")
        string_buffer.append(f"actor_type: {self._actor_type}")
        string_buffer.append(f"actor_num: {self._actor_num}")
        string_buffer.append(f"env_num: {self._env_num}")

        string_actors = "\n".join(list(map(lambda x: "\t" + "\n\t".join(str(x).split('\n')), self._actors)))
        string_buffer.append("actors:")
        string_buffer.append(string_actors)
        string_buffer.append('-'*100)

        return "\n".join(string_buffer)

    def _get_explore_rate(self, explore_rate):
        is_explore = lambda x: 0
        if explore_rate is None:                            pass
        elif type(explore_rate) in (int, float):            is_explore = lambda x: explore_rate
        elif isinstance(explore_rate, types.FunctionType):  is_explore = explore_rate
        return is_explore

    @abc.abstractmethod
    def train(self,
        episode:int=100,
        explore_rate=None) -> None:
        pass
