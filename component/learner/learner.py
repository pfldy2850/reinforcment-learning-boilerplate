import abc

class ILearner(abc.ABC):

	def __init__(self, model, memory):
		self._model 	= model
		self._memory 	= memory

	def train(self):
		assert not self._memory.is_empty(), "Memory is empty."

		self._model.train(self._memory.get_all())
		self._memory.clear()

	def save(self, tflite:bool=False):
		self._model.save(tflite=tflite)

	def load(self):
		self._model.load()

	def get_memory(self):
		return self._memory

	def concat_memory(self, data):
		self._memory.concat(data)
