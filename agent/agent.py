import abc


class Agent(abc.ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
