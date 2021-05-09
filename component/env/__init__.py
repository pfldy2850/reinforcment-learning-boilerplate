from .env import IEnvironment
from .env_cartpole import EnvironmentCartPole

# Constants
ENV_TYPES = [
	'cartpole'
]

# Factory
def Environment(env_type:str) -> IEnvironment:
	assert env_type in ENV_TYPES, f"There isn't a environment which type is '{env_type}'."

	if env_type == 'cartpole':
		return EnvironmentCartPole()
