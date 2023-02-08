import argparse

from agent import AgentType
from env import EnvType
from model import ModelType
from system import SystemType


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agent",
        type=AgentType,
        default=AgentType.NORMAL,
        choices=list(AgentType),
    )
    parser.add_argument(
        "--model",
        type=ModelType,
        default=ModelType.DENSE,
        choices=list(ModelType),
    )
    parser.add_argument(
        "--system",
        type=SystemType,
        default=SystemType.DQN,
        choices=list(SystemType),
    )
    parser.add_argument(
        "--env",
        type=EnvType,
        default=EnvType.CARTPOLE,
        choices=list(EnvType),
    )

    return parser.parse_args()
