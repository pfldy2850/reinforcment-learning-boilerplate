import abc

class IEnvironment(abc.ABC):

	def __init__(self, index:str=''):
		self._setup(index)

	def __str__(self):
		string_buffer = []
		string_buffer.append(f"[{self.__class__.__name__} at {hex(id(self))}]")
		return "\n".join(string_buffer)


	@abc.abstractmethod
	def _setup(self, index):
		pass

	@abc.abstractmethod
	def get_state(self):
		pass

	@abc.abstractmethod
	def get_reward(self) -> float:
		pass

	@abc.abstractmethod
	def run_action(self, action) -> bool:
		pass

	@abc.abstractmethod
	def is_finish(self) -> bool:
		pass

	@abc.abstractmethod
	def get_action_mask(self):
		pass

	@abc.abstractmethod
	def get_action_size(self) -> int:
		pass

	@abc.abstractmethod
	def reset(self) -> None:
		pass

	@abc.abstractmethod
	def render(self) -> None:
		pass
