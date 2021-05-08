from .actor import IActor
from .env import IEnvironment
from .learner import ILearner
from .model import IModel

# Constants
ENV_TYPES = [
	'CartPole'
]


def Environment(env:str) -> IEnvironment:
	assert env in ENV_TYPES, f"There isn't environment which type is '{type}'."

	if env == 'CartPole':
		return EnvironmentCartPole()


def Actor(action_size, model_path:str, env:str='opengym') -> IActor:
	environment = Environment(env)
	model = ModelLite(model_path)

	return IActor(action_size, environment, model)


# def Learner(model, )
