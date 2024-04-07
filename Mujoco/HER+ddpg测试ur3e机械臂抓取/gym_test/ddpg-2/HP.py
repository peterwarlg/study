def get_hp(args):
    if args.ep == 'True':
        ep = True
    elif args.ep == 'False':
        ep = False
    else:
        ep = None

    seed = args.seed
    num_workers = args.num_workers
    device = args.device
    hidden_size = args.hidden_size
    sp_name = args.sp_name
    if args.mode == 'train':
        assert device == 'cpu' or device == 'gpu', 'wrong Device'
        assert seed is not None, 'Non seed'
        assert num_workers is not None, 'Non num_workers'
        assert ep is not None, '是否情景'
    print("*******************\n"
          "Hyper Params:\n"
          "seed: {}\n"
          "num_workers: {}\n"
          "device: {}\n"
          "hidden_size: {}\n"
          "ep: {}\n"
          'sp_name: {}\n'
          "*******************".format(seed, num_workers, device, hidden_size, ep, sp_name))
    hp_train = {
        'sp_name': sp_name,  # 备注
        'device': device,  # 硬件
        # 环境参数  environment
        'env_name': 'robotics_ur:ur3e-v3',  #'robotics_ur:ur3e-v0', 'FetchReach-v1', 'FetchPush-v1', 'FetchPickAndPlace-v1', 'FetchSlide-v1'
        'seed': seed,  # 随机种子  random seed for environment, torch, numpy, random packages
        'T': 50,  # 每幕最大步数  maximum episode length
        'ep': ep,
        # 训练参数  training setup
        'hidden_size': hidden_size,  # 网络节点数
        'num_workers': num_workers,  # 并行工程数         number of parallel workers
        'replay_strategy': 'future',
        # 'none': 纯ddpg, 'future': ddpg + HER     'none' for vanilla ddpg, 'future' for HER
        'n_epochs': 160,  # epochs数量        number of epochs, HER paper: 200 epochs (i.e. maximum of 8e6 timesteps)
        'n_cycles': 50,  # 每个epoch中的cycles      number of cycles per epoch, HER paper: 50 cycles
        'n_optim': 40,  # 每个cycle中的opti次数       number of optimization steps every cycle
        'n_eval_rollouts': 10,
        # 评估过程中的rollout次数   number of rollouts in evaluation, rollouts are episodes from num_workers
        # Agent超参数  Agent hyper-parameters
        'batch_size': 256,  # batch size per thread
        'lr_actor': 0.001,  # learning rate actor network
        'lr_critic': 0.001,  # learning rate critic network
        'buffer_size': int(1e6),  # replay-buffer size
        'tau': 0.05,  # soft update of network coefficient, 1-tau = polyak coefficient
        'gamma': 0.98,  # discount factor
        'clip_return': 50.,  # return clipping
        'clip_obs': 200.,  # observation clipping
        'clip_action': 1.,  # action clipping
        # 探索的概率         exploration
        'random_eps': 0.2,  # probability of random action in hypercube of possible actions
        'noise_eps': 0.05,  # std of gaussian noise added actions
        # normalization
        'norm_eps': 0.01,  # eps for observation normalization
        'norm_clip': 5.,  # normalized observations are clipped to this values
        # 保存结果的本地路径     location (path) of files for report
        'results_path': './tmp_results'
    }

    hp_test = {
        'device': 'cpu',  # 硬件
        # 环境参数  environment
        'env_name': 'FetchPickAndPlace-v1',  # 'FetchReach-v1', 'FetchPush-v1', 'FetchPickAndPlace-v1', 'FetchSlide-v1'
        'seed': 1,  # 随机种子  random seed for environment, torch, numpy, random packages
        'T': 50,  # 每幕最大步数  maximum episode length
        'ep': True,
        # 训练参数  training setup
        'hidden_size': 256,  # 网络节点数
        'replay_strategy': 'future',
        # 'none': 纯ddpg, 'future': ddpg + HER     'none' for vanilla ddpg, 'future' for HER
        'num_workers': 1,  # 并行工程数         number of parallel workers
        'n_epochs': 1,  # epochs数量        number of epochs, HER paper: 200 epochs (i.e. maximum of 8e6 timesteps)
        'n_cycles': 1,  # 每个epoch中的cycles      number of cycles per epoch, HER paper: 50 cycles
        'n_optim': 1,  # 每个cycle中的opti次数       number of optimization steps every cycle
        'n_eval_rollouts': 10,
        # 评估过程中的rollout次数   number of rollouts in evaluation, rollouts are episodes from num_workers
        # Agent超参数  Agent hyper-parameters
        'batch_size': 8,  # batch size per thread
        'lr_actor': 0.001,  # learning rate actor network
        'lr_critic': 0.001,  # learning rate critic network
        'buffer_size': int(1e6),  # replay-buffer size
        'tau': 0.05,  # soft update of network coefficient, 1-tau = polyak coefficient
        'gamma': 0.98,  # discount factor
        'clip_return': 50.,  # return clipping
        'clip_obs': 200.,  # observation clipping
        'clip_action': 1.,  # action clipping
        # 探索的概率         exploration
        'random_eps': 0.2,  # probability of random action in hypercube of possible actions
        'noise_eps': 0.05,  # std of gaussian noise added actions
        # normalization
        'norm_eps': 0.01,  # eps for observation normalization
        'norm_clip': 5.,  # normalized observations are clipped to this values
        # 保存结果的本地路径     location (path) of files for report
        'results_path': './tmp_results'
    }

    if args.mode == 'train':
        return hp_train
    elif args.mode == 'test':
        return hp_test


hp = {
    'count': 1,
    # 硬件
    'device': 'cpu',
    # 环境参数  environment
    'env_name': 'FetchPickAndPlace-v1',  # 'FetchReach-v1', 'FetchPush-v1', 'FetchPickAndPlace-v1', 'FetchSlide-v1'
    'seed': 2,  # 随机种子  random seed for environment, torch, numpy, random packages
    'T': 50,  # 每幕最大步数  maximum episode length

    # 训练参数  training setup
    'hidden_size': 256,  # 网络节点数
    'replay_strategy': 'future',  # 'none': 纯ddpg, 'future': ddpg + HER     'none' for vanilla ddpg, 'future' for HER
    'num_workers': 2,  # 并行工程数         number of parallel workers
    # 'n_epochs': 100,  # epochs数量        number of epochs, HER paper: 200 epochs (i.e. maximum of 8e6 timesteps)
    'n_epochs': 1,  # epochs数量        number of epochs, HER paper: 200 epochs (i.e. maximum of 8e6 timesteps)
    # 'n_cycles': 50,  # 每个epoch中的cycles      number of cycles per epoch, HER paper: 50 cycles
    'n_cycles': 1,  # 每个epoch中的cycles      number of cycles per epoch, HER paper: 50 cycles
    'n_optim': 40,  # 每个cycle中的opti次数       number of optimization steps every cycle
    'n_eval_rollouts': 10,  # 评估过程中的rollout次数   number of rollouts in evaluation, rollouts are episodes from num_workers

    # Agent超参数  Agent hyper-parameters
    'batch_size': 256,  # batch size per thread
    'lr_actor': 0.001,  # learning rate actor network
    'lr_critic': 0.001,  # learning rate critic network
    'buffer_size': int(1e6),  # replay-buffer size
    'tau': 0.05,  # soft update of network coefficient, 1-tau = polyak coefficient
    'gamma': 0.98,  # discount factor
    'clip_return': 50.,  # return clipping
    'clip_obs': 200.,  # observation clipping
    'clip_action': 1.,  # action clipping

    # 探索的概率         exploration
    'random_eps': 0.2,  # probability of random action in hypercube of possible actions
    'noise_eps': 0.05,  # std of gaussian noise added actions

    # normalization
    'norm_eps': 0.01,  # eps for observation normalization
    'norm_clip': 5.,  # normalized observations are clipped to this values

    # 保存结果的本地路径     location (path) of files for report
    'results_path': './tmp_results'
}
