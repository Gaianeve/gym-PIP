from gym.envs.registration import register

register(
    id='PIP-v0',
    entry_point='gym_PIP.envs:RealMegaFufiEnv',
    max_episode_steps=1200,
)
