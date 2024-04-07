
from utils import *


# xml_file_path = '/home/wangzitu/ur_control/base/MJ_IK/models_2/pick_and_place.xml'
xml_file_path = '/home/wangzitu/MyGymEnv/robotics_ur/robotics_ur/envs/ur3e_grip_3/models/pick_and_place.xml'
xml_file_path = '/home/wangzitu/miniconda3/envs/ur/lib/python3.7/site-packages/gym_robotics/envs/ur3e_grip_4/models/pick_and_place.xml'
model = mujoco_py.load_model_from_path(xml_file_path)
sim = mujoco_py.MjSim(model, nsubsteps=1)
viewer = mujoco_py.MjViewer(sim)
ges = mocapData()


joints = np.zeros((6,))
grip = np.zeros((2,))
ctrl_mode = np.zeros((1))

gripper_target = [0.3, 0.1, 1.1]
gripper_rotation = [0.7741671, 0, 0.7741671, 0]

unit = 0.005
done = True