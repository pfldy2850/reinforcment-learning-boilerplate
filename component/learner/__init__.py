import abc

class ILearner(abc.ABC):

	def __init__(self, model, memory):
		self._model 	= model
		self._memory 	= memory

	def train(self):
		assert not self._memory.is_empty(), "Memory is empty."

		self._model.train(self._memory.get_all())
		self._memory.clear()

	def save(self):
		self._model.save()

	def load(self):
		self._model.load()
