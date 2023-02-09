from typing import Tuple

import numpy as np
import torch

from env.env import Env
from model.model import Model
from system.dqn.experience import Experience
from system.dqn.replay_buffer import ReplayBuffer

from .agent import Agent


class ValueBasedAgent(Agent):
    def __init__(self, env: Env, *args, **kwargs) -> None:
        super().__init__(env, *args, **kwargs)

    def get_action(self, net: Model, epsilon: float, device: str) -> int:
        if np.random.random() < epsilon:
            action = self.env.action_space.sample()
        else:
            state = torch.tensor([self.state])

            if device not in ["cpu"]:
                state = state.cuda(device)

            q_values = net(state)
            _, action = torch.max(q_values, dim=1)
            action = int(action.item())

        return action

    @torch.no_grad()
    def play_step(
        self,
        net: Model,
        epsilon: float = 0.0,
        device: str = "cpu",
        replay_buffer: ReplayBuffer = None,
    ) -> Tuple[float, bool]:
        action = self.get_action(net, epsilon, device)

        # do step in the environment
        new_state, reward, done, truncated, info = self.env.step(action)

        exp = Experience(self.state, action, reward, done, new_state)

        if replay_buffer is not None:
            replay_buffer.append(exp)

        self.state = new_state
        if done:
            self.reset()
        return reward, done
