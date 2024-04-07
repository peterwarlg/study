from pynput import keyboard
from pynput.keyboard import Key
import numpy as np
from kinect_loop import renew_cube_xpos, renew_goal_xpos,renew_cube_or_goal
import globvar as gv
from real_loop import test_servo,test_servo_1

def on_press(key):
    if key == Key.f1:
        gv.dtt -= 10
        gv.dtt = max(gv.dtt, 1)
        gv.dt = 1.0 / gv.dtt
    elif  key == Key.f2:
        gv.dtt += 10
        gv.dtt = min(gv.dtt, 200)
        gv.dt = 1.0 / gv.dtt
    elif key == Key.f3:
        print(gv.dtt, gv.dt)
    elif key == Key.f5:
        renew_cube_xpos()
    elif key == Key.f6:
        renew_goal_xpos()
    elif key == Key.f7:
        renew_cube_or_goal()

    elif key == Key.f9:
        gv.flag_start_new_grasp = True
    elif key == Key.f10:
        gv.flag_start_new_real_grasp = True
        # test_servo()
        pass
    elif key == Key.f11:
        pass
        # test_servo()
    elif key == Key.f12:
        print(len(gv.data_joints))
    elif key == Key.esc:
        gv.Esc = True


    # try:
    #     print('alphanumeric key {0} pressed\r'.format(
    #         key.char), end="\t")
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))


def on_release(key):
    if key == keyboard.Key.esc:
        gv.ESC = True
        # Stop listener
        return False
