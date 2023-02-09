from torch import nn

from .model import Model


class DenseModel(Model):
    def __init__(
        self,
        observation_space_size: int,
        action_space_size: int,
        *args,
        hidden_size: int = 128,
        **kwargs
    ) -> None:
        super(DenseModel, self).__init__(*args, **kwargs)

        self.model = nn.Sequential(
            nn.Linear(observation_space_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, action_space_size),
        )

    def forward(self, x):
        return self.model(x.float())
