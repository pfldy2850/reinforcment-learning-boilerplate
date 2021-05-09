from .system import ISystem, run_actor
from ..model import IModel
from multiprocessing import Pool
from tqdm import tqdm

class SystemMTP(ISystem):
	def __init__(self,
			model:IModel,
			model_path:str,
			model_type:str,
			actor_num:int,
			env_type:str,
			mem_type:str,
			parallel:int=1) -> None:

		super().__init__(model, model_path, model_type, actor_num, env_type, mem_type)
		self.parallel = parallel


	# learning process
	def learn(self, epi_num:int, explore_rate:float=0, visible:bool=False) -> None:
		for epi_idx in tqdm(range(epi_num)):
			# run actors
			with Pool(processes=min(self.parallel, self._actor_num)) as pool:
				results = pool.starmap(run_actor, [
					(
						x,
						self._model_path,
						self._model_type,
						self._env_type,
						self._mem_type,
						explore_rate,
						visible
					) for x in range(self._actor_num)
				])

				for result in results: self.learner.concat_memory(result.get_all())

		# train learner
		self.learner.train()
		self.sync()
