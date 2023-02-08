from .actor import IActor
from env import EEnvType, create_environment
from agent import create_agent
from memory import create_memory

import random

class ActorNormal(IActor):

    def __init__(self,
        env_type:EEnvType=EEnvType.CARTPOLE,
        env_num:int=1):

        super().__init__(
            env_type=env_type,
            env_num=env_num
        )

        assert env_num > 0, "ActorNormal must have at least one environment."

        self._envs = [ create_environment(env_type) for _ in range(self._env_num) ]
        self._agent = create_agent()
        self._memory = create_memory('deque')

    def __str__(self):
        string_buffer = super().__str__().split('\n')
        string_buffer.append(self._get_string_agent())
        string_buffer.append(self._get_string_envs())
        return "\n".join(string_buffer)


    def run(self, explore_rate:float=0):
        # reset environments
        self._memory.clear()
        for env in self._envs: env.reset()

        while True:
            # check live envs
            live_env_indices = [ i for i in range(len(self._envs)) if not self._envs[i].is_finish() ]
            if len(live_env_indices) == 0: break
            live_env_explores = [ random.random() <= explore_rate for i in live_env_indices ]

            # get states
            states = [ self._envs[i].get_state() for i in live_env_indices ]

            # get actions
            actions_exploit = self._agent.get_actions(states)
            actions_explore = [ random.randrange(0, self._envs[i].get_action_size()) for i in live_env_indices ]
            actions = [ actions_explore[i]*int(live_env_explores[i]) + actions_exploit[i]*(1-int(live_env_explores[i])) for i in range(len(live_env_explores)) ]

            # run actions
            is_done = [ int(self._envs[live_env_indices[i]].run_action(actions[i])) for i in range(len(live_env_indices)) ]

            # get rewards
            rewards = [ self._envs[i].get_reward() for i in live_env_indices ]

            # get next states
            next_states = [ self._envs[i].get_state() for i in live_env_indices ]

            # get is finish
            is_finish = [ int(self._envs[i].is_finish()) for i in live_env_indices ]

            self._memory.concat([ [states[i], actions[i], is_done[i], rewards[i], next_states[i], is_finish[i]] for i in range(len(live_env_indices)) ])

        print(self._memory.length())
        pass
