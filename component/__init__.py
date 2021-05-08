from .actor import IActor
from .env import IEnvironment
from .env.env_cartpole import EnvironmentCartPole
from .learner import ILearner
from .model import IModel
from .model.model_tflite import ModelTFLite
from .model.model_ac import ModelAC
from .memory import IMemory
from .memory.memory_deque import MemoryDeque

# Constants
ENV_TYPES = [
	'cartpole'
]

MEM_TYPES = [
	'deque'
]

MODEL_TYPES = [
	'tflite'
]


def Environment(env_type:str) -> IEnvironment:
	assert env_type in ENV_TYPES, f"There isn't a environment which type is '{env_type}'."

	if env_type == 'cartpole':
		return EnvironmentCartPole()


def Memory(mem_type:str) -> IMemory:
	assert mem_type in MEM_TYPES, f"There isn't a memory which type is '{mem_type}'."

	if mem_type == 'deque':
		return MemoryDeque()


def Model(model_path, model_type:str) -> IModel:
	assert model_type in MODEL_TYPES, f"There isn't a model which type is '{model_type}'."

	if model_type == 'tflite':
		return ModelTFLite(model_path)


def Actor(model_path:str, model_type:str='tflite', env_type:str='cartpole', mem_type:str='deque') -> IActor:
	environment = Environment(env_type)
	memory 		= Memory(mem_type)
	model 		= Model(model_path, model_type)

	return IActor(environment, model, memory)


def Learner(model, mem_type:str='deque') -> ILearner:
	memory 		= Memory(mem_type)

	return ILearner(model, memory)


# def Learner(model, )
