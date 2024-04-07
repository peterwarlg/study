import numpy as np


class RolloutWorker:
    def __init__(self, venv, policy, params, evaluate=False):
        """
        Generate episodes from vectorized gym environment.
        @param venv: vectorized (parallel) environments
        @param policy: actions are determined according to this policy
        @param params: dict containing all necessary parameters:
        dims, T (episode length), num_workers, clip_obs, noise_eps, random_eps
        @param evaluate: (bool) sets noise to zero if evaluating
        平行环境下产生episode
        @参数：venv:平行环境
        @参数：policy：
        @参数：params：参数列表
        @参数：evaluate：判断是否为评估环境，是的话将噪声设置为 0
        """
        self.venv = venv
        self.policy = policy
        self.dims = params['dims']
        self.T = params['T']
        self.rollout_batch_size = params['num_workers']
        self.clip_obs = params['clip_obs']
        self.evaluate = evaluate

        self.noise_eps = params['noise_eps'] if not evaluate else 0
        self.random_eps = params['random_eps'] if not evaluate else 0

        self.info_keys = [key.replace('info_', '') for key in params['dims'].keys() if key.startswith('info_')]

        self.reset_all_rollouts()
        self.counter = 0

    def reset_all_rollouts(self):
        """
        Reset all environments and set initial observations.
        """
        self.obs_dict = self.venv.reset()
        self.initial_o = self.obs_dict['observation']
        self.initial_ag = self.obs_dict['achieved_goal']
        self.g = self.obs_dict['desired_goal'].astype(np.float32)

    def generate_rollouts(self):
        """
        Generating rollouts i.e. batch of episodes from all parallel environments.
        @return: episode batch
        """
        # 重置所有环境
        self.reset_all_rollouts()

        # 计算observation compute observations
        o = np.empty((self.rollout_batch_size, self.dims['o']), np.float32)  # observations
        ag = np.empty((self.rollout_batch_size, self.dims['g']), np.float32)  # achieved goals
        o[:] = self.initial_o
        ag[:] = self.initial_ag

        # 产生 episodes / generate episodes
        obs, achieved_goals, acts, goals, successes = [], [], [], [], []
        info_values = np.empty((self.T - 1, self.rollout_batch_size, 1), np.float32)
        for t in range(self.T):
            actions = self.policy.act(o, self.g, noise_eps=self.noise_eps, random_eps=self.random_eps)
            # compute new states and observations
            actions = actions.cpu().detach().numpy()
            obs_dict_new, _, done, info = self.venv.step(actions)
            o_new = obs_dict_new['observation']
            ag_new = obs_dict_new['achieved_goal']
            # 单次step的success， shape = (num_worker, )
            success = np.array([i['is_success'] for i in info])

            # assume all environments are done at approximately same number of steps, terminate rollouts
            if any(done):
                break

            for i, info_dict in enumerate(info):
                info_values[t, i] = info[i]['is_success']

            obs.append(o.copy())
            achieved_goals.append(ag.copy())
            successes.append(success.copy())
            acts.append(actions.copy())
            goals.append(self.g.copy())
            o[...] = o_new
            ag[...] = ag_new

        # success_rate 列表的最后一行就是最终的数据
        self.success_rate = np.mean(np.array(successes)[-1, :])

        obs.append(o.copy())
        achieved_goals.append(ag.copy())

        episode = dict(o=obs,
                       u=acts,
                       g=goals,
                       ag=achieved_goals)

        episode['info_is_success'] = info_values

        episode_batch = {}
        for key in episode.keys():
            val = np.array(episode[key]).copy()
            # convert an episode to have batch dimension in the first dimension
            episode_batch[key] = val.swapaxes(0, 1)

        episode_batch['o'] = np.clip(episode_batch['o'], -self.clip_obs, self.clip_obs)
        return episode_batch
