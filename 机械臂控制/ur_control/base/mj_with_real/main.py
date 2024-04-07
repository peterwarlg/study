import threading

from mujoco_loop import mujoco_loop
from pynput import keyboard
from key_loop import on_press, on_release
from real_loop import servo, test_servo, test_servo_1
import globvar as gv


import numpy as np
import rtde_control
import base.MJ_IK.robotiq.robotiq_gripper as rg
import time
import globvar as gv

ip = "192.168.1.102"
rtde_c = rtde_control.RTDEControlInterface(ip)
print("创建夹爪对象")
gripper = rg.RobotiqGripper()
print('连接夹爪...')
gripper.connect(ip, 63352)
print('激活夹爪...')
gripper.activate()
rtde_c.moveJ(gv.initial_joint_q, 1, 1)


if __name__ == '__main__':
    # keyloop
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

    t1 = threading.Thread(target=servo,args=(rtde_c, gripper))
    t1.start()

    mujoco_loop()

    t1.join()



