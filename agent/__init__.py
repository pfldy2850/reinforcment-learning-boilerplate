from enum import Enum, unique

from .agent import Agent


@unique
class AgentType(Enum):
    NORMAL = "normal"


def create_agent(agent_type: AgentType, *args, **kwargs) -> Agent:
    return Agent(*args, **kwargs)
