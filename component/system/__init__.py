from .system import ISystem
from .system_mtp import SystemMTP
from ..model import IModel

# Constants
SYS_TYPE = [
	'mtp'
]

# Factory
def System(
		model:IModel,
		model_path:str,
		model_type:str='tflite',
		actor_num:int=1,
		env_type:str='cartpole',
		mem_type:str='deque',
		sys_type:str='mtp',
		parallel:int=1
	) -> ISystem:

	assert sys_type in SYS_TYPE, f"There isn't a system which type is '{sys_type}'."

	system = None

	if sys_type == 'mtp':
		system = SystemMTP(model, model_path, model_type, actor_num, env_type, mem_type, parallel=parallel)

	return system
