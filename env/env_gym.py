import gym

from .env import Env


class GymEnv(Env):
    def __new__(cls, id: str, *args, **kwargs):
        return gym.make(id, *args, **kwargs)
