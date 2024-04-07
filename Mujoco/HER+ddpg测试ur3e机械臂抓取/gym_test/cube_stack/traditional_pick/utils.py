import threading
import gym
import gym_robotics
from gym_robotics.envs import utils
import mujoco_py
import numpy as np


def set_mocap(sim: mujoco_py.MjSim, viewer: mujoco_py.MjViewer, pos, quat):
    sim.data.set_mocap_pos("robot0:mocap", pos)
    sim.data.set_mocap_quat("robot0:mocap", quat)
    for _ in range(10):
        sim.step()
        viewer.render()

def set_ctrl(sim: mujoco_py.MjSim, viewer: mujoco_py.MjViewer, grip):
    if sim.data.ctrl is not None:
        for i in range(grip.shape[0]):
            sim.data.ctrl[i] = grip[i]

    for _ in range(10):
        sim.step()
        viewer.render()


class mocapData():
    def __init__(self):
        self.xpos = np.zeros((3,))
        self.quat = np.zeros((4,))
        self.euler = np.zeros((3,))
        self.grip = np.zeros((2,))

    def set_xpos(self, xpos):
        self.xpos = xpos.copy()

    def set_quat(self, quat):
        q = (quat.copy())
        self.quat = q
        self.euler = gym_robotics.envs.rotations.quat2euler(q)

    def set_euler(self, euler):
        e = euler.copy()
        self.euler = e
        self.quat = gym_robotics.envs.rotations.euler2quat(e)

    def set_grip(self, g):
         self.grip = g.copy()


def reset(sim: mujoco_py.MjSim):
    initial_qpos = {
        'robot0:shoulder_pan_joint': 0.,
        'robot0:shoulder_lift_joint': -1.57,
        'robot0:elbow_joint': 1.57,
        'robot0:wrist_1_joint': -1.57,
        'robot0:wrist_2_joint': -1.57,
        'robot0:wrist_3_joint': 0.0,
        'object0:joint': [0.3, 0.0, 1.025, 1, 0, 0, 0]
    }
    for name, value in initial_qpos.items():
        sim.data.set_joint_qpos(name, value)
    utils.reset_mocap_welds(sim)
    sim.forward()


