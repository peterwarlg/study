"""
Available "joint" names = (
'robot0:slide0', 'robot0:slide1', 'robot0:slide2',
'robot0:shoulder_pan_joint', 'robot0:shoulder_lift_joint',
'robot0:elbow_joint', 'robot0:wrist_1_joint',
'robot0:wrist_2_joint', 'robot0:wrist_3_joint',
'robot0:base_to_lik', 'robot0:base_to_rik',
'cube_0:joint').
"""
import numpy as np

from gym_robotics.envs import rotations, utils
# from gym.envs.robotics import rotations, utils
from gym_robotics.envs.ur3e_grip_4 import robot_env


def goal_distance(goal_a: np.ndarray, goal_b: np.ndarray):
    assert goal_a.shape == goal_b.shape
    return np.linalg.norm(goal_a - goal_b, axis=-1)


class UrEnv(robot_env.RobotEnv):
    # 所有UR 机械臂的超类
    def __init__(
            self,
            model_path,
            n_substeps,
            gripper_extra_height,
            block_gripper,
            has_object,
            target_in_the_air,
            target_offset,
            obj_range,
            target_range,
            distance_threshold,
            initial_qpos,
            reward_type,
    ):
        """Initializes a new Fetch environment.
        Args:
            model_path (string): XMl文件的路径   path to the environments XML file
            n_substeps (int): sim中每次调用step时substep的数量   number of substeps the simulation runs on every call to step
            gripper_extra_height (float): additional height above the table when positioning the gripper
            block_gripper (boolean): whether or not the gripper is blocked (i.e. not movable) or not
            has_object (boolean): whether or not the environment has an object
            target_in_the_air (boolean): whether or not the target should be in the air above the table or on the table surface
            target_offset (float or array with 3 elements): 目标的偏移   offset of the target
            obj_range (float): cube的初始位置范围  range of a uniform distribution for sampling initial object positions
            target_range (float): 目标的采样范围   range of a uniform distribution for sampling a target
            distance_threshold (float): 判断是否成功的阈值   the threshold after which a goal is considered achieved
            initial_qpos (dict): 初始角度,字典 {'name':qpos}   a dictionary of joint names and values that define the initial configuration
            reward_type ('sparse' or 'dense'): the reward type, i.e. sparse or dense
        """
        self.gripper_extra_height = gripper_extra_height
        self.block_gripper = block_gripper
        self.has_object = has_object
        self.target_in_the_air = target_in_the_air
        self.target_offset = target_offset
        self.obj_range = obj_range
        self.target_range = target_range
        self.distance_threshold = distance_threshold
        self.reward_type = reward_type

        super(UrEnv, self).__init__(
            model_path=model_path,
            n_substeps=n_substeps,
            n_actions=4,
            initial_qpos=initial_qpos,
        )

    # GoalEnv methods
    # ----------------------------

    def compute_reward(self, achieved_goal: np.ndarray, goal: np.ndarray, info):
        # Compute distance between goal and the achieved goal.
        # 计算goal和achieved_goal的距离
        d = goal_distance(achieved_goal, goal)
        if self.reward_type == "sparse":
            return -(d > self.distance_threshold).astype(np.float32)
        else:
            return -d

    # RobotEnv methods
    # ----------------------------

    def _step_callback(self):
        if self.block_gripper:
            self.sim.data.set_joint_qpos("robot0:l_gripper_finger_joint", 0.0)
            self.sim.data.set_joint_qpos("robot0:r_gripper_finger_joint", 0.0)
            self.sim.forward()

    def _set_action(self, action):
        assert action.shape == (4,)
        action = (
            action.copy()
        )  # ensure that we don't change the action outside of this scope
        pos_ctrl, gripper_ctrl = action[:3], action[3]

        pos_ctrl *= 0.05  # limit maximum change in position
        rot_ctrl = [
            1.0,
            0.0,
            1.0,
            0.0,
        ]  # fixed rotation of the end effector, expressed as a quaternion
        gripper_ctrl = np.array([gripper_ctrl, gripper_ctrl])

        '''
        TOBE CONTINUE
        '''

        assert gripper_ctrl.shape == (2,)
        if self.block_gripper:
            gripper_ctrl = np.zeros_like(gripper_ctrl)
        action = np.concatenate([pos_ctrl, rot_ctrl, gripper_ctrl])

        # Apply action to simulation.
        utils.ctrl_set_action(self.sim, action)
        utils.mocap_set_action(self.sim, action)

    def _get_obs(self, obj_name="object0"):
        # positions
        # robot0:grip定义在 ee_link上,方向仍待确定
        # 标准初始状态下ee_link的坐标为[0.29809318 0.1310655  1.31215644]
        grip_pos = self.sim.data.get_site_xpos("robot0:grip")
        dt = self.sim.nsubsteps * self.sim.model.opt.timestep
        grip_velp = self.sim.data.get_site_xvelp("robot0:grip") * dt

        # 返回所有以"robot"开头的角度的qpos
        robot_qpos, robot_qvel = utils.robot_get_obs(self.sim)
        if self.has_object:
            object_pos = self.sim.data.get_site_xpos(obj_name)
            # rotations
            object_rot = rotations.mat2euler(self.sim.data.get_site_xmat(obj_name))
            # velocities
            object_velp = self.sim.data.get_site_xvelp(obj_name) * dt
            object_velr = self.sim.data.get_site_xvelr(obj_name) * dt
            # gripper state
            object_rel_pos = object_pos - grip_pos
            object_velp -= grip_velp
        else:
            object_pos = (
                object_rot
            ) = object_velp = object_velr = object_rel_pos = np.zeros(0)
        gripper_state = robot_qpos[-2:]
        gripper_vel = (
                robot_qvel[-2:] * dt
        )  # change to a scalar if the gripper is made symmetric

        if not self.has_object:
            achieved_goal = grip_pos.copy()
        else:
            achieved_goal = np.squeeze(object_pos.copy())
        obs = np.concatenate(
            [
                grip_pos,
                object_pos.ravel(),
                object_rel_pos.ravel(),
                gripper_state,
                object_rot.ravel(),
                object_velp.ravel(),
                object_velr.ravel(),
                grip_velp,
                gripper_vel,
            ]
        )

        return {
            "observation": obs.copy(),
            "achieved_goal": achieved_goal.copy(),
            "desired_goal": self.goal.copy(),
        }

    def _viewer_setup(self):
        body_id = self.sim.model.body_name2id("robot0:gripper_link")
        lookat = self.sim.data.body_xpos[body_id]
        for idx, value in enumerate(lookat):
            self.viewer.cam.lookat[idx] = value
        self.viewer.cam.distance = 2.5
        self.viewer.cam.azimuth = 132.0
        self.viewer.cam.elevation = -14.0

    def _render_callback(self):
        # Visualize target.
        # 将目标可视化:
        #   self.sim.data.site_xpos: 当前所有site的位置
        #   self.sim.model.site_pos: xml model中site相对于所在body的位置
        sites_offset = (self.sim.data.site_xpos - self.sim.model.site_pos).copy()
        site_id = self.sim.model.site_name2id("target0")
        self.sim.model.site_pos[site_id] = self.goal.copy()  # - sites_offset[0]
        self.sim.forward()

    def _reset_sim(self):
        self.sim.set_state(self.initial_state)
        # Randomize start position of object.
        # 初始化时随机cube的位置
        if self.has_object:
            object_xpos = self.initial_gripper_xpos[:2]
            while np.linalg.norm(object_xpos - self.initial_gripper_xpos[:2]) < 0.1:
                object_xpos = self.initial_gripper_xpos[:2] + self.np_random.uniform(
                    -self.obj_range, self.obj_range, size=2
                )
            object_qpos = self.sim.data.get_joint_qpos("object0:joint")
            assert object_qpos.shape == (7,)
            object_qpos[:2] = object_xpos
            self.sim.data.set_joint_qpos("object0:joint", object_qpos)

        self.sim.forward()
        return True

    def _reset_sim_custom(self, cube_xpos: np.ndarray = np.array([0.3, 0.0])) -> bool:
        """
        指定cube位置的初始化
        """
        assert len(cube_xpos) == 2, "指定的object的x, y坐标"
        self.sim.set_state(self.initial_state)
        object_xpos = cube_xpos.copy()
        object_qpos = self.sim.data.get_joint_qpos("object0:joint")
        assert object_qpos.shape == (7,)
        object_qpos[:2] = object_xpos
        self.sim.data.set_joint_qpos("object0:joint", object_qpos)

        self.sim.forward()
        return True

    def _sample_goal_ur(self):
        if self.has_object:
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(
                -self.target_range, self.target_range, size=3
            )
            goal += self.target_offset
            goal[2] = 1.025
            if self.target_in_the_air and self.np_random.uniform() < 0.5:
                goal[2] += self.np_random.uniform(0.1, 0.2)
        else:
            raise NotImplementedError
        return goal.copy()

    def _sample_goal(self):
        return self._sample_goal_ur()
        """
        采样goal
        initial_gripper_xpos是_env_setup()后手爪的位置:[0.29995379 0.1312044  1.15547724]
        self.height_offset是木块高度,也就是桌子高度(Fetch环境中,他的坐标系设置如此)
        """
        if self.has_object:
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(
                -self.target_range, self.target_range, size=3
            )
            goal += self.target_offset
            goal[2] = self.height_offset
            if self.target_in_the_air and self.np_random.uniform() < 0.5:
                goal[2] += self.np_random.uniform(0, 0.45)
        # pass
        else:
            goal = self.initial_gripper_xpos[:3] + self.np_random.uniform(
                -self.target_range, self.target_range, size=3
            )
        return goal.copy()

    def _is_success(self, achieved_goal, desired_goal):
        d = goal_distance(achieved_goal, desired_goal)
        return (d < self.distance_threshold).astype(np.float32)

    def _env_setup(self, initial_qpos):
        """
        环境重置, 机器人初始化qpos
        """
        for name, value in initial_qpos.items():
            self.sim.data.set_joint_qpos(name, value)
        utils.reset_mocap_welds(self.sim)
        self.sim.forward()
        """
        Move end effector into position.
        这里应该是,fetch初始化时机器人不在桌子上,需要先整体移动机器人到桌子旁边
        所以,用机械臂初始化要用末端位置减去 0.498...,并且加上手爪的提升高度(初始化时机械臂是水平的,可以直接加载fetch的xml文件来看)
        这里的gripper_target可以自己设定一个差不多的值即可,
        源码中的self.gripper_extra_height是手爪相较于桌面的高度
        关节角全为0时末端位置: [0.45638164 0.2133     1.06438925]
        关节角为[0, -1.57, 1.57, -1.57, -1.57, 0.0, 0.3]时:  [0.29809318 0.1310655  1.31215644]
        """
        gripper_target = np.array([-0.498, 0.005, -0.431 + self.gripper_extra_height]) \
                         + self.sim.data.get_site_xpos("robot0:grip")

        # 因为在UrPickAndPlaceEnv::__init__()中初始化时已经设定了关节角的角度:[0, -1.57, 1.57, -1.57, -1.57, 0.0, 0.3]
        # 所以此时直接用robot0:grip的位置作为mocap的位置即可,即机械臂不需要移动
        gripper_target = np.array(self.sim.data.get_site_xpos("robot0:grip"))
        gripper_target[0] -= 0  # 0.05
        gripper_target[1] -= 0.1310655
        gripper_rotation = np.array([1.0, 0.0, 1.0, 0.0])

        # 把mocap移动到设定的目标手爪中心位置
        self.sim.data.set_mocap_pos("robot0:mocap", gripper_target)
        self.sim.data.set_mocap_quat("robot0:mocap", gripper_rotation)

        # 原值为10
        for _ in range(10):
            self.sim.step()

        # 为之后采样goal做准备  Extract information for sampling goals.
        self.initial_gripper_xpos = self.sim.data.get_site_xpos("robot0:grip").copy()

        # offset: 当前物体到世界坐标系的高度偏移
        if self.has_object:
            self.height_offset = self.sim.data.get_site_xpos("object0")[2]

    def render(self, mode="human", width=500, height=500):
        return super(UrEnv, self).render(mode, width, height)
