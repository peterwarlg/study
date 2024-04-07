hp_train = {
    'sample_her_transitions': None,

    'sp_name': None,  # 备注
    'device': 'cpu',  # 硬件
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