# gym-domain

Reinforcement learning gyms for experimenting with domain generalization, domain adaptation, and robustness to domain shift.

#### DomainCartPole-v0

- based on OpenAI's https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
- changed to allow physics parameters to be customized on gym creation

Examples:
```
env = gym.make('DomainCartPole-v0', gravity=20.0)

env = gym.make('DomainCartPole-v0', half_length=5.0, tau=0.02)
```
