#!/usr/bin/env python

'''
wztuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
edition in 2020 10 09
a class of cubes with
    1.set cube
    2.reset cube
    3.get cube's state
uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
'''

import rospy
import p_robot_learning_demo.msg as msg
import actionlib
from gazebo_msgs.srv import *
from enum import Enum


# initial cube position
class Cube(Enum):
    big_cup = [0.2, 0.6, 0.8, 0, 0, 0]

    MuKuai_red = [0.4, 0.3, 0.8, 0, 0, 0]
    MuKuai_green = [0.4, 0.4, 0.8, 0, 0, 0]
    MuKuai_blue = [0.4, 0.5, 0.8, 0, 0, 0]
    # MuKuai_yellow = [0.4, 0.6, 0.82,0,0,0]
    xiaoyuanzhu_red = [0.5, 0.3, 0.8, 0.5, 0, 0]
    xiaoyuanzhu_green = [0.5, 0.4, 0.8, 0.5, 0, 0]
    xiaoyuanzhu_blue = [0.5, 0.5, 0.8, 0.5, 0, 0]
    # xiaoyuanzhu_yellow = [0.5, 0.6, 0.82,0,0,0]


class Obj():
    def __init__(self):
        self.cube_state = []
    # cubeANDyuanzhu = Cube()
    # set cube with x, y, z and cube name {r, g, b, y}
    def set_cube(self, *args, name='cube_name'):
        try:
            set_state_service = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            objstate = SetModelStateRequest()  # Create an object of type SetModelStateRequest

            # set red cube pose
            objstate.model_state.model_name = name
            objstate.model_state.pose.position.x = args[0]
            objstate.model_state.pose.position.y = args[1]
            objstate.model_state.pose.position.z = args[2]
            objstate.model_state.pose.orientation.w = 1
            objstate.model_state.pose.orientation.x = args[3]
            objstate.model_state.pose.orientation.y = args[4]
            objstate.model_state.pose.orientation.z = args[5]
            objstate.model_state.twist.linear.x = 0.0
            objstate.model_state.twist.linear.y = 0.0
            objstate.model_state.twist.linear.z = 0.0
            objstate.model_state.twist.angular.x = 0.0
            objstate.model_state.twist.angular.y = 0.0
            objstate.model_state.twist.angular.z = 0.0
            objstate.model_state.reference_frame = "world"

            result = set_state_service(objstate)

            if result:
                pass
            else:
                pass
        except rospy.ServiceException:
            print("Service call failed")

    def cube_reset(self):
        for cube in Cube:
            self.set_cube(cube.value[0], cube.value[1], cube.value[2],
                          cube.value[3], cube.value[4], cube.value[5], name=cube.name)
        # self.set_cube(Cube.MuKuai_red.value[0], Cube.MuKuai_red.value[1],
        #               Cube.MuKuai_red.value[2], name=Cube.MuKuai_red.name)
        # self.set_cube(Cube.MuKuai_green.value[0], Cube.MuKuai_green.value[1],
        #               Cube.MuKuai_green.value[2], name=Cube.MuKuai_green.name)
        # self.set_cube(Cube.MuKuai_blue.value[0], Cube.MuKuai_blue.value[1],
        #               Cube.MuKuai_blue.value[2], name=Cube.MuKuai_blue.name)
        # self.set_cube(Cube.MuKuai_yellow.value[0], Cube.MuKuai_yellow.value[1],
        #               Cube.MuKuai_yellow.value[2], name=Cube.MuKuai_yellow.name)

    def get_cube_state(self):
        get_state_service = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        model = GetModelStateRequest()
        model_name_cube = ['big_cup', 'MuKuai_red', 'MuKuai_green', 'MuKuai_blue',
                           'xiaoyuanzhu_red', 'xiaoyuanzhu_green', 'xiaoyuanzhu_blue']
        for i in range(len(model_name_cube)):
            model.model_name = model_name_cube[i]
            objstate = get_state_service(model)
            self.cube_state.append([objstate.pose.position.x, objstate.pose.position.y, objstate.pose.position.z])
        return self.cube_state


if __name__ == '__main__':
    obj = Obj()
    state = obj.get_cube_state();
    print(state)
    obj.cube_reset()
    obj.set_cube(0.2, 0.6, 1, 0, 0, 0, name='big_cup')
