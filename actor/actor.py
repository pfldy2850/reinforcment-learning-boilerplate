import abc
from env import EEnvType
from agent import IAgent

class IActor(abc.ABC):
    _agent = None
    _envs = None

    def __init__(self,
        env_type:EEnvType=EEnvType.CARTPOLE,
        env_num:int=1):
        self._env_type = env_type
        self._env_num = env_num
        pass

    def __str__(self):
        string_buffer = []
        string_buffer.append(f"[{self.__class__.__name__} at {hex(id(self))}]")
        string_buffer.append(f"env_type: {self._env_type}")
        string_buffer.append(f"env_num: {self._env_num}")
        return "\n".join(string_buffer)

    def _get_string_envs(self):
        string_buffer = []
        if self._envs is None:
            string_buffer.append("envs: None")
        else:
            string_envs = "\n".join(list(map(lambda x: "\t" + "\n\t".join(str(x).split('\n')), self._envs)))
            string_buffer.append("envs:")
            string_buffer.append(string_envs)
        return "\n".join(string_buffer)

    def _get_string_agent(self):
        string_buffer = []
        if self._agent is None:
            string_buffer.append("agent: None")
        else:
            string_buffer.append(f"agent:")
            string_buffer.append("\t" + str(self._agent))
        return "\n".join(string_buffer)

    def get_agent(self) -> IAgent:
        return self._agent


    @abc.abstractmethod
    def run(self, explore_rate:float=0):
        pass
