import rtde_control
import time

rtde_c = rtde_control.RTDEControlInterface("192.168.1.102")

task_frame = [0, 0, 0, 0, 0, 0]
selection_vector = [1, 1, 1, 0, 0, 0]
wrench_down = [0, 0, -20, 0, 0, 0]
wrench_up = [0, 0, 20, 0, 0, 0]
force_type = 2
limits = [2, 2, 1.5, 1, 1, 1]
dt = 1.0 / 500  # 2ms
joint_q = [0, -1.57, 1.57, -1.57, -1.57, 0]

# Move to initial joint position with a regular moveJ
rtde_c.moveJ(joint_q)

# Execute 500Hz control loop for 4 seconds, each cycle is 2ms
for i in range(1000):
    start = time.time()
    # First move the robot down for 2 seconds, then up for 2 seconds
    if i > 500:
        rtde_c.forceMode(task_frame, selection_vector, wrench_up, force_type, limits)
    else:
        rtde_c.forceMode(task_frame, selection_vector, wrench_down, force_type, limits)
    end = time.time()
    duration = end - start
    if duration < dt:
        time.sleep(dt - duration)
rtde_c.forceMode(task_frame, selection_vector, [0, 0, 0, 0, 0, 0], force_type, limits)
