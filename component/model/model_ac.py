from . import IModel
import abc
import os
import tensorflow as tf

class ModelAC(IModel):
	def __init__(self, model_path:str, discount:float=0.99, batch_size:int=100):
		self.create_model()
		self.compile_model()
		assert self._actor is not None, 'create actor model.'
		assert self._critic is not None, 'create critic model.'

		self._discount 		= discount
		self._batch_size 	= batch_size
		self._model_path 	= model_path

		self.save(tflite=True)

	@abc.abstractmethod
	def create_model(self) -> None:
		pass

	def compile_model(self) -> None:
		self._critic = tf.keras.models.Model(inputs=self._input, outputs=self._critic, name="critic")
		self._critic.compile(
			optimizer='adam',
			loss=tf.losses.MeanSquaredError()
		)

		self._actor = tf.keras.models.Model(inputs=self._input, outputs=self._actor, name="actor")
		# def _actor_loss(y_true, y_pred):
		#     log_prob = tf.keras.backend.log(y_pred) * y_true
		#     return - tf.keras.backend.sum(log_prob)
		self._actor.compile(
			optimizer='adam',
			loss=(lambda y_true, y_pred: - tf.keras.backend.sum(tf.keras.backend.log(y_pred) * y_true))
		)


	def get_action_prob(self, state):
		return self._actor.predict(state)[0]

	def get_action_prob_list(self, state):
		return self._actor.predict(state)

	def get_action(self, state):
		action_prob = self.get_action_prob()
		return np.argmax(action_prob)

	def train(self, data):
		# data -> state, action, reward, next_state, done, finish
		states 		= np.array([ d[0] for d in data ])
		actions 	= np.array([ d[1] for d in data ])
		rewards 	= np.array([ d[2] for d in data ])
		next_states = np.array([ d[3] for d in data ])

		done 		= np.array([ 1 - int(d[4]) for d in data ])

		values 		= rewards + self._discount * self._critic.predict(next_states) * done
		advantages 	= self._critic.predict(states) - values

		self._actor.fit(states, advantages, epochs=1, verbose=0, batch_size=self._batch_size)
		self._critic.fit(states, values, epochs=1, verbose=0, batch_size=self._batch_size)

	def load(self):
		assert os.path.isdir(self._model_path), f"Directory not found '{self._model_path}'"

		self._actor.load_weights(os.path.join(self._model_path, 'actor.h5'))
		self._critic.load_weights(os.path.join(self._model_path, 'critic.h5'))

	def save(self, tflite:bool=False):
		if not os.path.isdir(self._model_path): os.mkdir(self._model_path)
		
		self._actor.save_weights(os.path.join(self._model_path, 'actor.h5'))
		self._critic.save_weights(os.path.join(self._model_path, 'critic.h5'))

		if tflite: self.save_tflite()

	# tflite save
	def save_tflite(self):
		actor_model = tf.lite.TFLiteConverter.from_keras_model(self._actor).convert()
		with open(os.path.join(self._model_path, 'actor.tflite'), 'wb') as f: f.write(actor_model)

		critic_model = tf.lite.TFLiteConverter.from_keras_model(self._critic).convert()
		with open(os.path.join(self._model_path, 'critic.tflite'), 'wb') as f: f.write(critic_model)
