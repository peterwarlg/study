import numpy as np

import globvar as gv


def renew_cube_xpos():
    print('输入cube_xpos: x y')
    cube = input().split(" ")
    gv.cube_xpos = np.array(list(map(float, cube)))

def renew_goal_xpos():
    print('输入goal_xpos: x y z')
    cube = input().split(" ")
    gv.goal_xpos = np.array(list(map(float, cube)))

def renew_cube_or_goal():
    print('Input Command')
    command = input().split(" ")
    try:
        command = np.array(list(map(float, command)))
    except ValueError as e:
        print("WRONG Input format")
        return
    if len(command) == 2:
        gv.cube_xpos = command.copy()
    elif len(command) == 3:
        gv.goal_xpos = command.copy()
        gv.goal_xpos[2] = max(gv.goal_xpos[2], 1.1)
    else:
        print("WRONG Input format")



