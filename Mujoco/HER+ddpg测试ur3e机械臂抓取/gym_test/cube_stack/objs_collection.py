import gym
import numpy as np
import globvar as gv
from ddpg.ddpg import ddpgAgent
from ddpg.hp import hp_train

env_name = 'ur3e-v4'
env = gym.make(env_name)
obs = env.reset()

hp_train['env_name'] = env_name
hp_train['dims'] = {
            'o': obs['observation'].shape[0],
            'u': env.action_space.shape[0],
            'g': obs['desired_goal'].shape[0],
            'info_is_success': 1,
        }

agent = ddpgAgent(hp_train)
agent.load_checkpoint(hp_train['results_path'], 'robotics_ur:ur3e-v3' + 'ep',isbackup=False)

def reset_cubes():
    pass

def pick():
    obs = env.reset_custom(gv.cube_xpos, gv.goal_xpos)
    g = [obs['desired_goal']]
    o = np.empty((1, hp_train['dims']['o']), np.float32)
    ag = np.empty((1, hp_train['dims']['g']), np.float32)
    o[:] = [obs['observation']]
    ag[:] = [obs['achieved_goal']]

    # 重置cube位置 重置target位置
    obs = env.reset_custom(np.array([0.3, 0.1]), np.array([0.3, -0.25, 1.2]))
    g = [obs['desired_goal']]
    o = np.empty((1, hp_train['dims']['o']), np.float32)
    ag = np.empty((1, hp_train['dims']['g']), np.float32)
    o[:] = [obs['observation']]
    ag[:] = [obs['achieved_goal']]

    for i in range(1000):
        env.render()

    for i in range(400):
        actions = agent.act(o, g, 0, 0)
        actions = actions.cpu().detach().numpy()
        obs_dict_new, _, done, info = env.step_custom(actions[0], "object0")
        env.render()
        o_new = obs_dict_new['observation']
        ag_new = obs_dict_new['achieved_goal']
        o[...] = o_new
        ag[...] = ag_new
        pass
    action = np.array([0, 0, 0, 0.05])
    for i in range(100):
        env.step_custom(action,"object0")
        env.render()

    for i in range(400):
        actions = agent.act(o, g, 0, 0)
        actions = actions.cpu().detach().numpy()
        obs_dict_new, _, done, info = env.step_custom(actions[0], "object2")
        env.render()
        o_new = obs_dict_new['observation']
        ag_new = obs_dict_new['achieved_goal']
        o[...] = o_new
        ag[...] = ag_new
        pass
    action = np.array([0, 0, 0, 0.05])
    for i in range(100):
        env.step_custom(action,"object2")
        env.render()

    for i in range(400):
        actions = agent.act(o, g, 0, 0)
        actions = actions.cpu().detach().numpy()
        obs_dict_new, _, done, info = env.step_custom(actions[0], "object1")

        qpos, qvel = env.get_robot_qpos()
        grip_xpos = env.get_grip_xpos()
        gv.data_joints.append(qpos)

        env.render()
        o_new = obs_dict_new['observation']
        ag_new = obs_dict_new['achieved_goal']
        # success = np.array([i['is_success'] for i in info])
        o[...] = o_new
        ag[...] = ag_new
        pass
    action = np.array([0, 0, 0, 0.05])

    for i in range(200):
        env.step(action)
        env.render()


if __name__ == '__main__':
    pick()
    while 1:
        env.render()
