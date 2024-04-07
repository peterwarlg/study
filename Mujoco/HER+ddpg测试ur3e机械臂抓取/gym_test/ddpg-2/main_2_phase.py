from HP import get_hp

'''
三种可能:
    1. baselines_epochs-120_no-ep_netnode-256_workers-32
    2. 纯粹情景
    3. 一半情景+一半无情景
'''

import numpy as np
import torch
import random
import gym
import mujoco_py

import progressbar as pb  # tracking time while training
import matplotlib.pyplot as plt  # plotting scores

from ddpg_2_phase import ddpgAgent
from rollout import RolloutWorker
from her_sampler import make_sample_her_transitions
from parallelEnvironment import parallelEnv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default=None, help='train or test')
parser.add_argument('--seed', type=int, default=None, help='任意整形')
parser.add_argument('--num_workers', type=int, default=None, help='workers数量')
parser.add_argument('--ep', type=str, default=None, help='True or False')
parser.add_argument('--device', type=str, default='cpu', help='cpu or gpu')
parser.add_argument('--hidden_size', type=int, default=256, help='全连接层节点数量')
parser.add_argument('--sp_name', type=str, default='', help='')
parser.add_argument('--show', type=str, default='True', help='')
args = parser.parse_args()
assert args.mode is not None, 'Train or Test'

hp = get_hp(args)


def set_seeds(seed: int = 0):
    """
    Set the random seed to all packages.
    Note: Parallel workers will have different seeds in each environment based on this seed.
    @param seed: (int) seed for torch, numpy, random. By default zero.
    """
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    pass


def dims_and_reward_fun(env_name: str):
    """"""
    """
    Get dimensions of observations, action, goal and the used reward function.
    @param env_name: (str) name of gym environment
    @return: dict for dimensions, reward function of environment
    """
    env = gym.make(env_name)
    env.reset()
    obs, _, _, _ = env.step(env.action_space.sample())
    dims = {
        'o': obs['observation'].shape[0],
        'u': env.action_space.shape[0],
        'g': obs['desired_goal'].shape[0],
        'info_is_success': 1,
    }
    return dims, env.compute_reward


def train(agent: ddpgAgent, rollout_worker, evaluation_worker):
    """
    Train DDPG (+ HER is optional) with multiple workers and save values to scores.
    @param agent: (object) DDPG agent
    @param rollout_worker: (object) worker for training the networks
    @param evaluation_worker: (object) worker for evaluating current networks
    @return: scores i.e. success-rate of agent from evaluating worker in a list
    """
    """
    开多个worker，将 values 保存到 scores
    @参数：agent ： ddpg agent
    @参数：rollout_worker: 用于训练的 worker 对象
    @参数：evaluation_worker：用于评估的 worker 对象
    @返回值：scores：成功率，一个列表，返回 evaluation_worker 的成功率
    """
    switch_flag = False
    judge_flag = False
    scores = []
    print("当前训练环境: ", hp['env_name'], "started...")
    print("最大训练步数: ",
          hp['n_epochs'] * hp['n_cycles'] * hp['T'] * hp['num_workers'], "in",
          hp['n_epochs'], "epochs with", hp['num_workers'], "parallel workers.")

    # 训练过程中显示进度的配件  widget bar to display progress during training
    widget = ['training loop: ', pb.Percentage(), ' ', pb.Bar(), ' ', pb.ETA()]
    timer = pb.ProgressBar(widgets=widget, maxval=hp['n_epochs']).start()

    # 开始训练
    for epoch in range(hp['n_epochs']):

        # 切换her的sample，在30epoch之后不采用ep
        if epoch > 1 and not switch_flag and judge_flag:
            switch_flag = True
            print('switch stratage of HER')
            agent.sample_transitions = agent.sample_transitions_2
            agent.buffer.sample_transitions = agent.sample_transitions_2

        for _ in range(hp['n_cycles']):
            # 每个平行环境中产生episodes
            episode = rollout_worker.generate_rollouts()  # generate episodes with every parallel environment
            # agent保存为一整个episodes，
            agent.store_episode(episode)  # store experiences as whole episodes
            # 训练
            for _ in range(hp['n_optim']):  # optimize target network
                agent.learn()
            # 更新target网络
            agent.soft_update_target_networks()  # update target network

        # 评估策略， evaluating agent for report
        eval_scores = []

        # 每个eva_worker评估rollouts次
        # 一次rollout就是n个环境执行一次， evaluation_worker.success_rate是这n个worker一次中几个成功
        for _ in range(hp['n_eval_rollouts']):
            evaluation_worker.generate_rollouts()
            eval_scores.append(evaluation_worker.success_rate)

            pass
        print('\n \tEpoch: {} / {}, Success: {:.4f}'.format(epoch, hp['n_epochs'], np.mean(eval_scores)))
        if np.mean(eval_scores) > 0.35:
            judge_flag = True

        scores.append(np.mean(eval_scores))

        timer.update(epoch)
        if (epoch + 1) % 20 == 0:
            print("\n=================SAVE AGENT=================\n")
            agent.save_checkpoint(hp['results_path'], hp['env_name'] + 'ep')

    timer.finish()
    return scores


def main():
    """
    Main function: Training ddpg agent (optional with HER) as defined in hp and saving stats.
    """
    set_seeds(hp['seed'])
    # 平行环境，实例唯一
    env = parallelEnv(hp['env_name'], n=hp['num_workers'], seed=hp['seed'])

    hp['dims'], hp['reward_fun'] = dims_and_reward_fun(hp['env_name'])

    hp['sample_her_transitions'] = make_sample_her_transitions(
        replay_strategy=hp['replay_strategy'], replay_k=4, reward_fun=hp['reward_fun'], ep=True, switch=True)

    hp['sample_her_transitions_2'] = make_sample_her_transitions(
        replay_strategy=hp['replay_strategy'], replay_k=4, reward_fun=hp['reward_fun'], ep=False, switch=True)

    ''' 创建三个主要对象， ddpg的agent、buffer生成器、策略评估器 '''
    agent = ddpgAgent(hp)
    rollout_worker = RolloutWorker(env, agent, hp)
    evaluation_worker = RolloutWorker(env, agent, hp, evaluate=True)

    '''训练'''
    scores = train(agent, rollout_worker, evaluation_worker)

    '''# 保存网络和状态   save networks and stats
    # ------------------------------------------------------------------------------------------
    '''
    if args.mode == 'train':
        np.savetxt(
            hp['results_path'] +
            '/scores_' +
            '环境:' + hp['env_name'] + '_' +
            'seed:' + str(hp['seed']) + '_' +
            '线程数:' + str(hp['num_workers']) + '_' +
            '是否ep:' + str(hp['ep']) + '_' +
            '网络节点数' + str(hp['hidden_size']) + '_' +
            'epochs: ' + str(hp['n_epochs']) + '_' +
            '备注:' + hp['sp_name'] +
            '.csv',
            scores, delimiter=',')

        fig = plt.figure()
        fig.add_subplot(111)
        plt.plot(np.arange(len(scores)), scores)
        plt.savefig(
            hp['results_path'] +
            '/scores_' +
            '环境:' + hp['env_name'] + '_' +
            'seed:' + str(hp['seed']) + '_' +
            '线程数:' + str(hp['num_workers']) + '_' +
            '是否ep:' + str(hp['ep']) + '_' +
            '网络节点数' + str(hp['hidden_size']) + '_' +
            'epochs: ' + str(hp['n_epochs']) + '_' +
            '备注:' + hp['sp_name'] +
            '.png')
        if args.show == 'False':
            pass
        else:
            plt.show()
        agent.save_checkpoint(hp['results_path'], hp['env_name'] + 'ep')


if __name__ == '__main__':
    main()
