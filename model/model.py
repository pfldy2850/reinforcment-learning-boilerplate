import abc
import os

import torch
from torch import nn


class Model(nn.Module, abc.ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
