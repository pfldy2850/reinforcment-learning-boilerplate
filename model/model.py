import abc
import os

class IModel(abc.ABC):

	def __init__(self, model_path:str, overwrite:bool=False):
		self._model_path 	= model_path

		if overwrite or os.path.exists(model_path): self.save(tflite=True)
		self.load()


	@abc.abstractmethod
	def get_action_prob(self, state):
		pass

	@abc.abstractmethod
	def get_action(self, state):
		pass

	@abc.abstractmethod
	def train(self, data):
		pass

	@abc.abstractmethod
	def load(self):
		pass

	@abc.abstractmethod
	def save(self, tflite:bool=False):
		pass
