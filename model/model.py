import abc
import os

import torch
from torch import nn


class Model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super(Model, self).__init__()
