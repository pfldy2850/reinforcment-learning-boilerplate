import abc
import types

import pytorch_lightning as pl

from env import Env
from model import Model


class System(pl.LightningModule, abc.ABC):
    def __init__(self, env: Env, model: Model, *args, **kwargs):
        super().__init__()
        self._env = env
        self._model = model
