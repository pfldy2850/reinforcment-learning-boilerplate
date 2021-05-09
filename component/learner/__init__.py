from .learner import ILearner
from ..memory import Memory


def Learner(model, mem_type:str='deque') -> ILearner:
	memory 		= Memory(mem_type)

	return ILearner(model, memory)
