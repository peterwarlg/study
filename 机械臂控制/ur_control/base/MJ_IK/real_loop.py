import time

import rtde_control
import base.MJ_IK.robotiq.robotiq_gripper as rg
import globvar as g
import time

ip = "192.168.1.102"


def log_info(gripper):
    print(f"Pos: {str(gripper.get_current_position()): >3}  "
          f"Open: {gripper.is_open(): <2}  "
          f"Closed: {gripper.is_closed(): <2}  ")


def riq85to255(num):
    return num * (255 / 0.445)


print("创建夹爪对象")
gripper = rg.RobotiqGripper()
print('连接夹爪...')
gripper.connect(ip, 63352)
print('激活夹爪...')
gripper.activate()


# print('连接机器人...')
# rtde_c = rtde_control.RTDEControlInterface('192.168.1.102')


def real_loop():
    while g.done:
        if g.ctrl_mode[0] == 1:
            rtde_c.moveJ(g.joints, 1, 1)
            gripper.move_and_wait_for_pos(riq85to255(g.grip[0]), 255, 255)

