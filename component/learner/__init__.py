import abc

class ILearner(abc.ABC):

	def __init__(self, model=None):
		self.set_model(model)
		self.set_memory()

	def set_model(self, model):
		self._model = model

	def train(self):
		assert not self.is_empty_memory(), "Memory is empty."

		self._model.train(self.get_all_memory())
		self._memory.clear()

	def save(self, model_path):
		self._model.save(model_path)

	def load(self, model_path):
		self._model.load(model_path)


	@abc.abstractmethod
	def set_memory(self) -> void:
		pass

	@abc.abstractmethod
	def append_memory(self, data) -> void:
		pass

	@abc.abstractmethod
	def is_empty_memory(self) -> bool:
		pass

	@abc.abstractmethod
	def get_all_memory(self):
		pass
