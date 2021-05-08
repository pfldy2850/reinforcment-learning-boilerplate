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
	def load(self, model_path):
		pass

	@abc.abstractmethod
	def save(Self, model_path):
		pass
