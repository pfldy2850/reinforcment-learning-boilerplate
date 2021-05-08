import abc

class IEnvironment(abc.ABC):

	def __init__(self, index:str=''):
		self._setup(index)

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
