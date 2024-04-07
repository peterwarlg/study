import numpy as np
from HP import hp


def make_sample_her_transitions(replay_strategy, replay_k, reward_fun, ep):
    if ep:
        print("************************ Using ep ************************ \n")
    else:
        print("************************ Not using ep ************************\n")
    """
    Creates a sample function that can be used for HER experience replay.
    @param replay_strategy: (in ['future', 'none']) the HER replay strategy; if set to 'none',
            regular DDPG experience replay is used
    @param replay_k: (int) the ratio between HER replays and regular replays (e.g. k = 4 -> 4 times
            as many HER replays as regular replays are used)
    @param reward_fun: (function): function to re-compute the reward with substituted goals
    @return: transitions
    """
    if replay_strategy == 'future':
        future_p = 1 - (1. / (1 + replay_k))
    else:  # 'replay_strategy' == 'none'
        future_p = 0

    def _sample_her_transitions(episode_batch, batch_size_in_transitions):
        """
        Sampling the transitions with substituting goals for HER.
        @param episode_batch: {key: array(buffer_size x T x dim_key)} containing observation 'o', achieved goal 'ag',
        goal 'g', action 'u', reward 'r', info (i.e. success)
        @param batch_size_in_transitions: batch size of transitions
        @return: transitions
        """
        """
        episode_batch: 
            {o, u, g, ag, r, info},shape为 <dim_key * buffer * T>, 即 <键的数量 * 50 * buffer_size>
            键为： dict_keys(['o', 'u', 'g', 'info_is_success', 'ag', 'o_2', 'ag_2'])
            每个键的形状为： worker的数量 * 每幕步长（50） * 对应的特征维度（比如状态为25，动作为4）
        batch_size_in_transitions: 256; batch size of transitions
        """
        T = episode_batch['u'].shape[1]  # episode (rollouts) horizon = 50
        rollout_batch_size = episode_batch['u'].shape[0]  # worker的数量 equals to number of workers
        batch_size = batch_size_in_transitions  # 256

        # Select which episodes and time steps to use.
        # 在worker中选256次， [n] * 256, n: 1-9,代表worker下标
        episode_idxs = np.random.randint(0, rollout_batch_size, batch_size)  # sample random ids of workers
        # 在steps中选256次， [n] * 256, n: 0-50,代表step下标
        t_samples = np.random.randint(T, size=batch_size)  # random timestep samples from episode

        # 原始 episode_batch = key * (workers * T * dim)
        # 选出来一共 batch_size (256) 个transition, transiton[key] = (256, key的维度)
        transitions = {key: episode_batch[key][episode_idxs, t_samples].copy()  # stacking whole batch to one dict
                       for key in episode_batch.keys()}

        # Select future time indexes proportional with probability future_p. These
        # will be used for HER replay by substituting in future goals.

        # 256个, 根据future_p随机采样出下标 [random * 256] -> [random * 256] < 0.8 -> [True/False * 256]
        # 返回所有为True的下标
        her_indexes = np.where(np.random.uniform(size=batch_size) < future_p)  # indices for hindsight goal substitution
        # batch中 [random * 256] *  50-[x:0~50]
        future_offset = np.random.uniform(size=batch_size) * (T - t_samples)
        future_offset = future_offset.astype(int)

        '''
        future_t = [256 * rando(0-50) + 1 + offset][her_index]
        # 在t_samples先加offset，再按her_indexes为下标取值
        # future_t长度在[0-256]之间
        '''
        future_t = (t_samples + 1 + future_offset)[her_indexes]

        # Replace goal with achieved goal but only for the previously-selected
        # HER transitions (as defined by her_indexes). For the other transitions,
        # keep the original goal.
        # 根据之前挑选的her_indexes, 将transition中的goal换成achieved_goal, 其余不变
        # 采样的step为t，此时取得goal为t之后的随机某个ep中的goal，为future_t
        future_ag = episode_batch['ag'][episode_idxs[her_indexes], future_t]
        transitions['g'][her_indexes] = future_ag
        # Reconstruct info dictionary for reward computation.
        info = {}
        for key, value in transitions.items():
            if key.startswith('info_'):
                info[key.replace('info_', '')] = value

        # Re-compute reward since we may have substituted the goal.
        reward_params = {k: transitions[k] for k in ['ag_2', 'g']}
        reward_params['info'] = info
        transitions['r'] = reward_fun(reward_params['ag_2'], reward_params['g'], reward_params['info'])
        transitions = {k: transitions[k].reshape(batch_size, *transitions[k].shape[1:])
                       for k in transitions.keys()}
        assert (transitions['u'].shape[0] == batch_size_in_transitions)

        return transitions

    # 以当前选择的step到最终，也就是T，之间的距离为奖赏，要*一个因子，增大奖赏值
    def _sample_her_transitions_with_ep(episode_batch, batch_size_in_transitions):
        """
        episode_batch:
            {o, u, g, ag, r, info},shape为 <dim_key * buffer * T>, 即 <键的数量 * 50 * buffer_size>
            键为： dict_keys(['o', 'u', 'g', 'info_is_success', 'ag', 'o_2', 'ag_2'])
            每个键的形状为： worker的数量 * 每幕步长（50） * 对应的特征维度（比如状态为25，动作为4）
        batch_size_in_transitions: 256; batch size of transitions
        """
        T = episode_batch['u'].shape[1]  # episode (rollouts) horizon = 50
        rollout_batch_size = episode_batch['u'].shape[0]  # 不对 该值无限递增 worker的数量 equals to number of workers
        batch_size = batch_size_in_transitions  # 256
        # Select which episodes and time steps to use.

        # 在replay buffer中选256次， [n] * 256, n: 1-9,代表worker下标
        episode_idxs = np.random.randint(0, rollout_batch_size, batch_size)  # sample random ids of workers
        # 在steps中选256次， [n] * 256, n: 0-50,代表step下标
        t_samples = np.random.randint(T, size=batch_size)  # random timestep samples from episode

        # 每个worker-step占最大步数的百分比
        ratio_index = np.array(range(len(episode_idxs)), dtype=np.float32)

        for i in range(len(ratio_index)):
            ratio_index[i] = float(t_samples[i] / T)

        # 原始 episode_batch = key * (workers * T * dim)
        # 选出来一共 batch_size (256) 个transition, transiton[key] = (256, key的维度)
        transitions = {key: episode_batch[key][episode_idxs, t_samples].copy()  # stacking whole batch to one dict
                       for key in episode_batch.keys()}

        # 256个, 根据future_p随机采样出下标 [random * 256] -> [random * 256] < 0.8 -> [True/False * 256]
        # 返回所有为True的下标
        her_indexes = np.where(np.random.uniform(size=batch_size) < future_p)  # indices for hindsight goal substitution
        # batch中 [random * 256] *  50-[x:0~50]
        future_offset = np.random.uniform(size=batch_size) * (T - t_samples)
        future_offset = future_offset.astype(int)

        # future_t = [256 * rando(0-50) + 1 + offset][her_index]
        # 在t_samples先加offset，再按her_indexes为下标取值
        # future_t长度在[0-256]之间, 全为-1,即取每个episode的最后一个state为goal
        future_t = np.array([-1] * len(t_samples))
        future_t = future_t[her_indexes]

        # Replace goal with achieved goal but only for the previously-selected
        # HER transitions (as defined by her_indexes). For the other transitions,
        # keep the original goal.
        # 根据之前挑选的her_indexes, 将transition中的goal换成achieved_goal, 其余不变
        # 采样的step为t，此时取得goal为当前episode中最后一个transition
        future_ag = episode_batch['ag'][episode_idxs[her_indexes], future_t]

        transitions['g'][her_indexes] = future_ag

        # Reconstruct info dictionary for reward computation.
        info = {}
        for key, value in transitions.items():
            if key.startswith('info_'):
                info[key.replace('info_', '')] = value

        # Re-compute reward since we may have substituted the goal.
        reward_params = {k: transitions[k] for k in ['ag_2', 'g']}
        reward_params['info'] = info
        transitions['r'] = reward_fun(reward_params['ag_2'], reward_params['g'], reward_params['info'])

        reward = transitions['r']
        for i in her_indexes:
            reward[i] = (ratio_index[i] - 1) / 2
        transitions['r'] = reward

        transitions = {k: transitions[k].reshape(batch_size, *transitions[k].shape[1:])
                       for k in transitions.keys()}

        assert (transitions['u'].shape[0] == batch_size_in_transitions)
        return transitions

    # 以future_t 和所选择的step 的距离差为奖赏
    def _sample_her_transitions_with_ep_future(episode_batch, batch_size_in_transitions):
        """
        Sampling the transitions with substituting goals for HER.
        @param episode_batch: {key: array(buffer_size x T x dim_key)} containing observation 'o', achieved goal 'ag',
        goal 'g', action 'u', reward 'r', info (i.e. success)
        @param batch_size_in_transitions: batch size of transitions
        @return: transitions
        """
        """
        episode_batch: 
            {o, u, g, ag, r, info},shape为 <dim_key * buffer * T>, 即 <键的数量 * 50 * buffer_size>
            键为： dict_keys(['o', 'u', 'g', 'info_is_success', 'ag', 'o_2', 'ag_2'])
            每个键的形状为： worker的数量 * 每幕步长（50） * 对应的特征维度（比如状态为25，动作为4）
        batch_size_in_transitions: 256; batch size of transitions
        """
        T = episode_batch['u'].shape[1]  # episode (rollouts) horizon = 50
        rollout_batch_size = episode_batch['u'].shape[0]  # worker的数量 equals to number of workers
        batch_size = batch_size_in_transitions  # 256

        # Select which episodes and time steps to use.
        # 在worker中选256次， [n] * 256, n: 1-9,代表worker下标
        episode_idxs = np.random.randint(0, rollout_batch_size, batch_size)  # sample random ids of workers
        # 在steps中选256次， [n] * 256, n: 0-50,代表step下标
        t_samples = np.random.randint(T, size=batch_size)  # random timestep samples from episode

        # 原始 episode_batch = key * (workers * T * dim)
        # 选出来一共 batch_size (256) 个transition, transiton[key] = (256, key的维度)
        transitions = {key: episode_batch[key][episode_idxs, t_samples].copy()  # stacking whole batch to one dict
                       for key in episode_batch.keys()}

        # Select future time indexes proportional with probability future_p. These
        # will be used for HER replay by substituting in future goals.

        # 256个, 根据future_p随机采样出下标 [random * 256] -> [random * 256] < 0.8 -> [True/False * 256]
        # 返回所有为True的下标
        her_indexes = np.where(np.random.uniform(size=batch_size) < future_p)  # indices for hindsight goal substitution
        # batch中 [random * 256] *  50-[x:0~50]
        future_offset = np.random.uniform(size=batch_size) * (T - t_samples)
        future_offset = future_offset.astype(int)

        # future_t = [256 * rando(0-50) + 1 + offset][her_index]
        # 在t_samples先加offset，再按her_indexes为下标取值
        # future_t长度在[0-256]之间
        future_t_without_her = t_samples + 1 + future_offset
        future_t = (t_samples + 1 + future_offset)[her_indexes]
        # Replace goal with achieved goal but only for the previously-selected
        # HER transitions (as defined by her_indexes). For the other transitions,
        # keep the original goal.
        # 根据之前挑选的her_indexes, 将transition中的goal换成achieved_goal, 其余不变
        # 采样的step为t，此时取得goal为t之后的随机某个ep中的goal，为future_t
        future_ag = episode_batch['ag'][episode_idxs[her_indexes], future_t]
        transitions['g'][her_indexes] = future_ag
        # Reconstruct info dictionary for reward computation.
        info = {}
        for key, value in transitions.items():
            if key.startswith('info_'):
                info[key.replace('info_', '')] = value

        # Re-compute reward since we may have substituted the goal.
        reward_params = {k: transitions[k] for k in ['ag_2', 'g']}
        reward_params['info'] = info
        transitions['r'] = reward_fun(reward_params['ag_2'], reward_params['g'], reward_params['info'])
        # print(transitions['r'].shape)
        # future_t.shape == her_indexes[0].shape
        # t_samples.shape == transitions['r'].shape == batch_size
        reward = transitions['r']
        for i in her_indexes[0]:
            if reward[i] < -0.:
                reward[i] = (-(future_t_without_her[i] - t_samples[i]) / (T))/2
                pass
            pass
        transitions['r'] = reward
        transitions = {k: transitions[k].reshape(batch_size, *transitions[k].shape[1:])
                       for k in transitions.keys()}
        assert (transitions['u'].shape[0] == batch_size_in_transitions)

        return transitions


    return _sample_her_transitions_with_ep_future if ep else _sample_her_transitions
