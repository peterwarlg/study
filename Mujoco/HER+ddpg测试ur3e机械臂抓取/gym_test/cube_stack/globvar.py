import threading
import numpy as np

data_joints = []
last_data_joints_for_real = []
data_mocap = []
cube_xpos = np.array([0.3, 0.0])
goal_xpos = np.array([0.3, 0.0, 1.25])

"""
real_loop
"""

# Parameters
velocity = 0.01
acceleration = 0.5
dtt = 50
dt = 1.0/dtt  # 2ms
lookahead_time = 0.1
gain = 100
initial_joint_q = [0, -1.57, 1.57, -1.57, -1.57, 0]

l_flag_start_new_grasp = threading.Lock()
l_flag_start_new_real_grasp = threading.Lock()

flag_start_new_grasp = True
flag_start_new_real_grasp = False
Esc = False

