from gym.envs.registration import register

register(
    id='DomainCartPole-v0',
    entry_point = 'gym_stochastic.envs:DomainCartPoleEnv',
)
