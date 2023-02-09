from enum import Enum, unique

from .agent import Agent


@unique
class AgentType(Enum):
    VALUE_BASED = "value_based"


def create_agent(agent_type: AgentType, *args, **kwargs) -> Agent:
    from .agent_value_based import ValueBasedAgent

    if agent_type == AgentType.VALUE_BASED:
        return ValueBasedAgent(*args, **kwargs)

    return Agent(*args, **kwargs)
