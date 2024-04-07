#!/usr/bin/env python

'''
wztuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
re-edition in 2020 10 09
机器人控制的基本文件
a class of ur3e with
    1.end-effect position control (ignore orientation)
    2.joint control
    3.gripper control
    4.objects(cubes) setting
uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
'''
import rospy
import sys
import p_robot_learning_demo.msg as msg
import actionlib
from gazebo_msgs.srv import *
from Object import Obj
import math

''' 
所有机械臂运动后的返回值(result)改为  7（末端姿态）+6（六关节角度）+1（success）=
[
    [len=7],    7（末端姿态）
    [len=6],    6（六关节角度）
    [len=1]     1（success）
            ]列表
'''


class ur3e():
    def __init__(self):
        self.robot_pose = [[0.0] * 7,
                           [0.0] * 6,
                           []]
        self.env = Obj()
        rospy.init_node('p_robot_env')
        rospy.wait_for_service('/gazebo/set_model_state')
        rospy.wait_for_service('/gazebo/get_model_state')

        # ur action client
        self.client = actionlib.SimpleActionClient('ur_demo', msg.UrDemoAction)
        self.client.wait_for_server()
        self.goal = msg.UrDemoGoal()

        # gripper action client
        self.client_g = actionlib.SimpleActionClient('robotiq_demo', msg.UrDemoAction)
        self.client_g.wait_for_server()
        self.goal_g = msg.UrDemoGoal()
        self.goal_g.urpos = [0]

    def sendGoalAndWait(self, actClient, goalMsg, name='arm'):
        actClient.send_goal(goalMsg)
        actClient.wait_for_result()
        result = actClient.get_result()
        if name == 'arm':
            # print(list(result.rurpos))
            # print('-------------')
            # print(list(result.rurpos)[:7])
            # print('-------------')
            # print(list(result.rurpos)[7:13])
            # print('-------------')
            # print([list(result.rurpos)[13]])
            self.robot_pose[0] = list(result.rurpos)[:7]
            self.robot_pose[1] = list(result.rurpos)[7:13]
            self.robot_pose[2] = [list(result.rurpos)[13]]
        elif name == 'gripper':
            pass
        return result

    # input 3 position values of end-effect
    def set_pose_with_posi(self, *args):
        self.goal.mode_id = 1
        self.goal.action_id = 1
        self.goal.urpos = [args[0], args[1], args[2], 0.70710678, 0.0, 0.0,
                           0.70710678]  # , 0, math.pi / 2, math.pi / 2]
        result = self.sendGoalAndWait(self.client, self.goal)
        return result.rurpos

    # input six joint values
    def set_pose_with_joint(self, *args):
        self.goal.mode_id = 2
        self.goal.action_id = 1
        self.goal.urpos = list(args)
        result = self.sendGoalAndWait(self.client, self.goal)
        return result.rurpos

    # default input 0 or 1 with gripper open or close   例:class.gripper_set_pose(0)
    # or a value between 0-? and control='dis' to specific the distance 例: class.gripper_set_pose(0.3,control='dis')
    def gripper_set_pose(self, *args, control='cANDo'):
        self.goal_g.mode_id = 1
        self.goal_g.urpos = [0]
        self.goal_g.urpos[0] = 0.0 if args[0] == 0 else 0.285
        if control == 'dis':
            self.goal_g.urpos[0] = args[0]
        result_g = self.sendGoalAndWait(self.client_g, self.goal_g, name='gripper')
        return result_g

    def get_robot_pose(self):
        return self.robot_pose

    # initial pose for 2 types
    # 1.a horizon pose
    # 2.grasp pose ,which the end pose is approx [0.4,0.4,0.9]
    def initial_pose_with_joint(self, pose=None):
        if pose == 'initial':
            self.set_pose_with_joint(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        elif pose == 'grasp_initial':
            self.set_pose_with_joint(-1.9, -1.7, -2.0, -0.98, 1.57, -0.36)


if __name__ == '__main__':
    ur = ur3e()
    # ur.env.cube_reset()
    # result = ur.get_pose()
    # ur.initial_pose_with_joint(pose='grasp_initial')
    ur.env.set_cube(0.5, 0.2, 1.1, name='yellow_cube')
    # ur.env.set_cube(0.5, 0.5, 1.0, name='green_cube')
    # ur.env.set_cube(0.5, 0.5, 1.0, name='green_cube')
    # # ur.gripper_set_pose(0)
    # # result=ur.set_pose_with_joint(0,0,0,0,0,0)
    # # print(result)
    # # ur.set_pose_with_joint(0, 0, 0,0,0,0)
    #
    # # ur.initial_pose_with_joint(pose='grasp_initial')
    # # result = ur.env.get_cube_state()
    # # print(ur.env.cube_state[0])
    # result = ur.set_pose_with_posi(0.4, 0.2, 0.99)
    # ur.gripper_set_pose(0.0, control='dis')
    # # print(result)
    # result = ur.set_pose_with_posi(0.4, 0.2, 0.88)
    # ur.gripper_set_pose(0.28, control='dis')
    # result = ur.set_pose_with_posi(0.4, 0.2, 0.99)
    # env.set_cube(0.5,0.5,1.0,name='green_cube')
    # ur.set_pose_with_posi(0.3, 0.5, 1.05)
