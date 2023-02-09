import abc

from torch import nn

from env.env import Env


class Agent(abc.ABC):
    def __init__(self, env: Env, *args, **kwargs) -> None:
        self.env = env
        self.reset()

    def reset(self):
        self.state, info = self.env.reset()
