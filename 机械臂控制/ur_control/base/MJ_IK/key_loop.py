from pynput import keyboard
from pynput.keyboard import Key
import numpy as np

from utils import reset
import globvar as g


def on_press(key):
    # global ges, unit,sim,joints,grip,ctrl_mode
    if key == Key.home:
        g.ges.set_xpos([g.ges.xpos[0], g.ges.xpos[1] + g.unit, g.ges.xpos[2]])
    elif key == Key.end:
        g.ges.set_xpos([g.ges.xpos[0], g.ges.xpos[1] - g.unit, g.ges.xpos[2]])
    elif key == Key.delete:
        g.ges.set_xpos([g.ges.xpos[0] - g.unit, g.ges.xpos[1], g.ges.xpos[2]])
    elif key == Key.page_down:
        g.ges.set_xpos([g.ges.xpos[0] + g.unit, g.ges.xpos[1], g.ges.xpos[2]])
    elif key == Key.up:
        g.ges.set_xpos([g.ges.xpos[0], g.ges.xpos[1], g.ges.xpos[2] + g.unit])
    elif key == Key.down:
        g.ges.set_xpos([g.ges.xpos[0], g.ges.xpos[1], g.ges.xpos[2] - g.unit])
    elif key == Key.insert:
        g.ges.set_grip(np.array([g.ges.grip[0] + g.unit, g.ges.grip[1] + g.unit]))
        g.ges.grip = np.clip(g.ges.grip, np.array([0, 0]), np.array([0.044715321758878, 0.044715321758878]))
    elif key == Key.page_up:
        g.ges.set_grip(np.array([g.ges.grip[0] - g.unit, g.ges.grip[1] - g.unit]))
        g.ges.grip = np.clip(g.ges.grip, np.array([0, 0]), np.array([0.044715321758878, 0.044715321758878]))

    elif key == Key.f1:
        g.ges.set_euler([g.ges.euler[0] + g.unit, g.ges.euler[1], g.ges.euler[2]])
    elif key == Key.f2:
        g.ges.set_euler([g.ges.euler[0] - g.unit, g.ges.euler[1], g.ges.euler[2]])
    elif key == Key.f3:
        g.ges.set_euler([g.ges.euler[0], g.ges.euler[1] + g.unit, g.ges.euler[2]])
    elif key == Key.f4:
        g.ges.set_euler([g.ges.euler[0], g.ges.euler[1] - g.unit, g.ges.euler[2]])
    elif key == Key.f5:
        g.ges.set_euler([g.ges.euler[0], g.ges.euler[1], g.ges.euler[2] + g.unit])
    elif key == Key.f6:
        g.ges.set_euler([g.ges.euler[0], g.ges.euler[1], g.ges.euler[2] - g.unit])
    elif key == Key.f9:
        g.ges.set_xpos(g.gripper_target)
        g.ges.set_quat(g.gripper_rotation)
        reset(g.sim)
    elif key == Key.f10:
        print(g.joints, g.grip)
    elif key == Key.f11:
        print("Real Ctrl")
        g.ctrl_mode[0] = 1
    elif key == Key.f12:
        print("MJ Ctrl")
        g.ctrl_mode[0] = 0

    # try:
    #     print('alphanumeric key {0} pressed\r'.format(
    #         key.char), end="\t")
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


def on_release(key):
    if key == keyboard.Key.esc:
        g.done = False
        # Stop listener
        return False
