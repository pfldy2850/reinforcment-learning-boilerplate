from .model import IModel
import os
import tensorflow as tf
import numpy as np

class ModelTFLite(IModel):

	def __init__(self, model_path:str):
		self._model_path = model_path
		self.load()

	def get_action_prob(self, state):
		self._interpreter.set_tensor(self._input_index, np.reshape(state, self._input_shape).astype(np.float32))
		self._interpreter.invoke()
		return self._interpreter.get_tensor(self._output_index)[0]

	def get_action(self, state):
		action_prob = self.get_action_prob(state)
		return np.argmax(action_prob)

	def train(self, data):
		assert False, "ModelTFLite cannot train the model."

	def load(self):
		assert os.path.exists(self._model_path), f"File not Found '{self._model_path}'."

		self._interpreter = tf.lite.Interpreter(model_path=self._model_path)
		self._interpreter.allocate_tensors()

		input_details = self._interpreter.get_input_details()
		output_details = self._interpreter.get_output_details()
		self._input_shape = input_details[0]['shape']
		self._input_index = input_details[0]['index']
		self._output_shape = output_details[0]['shape']
		self._output_index = output_details[0]['index']

	def save(self, tflite:bool=False):
		assert False, "ModelTFLite cannot save the model."
