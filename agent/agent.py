import abc
from model import IModel, create_model

class IAgent(abc.ABC):

    def __init__(self):
        pass

    def __str__(self):
        string_buffer = []
        string_buffer.append(f"[{self.__class__.__name__} at {hex(id(self))}]")
        return "\n".join(string_buffer)

    def get_actions(self, states):
        # assert self._model is not None, "model is none"
        # self._model.get_action()
        return [ 0 for _ in range(len(states))]

    def set_model(self, model_config:dict) -> None:
        self._model = create_model(model_config)

    def get_model(self) -> IModel:
        return self._model

    ''' Virtual Methods - START '''
    ''' Virtual Methods - END '''
