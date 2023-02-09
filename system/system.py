import abc
import types

import pytorch_lightning as pl

from agent import Agent
from env import Env
from model import Model


class System(pl.LightningModule):
    def __init__(self, env: Env, model: Model, agent: Agent, *args, **kwargs):
        super(System, self).__init__()
        self.env = env
        self.model = model
        self.agent = agent
