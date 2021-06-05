from .memory import IMemory
from collections import deque

class MemoryDeque(IMemory):

	def __init__(self):
		self._instance = deque()

	def append(self, data) -> None:
		self._instance.append(data)

	def concat(self, data) -> None:
		self._instance += data

	def clear(self) -> None:
		self._instance.clear()

	def pop(self):
		return self._instance.popleft()

	def get_all(self):
		return self._instance

	def length(self) -> int:
		return len(self._instance)
