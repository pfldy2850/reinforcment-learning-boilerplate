import gym
import numpy as np

from .env import Env


class CartPoleEnv(Env):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._env: gym.Env = gym.make("CartPole-v0")

    def step(self, action):
        return self._env.step(action)

    def reset(self, **kwargs):
        return self._env.reset(**kwargs)

    def render(self, **kwargs):
        return self._env.render(**kwargs)
