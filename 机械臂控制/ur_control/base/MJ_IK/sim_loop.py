import time
import globvar as g
import numpy as np


def sim_loop():
    # time.sleep(4)
    for d, j in zip(g.mocap_data, g.joints_data):
        g.ges.set_xpos(np.array([d[0], d[1], d[2]]))
        g.ges.set_grip(np.array([j[-2], j[-1]]))
        # time.sleep(0.01)



initial_qpos_name = [
'robot0:shoulder_pan_joint',
        'robot0:shoulder_lift_joint',
        'robot0:elbow_joint',
        'robot0:wrist_1_joint',
        'robot0:wrist_2_joint',
        'robot0:wrist_3_joint',
]

for i in range(10):
    for j in g.joints_data:
        j = j[:-2]
        for i in range(len(j)):
            g.sim.data.set_joint_qpos(initial_qpos_name[i], j[i])

        g.sim.forward()
        g.viewer.render()
