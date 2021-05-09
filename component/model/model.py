import abc

class IModel(abc.ABC):

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
