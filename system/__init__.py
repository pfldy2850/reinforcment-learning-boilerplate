from enum import Enum, unique

from .system import System


@unique
class SystemType(Enum):
    DQN = "dqn"


def create_system(system_type: SystemType, *args, **kwargs) -> System:
    from .system_dqn import DqnSystem

    if system_type == SystemType.DQN:
        return DqnSystem(*args, **kwargs)

    pass
