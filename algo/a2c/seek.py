from gym import register
import gym


register(
    id='SimpleSeek-v0',
    entry_point='algo.a2c.seek:SeekEnv',
    max_episode_steps=999,
)

class SeekEnv(gym.Env):

    def __init__(self):
            from multiagent.environment import MultiAgentEnv
            import multiagent.scenarios as scenarios

            # load scenario from script
            scenario = scenarios.load("simple.py").Scenario()
            # create world
            world = scenario.make_world()
            # create multiagent environment
            self._env = MultiAgentEnv(world, scenario.reset_world, scenario.reward, scenario.observation)

    def step(self, action):
        obs_n, reward_n, done_n, info_n = self._env.step([action])
        return obs_n[0], reward_n[0], done_n[0], info_n

    def reset(self):
        return self._env.reset()[0]

    def render(self, mode='human'):
        self._env.render()

    @property
    def observation_space(self):
        return self._env.observation_space[0]

    @property
    def action_space(self):
        return self._env.action_space[0]
