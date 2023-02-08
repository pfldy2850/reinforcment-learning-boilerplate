from .model import IModel
from .model_ac import ModelAC
from .model_tflite import ModelTFLite

# Constants
MODEL_TYPES = [
	'tflite'
]

# Factory
def create_model(model_path, model_type:str) -> IModel:
	assert model_type in MODEL_TYPES, f"There isn't a model which type is '{model_type}'."

	if model_type == 'tflite':
		return ModelTFLite(model_path)
