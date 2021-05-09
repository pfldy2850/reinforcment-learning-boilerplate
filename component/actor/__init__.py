from .actor import IActor
from ..env import Environment
from ..memory import Memory
from ..model import Model


def Actor(
		model_path:str,
		model_type:str='tflite',
		env_type:str='cartpole',
		mem_type:str='none') -> IActor:

	environment = Environment(env_type)
	memory 		= Memory(mem_type)
	model 		= Model(model_path, model_type)

	return IActor(environment, model, memory)
