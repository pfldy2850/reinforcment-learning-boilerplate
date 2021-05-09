from .memory import IMemory
from .memory_deque import MemoryDeque

# Constants
MEM_TYPES = [
	'deque',
	'none'
]

# Factory
def Memory(mem_type:str) -> IMemory:
	assert mem_type in MEM_TYPES, f"There isn't a memory which type is '{mem_type}'."

	if mem_type == 'deque':
		return MemoryDeque()
	elif mem_type == 'none':
		return None
