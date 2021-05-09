import abc
from ..actor import Actor
from ..learner import Learner
from ..model import IModel


# run actor
def run_actor(idx, model_path, model_type, env_type, mem_type, explore_rate:float=0, visible:bool=False):
	actor = Actor(model_path, model_type=model_type, env_type=env_type, mem_type=mem_type)
	actor.reset()
	while not actor.is_finish():
		actor.run_step(explore_rate=explore_rate)
		if visible: actor.render()

	# print(actor.get_step_cnt())
	return actor.get_memory()


class ISystem(abc.ABC):

	def __init__(self,
			model:IModel,
			model_path:str,
			model_type:str,
			actor_num:int,
			env_type:str,
			mem_type:str) -> None:

		self._model_path 	= model_path
		self._model_type 	= model_type
		self._actor_num 	= actor_num
		self._env_type 		= env_type
		self._mem_type 		= mem_type
		self.learner 		= Learner(model, mem_type=mem_type)

	# sync trained weights for actors
	def sync(self) -> None:
		self.learner.save(tflite=True)

	def demo(self) -> None:
		actor = Actor(
			self._model_path,
			model_type=self._model_type,
			env_type=self._env_type,
			mem_type=self._mem_type)

		while not actor.is_finish():
			actor.run_step()
			actor.render()


	# learning process
	@abc.abstractmethod
	def learn(self, epi_num:int, explore_rate:float=0) -> None:
		pass
