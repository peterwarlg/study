import gym
import numpy as np

np.set_printoptions(suppress=True)
e = gym.make('robotics_ur:ur3e-v0')
# e = gym.make('FetchPickAndPlace-v1')

current_pos = e.reset()
print(current_pos['observation'][:3], current_pos['observation'][9:11], current_pos['observation'][3:6])
# print(e.action_space[0])
current = current_pos['observation'][[0, 1, 2]]
target = current_pos['observation'][[]]

#
# while 1:
#     e.step([0,0,0,0])
#     e.render()

def move_target(e, target):
    # target[2] += 0.01

    obs, _, _, _ = e.step([0, 0, 0, 0])
    while np.sum((np.abs(obs['observation'][[0, 1, 2]] - target[:3]))) > 0.00:
        action = (target - obs['observation'][[0, 1, 2, 9]])
        action[3] = -0.4
        obs, _, _, _ = e.step(action)
        e.render()
        # print(target, obs['observation'][[0, 1, 2, 9]])


move_target(e, np.concatenate((current_pos['desired_goal'],[-0.4])))

for i in range(5):
    e.step([0, 0, 0, 0.0])
    e.render()
# for i in range(50):
#     e.step([0, 0, 0, 0])
#     e.render()
for i in range(1000):
    e.step([0, 0, 0.1, -0.2])
    e.render()

# while 1:
    #     action = e.action_space.sample()
    #     e.step(action)
    # e.render()
