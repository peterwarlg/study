import gym
import numpy as np

np.set_printoptions(suppress=True)
e = gym.make('robotics_ur:ur3e-v1')
# e = gym.make('FetchPickAndPlace-v1')

e.reset()

# for i in range(5):
#     e.step([0, 0, 0, -0.2])
#     e.render()
# for i in range(50):
#     e.step([0, 0, 0, 0])
#     e.render()
for i in range(1000):
    e.step([0, 0, 0.1, 0.1])
    e.render()

