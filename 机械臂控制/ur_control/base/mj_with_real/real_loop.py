import threading
import time

import numpy as np
import rtde_control
import base.MJ_IK.robotiq.robotiq_gripper as rg
import time
import globvar as gv


# ip = "192.168.1.102"
# rtde_c = rtde_control.RTDEControlInterface(ip)
# print("创建夹爪对象")
# gripper = rg.RobotiqGripper()
# print('连接夹爪...')
# gripper.connect(ip, 63352)
# print('激活夹爪...')
# gripper.activate()
# rtde_c.moveJ(gv.initial_joint_q, 1, 1)

def log_info(gripper):
    print(f"Pos: {str(gripper.get_current_position()): >3}  "
          f"Open: {gripper.is_open(): <2}  "
          f"Closed: {gripper.is_closed(): <2}  ")


def riq85to255(num):
    return num * (255 / 0.445)


def servo(rtde_c, gripper: rg.RobotiqGripper):
    rtde_c.moveJ(gv.initial_joint_q, 1, 1)
    while 1:
        if gv.flag_start_new_real_grasp:
            gv.flag_start_new_real_grasp = False
            rtde_c.moveJ(gv.initial_joint_q, 1, 1)
            l = len(gv.data_joints)
            data_joints = np.array(gv.data_joints).copy()

            for i in range(l):
                joint_q = data_joints[i][:-2]
                grip2 = data_joints[i][-2:]
                start = time.time()
                rtde_c.servoJ(joint_q, gv.velocity, gv.acceleration, gv.dt, gv.lookahead_time, gv.gain)
                gripper.move(255 - int(grip2[0] * (255 / 0.0445)), 255, 255)
                end = time.time()
                duration = end - start
                if duration < gv.dt:
                    time.sleep(gv.dt - duration)
            print("finish")
            rtde_c.servoStop()
        else:
            t = time.time()
            time.sleep(0.01)
        if gv.Esc:
            break


def test_servo():
    l = len(gv.data_joints)
    data_joints = np.array(gv.data_joints).copy()
    if len(data_joints) == 0:
        data_joints = gv.last_data_joints_for_real
    else:
        gv.last_data_joints_for_real = data_joints.copy()
    gv.data_joints = []
    gv.data_mocap = []
    gv.rtde_c.moveJ(data_joints[0][:-2], 1, 1)
    for i in range(l):
        joint_q = data_joints[i][:-2]
        grip2 = data_joints[i][-2:]
        start = time.time()
        gv.rtde_c.servoJ(joint_q, gv.velocity, gv.acceleration, gv.dt, gv.lookahead_time, gv.gain)
        gv.gripper.move(255 - int(grip2[0] * (255 / 0.0445)), 255, 255)
        end = time.time()
        duration = end - start
        if duration < gv.dt:
            time.sleep(gv.dt - duration)


def test_servo_1():
    while 1:
        if gv.flag_start_new_real_grasp:
            gv.flag_start_new_real_grasp = False
            print('Start Real Control')
            time.sleep(5)
            print('Finish Real Control')
        else:
            ti = time.sleep(0.01)
        if gv.Esc:
            print("t1 stoped...")
            break


if __name__ == '__main__':
    # time.sleep(5)
    # real_loop()
    # test()
    servo()
