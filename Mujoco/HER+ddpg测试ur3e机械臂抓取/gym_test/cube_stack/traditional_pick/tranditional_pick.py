import time

import numpy as np
from utils import *


import globvar as g

np.set_printoptions(suppress=True)
reset(g.sim)
set_mocap(g.sim, g.viewer, g.gripper_target, g.gripper_rotation)
g.ges.set_xpos(g.sim.data.get_mocap_pos("robot0:mocap"))
g.ges.set_quat(g.sim.data.get_mocap_quat("robot0:mocap"))


def mainloop():
    while 1:
        set_mocap(g.sim, g.viewer, g.ges.xpos, g.ges.quat)
        set_ctrl(g.sim, g.viewer, g.ges.grip)
        joints_tmp, _ = gym_robotics.envs.utils.robot_get_obs(g.sim)
        g.grip = joints_tmp[-2:].copy()
        g.joints = joints_tmp[:-2]

        g.viewer.render()


def move(target):
    g.ges.set_xpos(target)
    set_mocap(g.sim, g.viewer, g.ges.xpos, g.ges.quat)
    g.viewer.render()


def close():
    g.ges.set_grip(np.array([0, 0]))
    set_ctrl(g.sim, g.viewer, g.ges.grip)
    g.viewer.render()

def open():
    g.ges.set_grip(np.array([0.05, 0.05]))
    set_ctrl(g.sim, g.viewer, g.ges.grip)
    g.viewer.render()

if __name__ == '__main__':

    for i in range(100):
        move(np.array([0.3,-0.0, 1.2]))
    for i in range(100):
        open()
    for i in range(100):
        move(np.array([0.3, -0.2, 1.1]))
    while 1:
        g.viewer.render()