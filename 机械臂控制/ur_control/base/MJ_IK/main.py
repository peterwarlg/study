from utils import *
from pynput import keyboard
from key_loop import on_press, on_release
from real_loop import real_loop
from main_loop import mainloop
from sim_loop import sim_loop

import globvar as g
np.set_printoptions(suppress=True)
reset(g.sim)
set_mocap(g.sim, g.viewer, g.gripper_target, g.gripper_rotation)
g.ges.set_xpos(g.sim.data.get_mocap_pos("robot0:mocap"))
g.ges.set_quat(g.sim.data.get_mocap_quat("robot0:mocap"))

# mocap比robot0:grip在z向高了0.05


if __name__ == '__main__':
    # keyloop
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    # t = threading.Thread(target=real_loop)
    # t.start()

    t1 = threading.Thread(target=sim_loop())
    t1.start()

    mainloop()
