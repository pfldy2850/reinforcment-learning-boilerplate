import abc
import random
import numpy as np

"""
Actor
  - Environment	: Simulation environment in which the simulation takes place
  - Model		: Algorithms or models which determine the simulation action
  - Memory		: Memory for saving the simulation information
"""

class IActor(abc.ABC):

	def __init__(self, environment, model, memory):
		self._memory 		= memory
		self._environment 	= environment
		self._model 		= model

	def run_step(self, explore_rate=0):
		if self.is_finish(): return

		state 		= self.get_state()
		action 		= self.get_action(state, explore_rate=explore_rate)
		reward 		= self.get_reward()
		done 		= self.run_action(action)
		next_state 	= self.get_state()
		finish		= self.is_finish()

		self.append_memory([state, action, reward, next_state, done, finish])

	def get_state(self):
		return self._environment.get_state()

	def get_action(self, state, explore_rate=0):
		action_mask = self._environment.get_action_mask()

		if random.random() < explore_rate: 		# explore
			action_prob = np.random.rand(self._environment.get_action_size())
		else: 									# exploit
			action_prob = self._model.get_action_prob(state)

		assert action_mask.shape == action_prob.shape, f"Shapes are different between action_mask({action_mask.shape}) and action_probs({action_prob.shape})."

		return np.argmax(action_prob * action_mask)

	def get_reward(self):
		return self._environment.get_reward()

	def append_memory(self, data):
		self._memory.append(data)

	def run_action(self, action):
		return self._environment.run_action(action)

	def is_finish(self):
		return self._environment.is_finish()
