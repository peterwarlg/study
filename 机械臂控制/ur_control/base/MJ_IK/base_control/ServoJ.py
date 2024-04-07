import rtde_control
import time

rtde_c = rtde_control.RTDEControlInterface("192.168.1.102")

# Parameters
velocity = 0.5
acceleration = 0.5
dt = 1.0/500  # 2ms
lookahead_time = 0.1
gain = 2000
joint_q = [0, -1.57, 1.57, -1.57, -1.57, 0]

# Move to initial joint position with a regular moveJ
rtde_c.moveJ(joint_q)

# Execute 500Hz control loop for 2 seconds, each cycle is 2ms
for i in range(1000):
    start = time.time()
    rtde_c.servoJ(joint_q, velocity, acceleration, dt, lookahead_time, gain)
    joint_q[0] += 0.001
    # joint_q[1] += 0.001
    end = time.time()
    duration = end - start
    if duration < dt:
        time.sleep(dt - duration)

rtde_c.servoStop()
rtde_c.stopScript()