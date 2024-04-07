#!/usr/bin/env python


import sys
import math


class ur3e():
    def __init__(self):
        self.robot_pose = [[0.0] * 7,
                           [0.0] * 6,
                           []]
        # ur action client

    def sendGoalAndWait(self):
        print("sendGoalAndWait")
        return "sendGoalAndWait"

    # input 3 position values of end-effect
    def set_pose_with_posi(self, *args):

        for i in range(7):
            self.robot_pose[0][i] += 0.1
            self.robot_pose[0][i]
        print("set_pose_with_posi:", args)
        return self.robot_pose

    # input six joint values
    def set_pose_with_joint(self, *args):

        for i in range(6):
            self.robot_pose[1][i] += 0.1
            self.robot_pose[1][i]
        print("set_pose_with_joint", args)
        return self.robot_pose

    # default input 0 or 1 with gripper open or close   例:class.gripper_set_pose(0)
    # or a value between 0-? and control='dis' to specific the distance 例: class.gripper_set_pose(0.3,control='dis')
    def gripper_set_pose(self, *args, control='cANDo'):
        print("gripper_set_pose", args)
        return self.robot_pose

    def get_robot_pose(self):
        print("get_robot_pose")

    # initial pose for 2 types
    # 1.a horizon pose
    # 2.grasp pose ,which the end pose is approx [0.4,0.4,0.9]
    def initial_pose_with_joint(self, pose=None):
        print()
        return self.robot_pose



if __name__ == '__main__':
    pass
