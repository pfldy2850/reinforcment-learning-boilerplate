import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import component as rlbase
import tensorflow as tf

# MODEL INIT -- START
class Model(rlbase.ModelAC):
	def create_model(self) -> None:
		self._input = tf.keras.Input(shape=(4,))

		common_net = tf.keras.layers.Dense(20)(self._input)
		common_net = tf.keras.layers.Dense(20)(common_net)
		common_net = tf.keras.layers.Dense(20)(common_net)

		self._actor = tf.keras.layers.Dense(20)(common_net)
		self._actor = tf.keras.layers.Dense(10)(self._actor)
		self._actor = tf.keras.layers.Dense(5)(self._actor)
		self._actor = tf.keras.layers.Dense(2)(self._actor)

		self._critic = tf.keras.layers.Dense(20)(common_net)
		self._critic = tf.keras.layers.Dense(10)(self._critic)
		self._critic = tf.keras.layers.Dense(5)(self._critic)
		self._critic = tf.keras.layers.Dense(1)(self._critic)
# MODEL INIT -- END


model = Model('./testmodel')
learner = rlbase.Learner(model)
actor1 = rlbase.Actor('./testmodel/actor.tflite')
actor2 = rlbase.Actor('./testmodel/actor.tflite')


for x in range(1000):
	if not actor1.is_finish():
		actor1.run_step(explore_rate=.5)
		actor1._environment._env.render()

	if not actor2.is_finish():
		actor2.run_step(explore_rate=.5)
		actor2._environment._env.render()
