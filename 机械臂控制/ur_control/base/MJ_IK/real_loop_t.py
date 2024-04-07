import time

import numpy as np
import rtde_control
import base.MJ_IK.robotiq.robotiq_gripper as rg
import time

ip = "192.168.1.102"

# print('连接机器人...')
rtde_c = rtde_control.RTDEControlInterface('192.168.1.102')


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

mocap_data = np.loadtxt('mocap_data.txt')
joints_data = np.loadtxt('joints_data.txt')

# joints_data = joints_data[::4]

rtde_c.moveJ(joints_data[0][:-2], 2, 1)


def real_loop():
    for j in joints_data:
        joints6 = j[:-2]
        joints6[0] += 1.57
        # print(joints6)
        grip2 = j[-2:]
        rtde_c.moveJ(joints6, 2, 0.1, True)
        print(grip2)
        gripper.move(255 - int(grip2[0] * (255 / 0.0445)), 255, 255)
        time.sleep(0.01)


def test():
    for i in range(255):
        gripper.move_and_wait_for_pos(i, 255, 255)

# Parameters
velocity = 0.01
acceleration = 0.5
dt = 1.0/5  # 2ms
lookahead_time = 0.1
gain = 100
joint_q = [0, -1.57, 1.57, -1.57, -1.57, 0]

joints_data = joints_data[::20]

def servo():
    l = len(joints_data)
    for i in range(l):
        joint_q = joints_data[i][:-2]
        grip2 = joints_data[i][-2:]
        start = time.time()
        rtde_c.servoJ(joint_q, velocity, acceleration, dt, lookahead_time, gain)
        gripper.move(255 - int(grip2[0] * (255 / 0.0445)), 255, 255)
        end = time.time()
        duration = end - start
        if duration < dt:
            time.sleep(dt - duration)

if __name__ == '__main__':
    # time.sleep(5)
    # real_loop()
    # test()
    servo()
