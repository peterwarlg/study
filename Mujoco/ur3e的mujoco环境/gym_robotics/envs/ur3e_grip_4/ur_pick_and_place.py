import gym
from gym import utils
from gym_robotics.envs.ur3e_grip_4 import ur_env
import gym_robotics
MODEL_XML_PATH = '/home/wangzitu/miniconda3/envs/ur/lib/python3.7/site-packages/gym_robotics/envs/ur3e_grip_4/models/pick_and_place.xml'

# [0, -1.57, 1.57, -1.57, -1.57, 0.0, 0.3]

class UrPickAndPlaceEnv4(ur_env.UrEnv, utils.EzPickle):
    def __init__(self, reward_type="sparse"):
        initial_qpos = {
            'robot0:shoulder_pan_joint': 0.,
            'robot0:shoulder_lift_joint': -1.57,
            'robot0:elbow_joint':  1.57,
            'robot0:wrist_1_joint': -1.57,
            'robot0:wrist_2_joint': -1.57,
            'robot0:wrist_3_joint': 0.0,

            'object0:joint': [0.3, 0.0, 1.025, 1, 0, 0, 0]
        }
        ur_env.UrEnv.__init__(
            self,
            MODEL_XML_PATH,
            has_object=True,
            block_gripper=False,
            n_substeps=1,
            gripper_extra_height=0.0,
            target_in_the_air=True,
            target_offset=0.0,
            obj_range=0.1,
            target_range=0.1,
            distance_threshold=0.05,
            initial_qpos=initial_qpos,
            reward_type=reward_type,
        )
        utils.EzPickle.__init__(self, reward_type=reward_type)

    def get_robot_qpos(self):
        robot_qpos, robot_qvel = gym_robotics.envs.utils.robot_get_obs(self.sim)
        return robot_qpos, robot_qvel

    def get_grip_xpos(self):
        grip_xpos = self.sim.data.get_site_xpos("robot0:grip")
        return grip_xpos.copy()


