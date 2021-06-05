import abc

class IMemory(abc.ABC):

	@abc.abstractmethod
	def append(self, data) -> None:
		pass

	@abc.abstractmethod
	def concat(self, data) -> None:
		pass

	@abc.abstractmethod
	def clear(self) -> None:
		pass

	@abc.abstractmethod
	def pop(self):
		pass

	@abc.abstractmethod
	def get_all(self):
		pass

	@abc.abstractmethod
	def length(self) -> int:
		pass


	def is_empty(self) -> bool:
		return self.length() == 0
