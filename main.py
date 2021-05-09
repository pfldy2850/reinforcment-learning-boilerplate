import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import component as rlbase
import tensorflow as tf


if __name__ == '__main__':
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
	system = rlbase.System(
		model,
		'./testmodel/actor.tflite',
		actor_num=10,
		sys_type='mtp',
		parallel=5
	)

	for explore_rate in range(11):
		system.learn(10, explore_rate=(1-explore_rate/10), visible=False)

	system.demo()
