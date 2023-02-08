import abc


class Env(abc.ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
