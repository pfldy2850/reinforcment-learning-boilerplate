from .env import IEnvironment
from .env_cartpole import EnvironmentCartPole
from enum import Enum, unique

@unique
class EEnvType(Enum):
	CARTPOLE = 1

# Factory
def create_environment(env_type:EEnvType) -> IEnvironment:
	if env_type == EEnvType.CARTPOLE:
		return EnvironmentCartPole()
