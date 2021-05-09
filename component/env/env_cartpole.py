from .env import IEnvironment
import gym
import numpy as np

class EnvironmentCartPole(IEnvironment):
	def __init__(self, index:str=''):
		self._setup(index)

	def _setup(self, index):
		self._env = gym.make('CartPole-v0')
		self._last_obs 	= self._env.reset()
		self._last_rwd 	= 0
		self._done		= False

	def get_state(self):
		return self._last_obs

	def get_reward(self) -> float:
		return self._last_rwd

	def run_action(self, action) -> bool:
		obs, rwd, done, info = self._env.step(action)
		self._last_obs = obs
		self._last_rwd = rwd
		self._done = done

		return done

	def is_finish(self) -> bool:
		return self._done

	def get_action_mask(self):
		return np.array([1, 1])

	def get_action_size(self) -> int:
		return 2

	def reset(self) -> None:
		self._last_obs = self._env.reset()
		self._last_rwd 	= 0
		self._done		= False

	def render(self):
		self._env.render()
