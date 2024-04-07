import gym
import numpy as np
import torch

from ddpg import ddpgAgent
env_name = 'ur3e-v3'
env = gym.make(env_name)
# env = gym.make('FetchPickAndPlace-v1')
obs = env.reset()

hp_train = {
    'sample_her_transitions': None,
    'dims': {
        'o': obs['observation'].shape[0],
        'u': env.action_space.shape[0],
        'g': obs['desired_goal'].shape[0],
        'info_is_success': 1,
    },
    'sp_name': None,  # 备注
    'device': 'cpu',  # 硬件
    'env_name': env_name,  # 'robotics_ur:ur3e-v1', 'FetchReach-v1', 'FetchPush-v1', 'FetchPickAndPlace-v1', 'FetchSlide-v1'
    'seed': 2,  # 随机种子  random seed for environment, torch, numpy, random packages
    'T': 50,  # 每幕最大步数  maximum episode length
    'ep': None,
    'hidden_size': 256,  # 网络节点数
    'num_workers': 32,  # 并行工程数         number of parallel workers
    'replay_strategy': 'future',
    'n_epochs': 300,  # epochs数量        number of epochs, HER paper: 200 epochs (i.e. maximum of 8e6 timesteps)
    'n_cycles': 50,  # 每个epoch中的cycles      number of cycles per epoch, HER paper: 50 cycles
    'n_optim': 40,  # 每个cycle中的opti次数       number of optimization steps every cycle
    'n_eval_rollouts': 10,
    'batch_size': 256,  # batch size per thread
    'lr_actor': 0.001,  # learning rate actor network
    'lr_critic': 0.001,  # learning rate critic network
    'buffer_size': int(1e6),  # replay-buffer size
    'tau': 0.05,  # soft update of network coefficient, 1-tau = polyak coefficient
    'gamma': 0.98,  # discount factor
    'clip_return': 50.,  # return clipping
    'clip_obs': 200.,  # observation clipping
    'clip_action': 1.,  # action clipping
    'random_eps': 0.2,  # probability of random action in hypercube of possible actions
    'noise_eps': 0.05,  # std of gaussian noise added actions
    'norm_eps': 0.01,  # eps for observation normalization
    'norm_clip': 5.,  # normalized observations are clipped to this values
    # 保存结果的本地路径     location (path) of files for report
    'results_path': '/home/wangzitu/gym_test/ddpg-2/trained/PickAndPlace/ur3e-v3-195'
}

# agent = ddpgAgent(hp_train)
agent = ddpgAgent(hp_train)
agent.load_checkpoint(hp_train['results_path'], 'robotics_ur:ur3e-v3' + 'ep',isbackup=False)

data_joints = []
data_mocap = []


for t in range(100):
    obs = env.reset()
    g = [obs['desired_goal']]

    o = np.empty((1, hp_train['dims']['o']), np.float32)
    ag = np.empty((1, hp_train['dims']['g']), np.float32)
    o[:] = [obs['observation']]
    ag[:] = [obs['achieved_goal']]

    obs, achieved_goals, acts, goals, successes = [], [], [], [], []


    for i in range(500):
        actions = agent.act(o, g, 0, 0)
        actions = actions.cpu().detach().numpy()
        obs_dict_new, _, done, info = env.step(actions[0])

        qpos, qvel = env.get_robot_qpos()
        grip_xpos = env.get_grip_xpos()
        data_joints.append(qpos)
        data_mocap.append(grip_xpos)

        # print(qpos)
        env.render()
        o_new = obs_dict_new['observation']
        ag_new = obs_dict_new['achieved_goal']
        # success = np.array([i['is_success'] for i in info])
        o[...] = o_new
        ag[...] = ag_new

# data_joints = np.array(data_joints)
# data_mocap = np.array(data_mocap)
# np.savetxt('joints_data.txt', data_joints)
# np.savetxt('mocap_data.txt', data_mocap)



