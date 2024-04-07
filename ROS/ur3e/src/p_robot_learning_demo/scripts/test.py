#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

robot_pose = [[0.0] * 7,
              [0.0] * 6,
              []]
result = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

x = '0.4'
print(float(x))
robot_pose[0]=result[:7]
robot_pose[1]=result[7:13]
robot_pose[2] = [result[13]]
# print(robot_pose)
