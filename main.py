import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import agent
import env
import memory
import model
import system
import tensorflow as tf


if __name__ == '__main__':

	system = system.create_system(
	    actor_num=1,
	    env_num=2,
	)
	print(system)

	system.train(episode=100, explore_rate=(lambda x: x/100))
