
from utils import *


# xml_file_path = '/home/wangzitu/ur_control/base/MJ_IK/models_2/pick_and_place.xml'
xml_file_path = '/home/wangzitu/MyGymEnv/robotics_ur/robotics_ur/envs/ur3e_grip_3/models/pick_and_place.xml'
model = mujoco_py.load_model_from_path(xml_file_path)
sim = mujoco_py.MjSim(model, nsubsteps=1)
viewer = mujoco_py.MjViewer(sim)
ges = mocapData()

mocap_data = np.loadtxt('mocap_data.txt')
joints_data = np.loadtxt('joints_data.txt')

joints = np.zeros((6,))
grip = np.zeros((2,))
ctrl_mode = np.zeros((1))

gripper_target = [0.3, 0.1, 1.1]
gripper_rotation = [0.7741671, 0, 0.7741671, 0]

unit = 0.005
done = True