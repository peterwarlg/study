import gym_robotics

from utils import set_mocap, set_ctrl
import globvar as g


def mainloop():
    while 1:
        set_mocap(g.sim, g.viewer, g.ges.xpos, g.ges.quat)
        set_ctrl(g.sim, g.viewer, g.ges.grip)
        joints_tmp, _ = gym_robotics.envs.utils.robot_get_obs(g.sim)
        g.grip = joints_tmp[-2:].copy()
        g.joints = joints_tmp[:-2]

        g.viewer.render()