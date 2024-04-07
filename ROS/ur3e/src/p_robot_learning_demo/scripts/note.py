#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

import tkinter as tk  # 使用Tkinter前需要先导入
from Robot1 import ur3e

gripper_control = False
joint_control = False
pose_control = False
xyzori_width = 10
xyzori_high = 1
joint_width = 10
joint_high = 1
couter = 1
ur = ur3e()
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('robot control')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x300')  # 这里的乘是小x
# 第4步，在图形界面上创建一个标签label用以显示并放置
#
p1 = tk.Entry(window, show=None)
p2 = tk.Entry(window, show=None)
p3 = tk.Entry(window, show=None)
p4 = tk.Entry(window, show=None)
p5 = tk.Entry(window, show=None)
p6 = tk.Entry(window, show=None)
p6 = tk.Entry(window, show=None)
p7 = tk.Entry(window, show=None)

j1 = tk.Entry(window, show=None)
j2 = tk.Entry(window, show=None)
j3 = tk.Entry(window, show=None)
j4 = tk.Entry(window, show=None)
j5 = tk.Entry(window, show=None)
j6 = tk.Entry(window, show=None)

p1.grid(column=1, row=1, pady=8)
p2.grid(column=1, row=2, pady=8)
p3.grid(column=1, row=3, pady=8)
p4.grid(column=1, row=4, pady=8)
p5.grid(column=1, row=5, pady=8)
p6.grid(column=1, row=6, pady=8)
p7.grid(column=1, row=7, pady=8)

j1.grid(column=2, row=1, pady=8)
j2.grid(column=2, row=2, pady=8)
j3.grid(column=2, row=3, pady=8)
j4.grid(column=2, row=4, pady=8)
j5.grid(column=2, row=5, pady=8)
j6.grid(column=2, row=6, pady=8)


robot_pose1 = tk.DoubleVar()
robot_pose2 = tk.DoubleVar()
robot_pose3 = tk.DoubleVar()
robot_pose4 = tk.DoubleVar()
robot_pose5 = tk.DoubleVar()
robot_pose6 = tk.DoubleVar()
robot_pose7 = tk.DoubleVar()

robot_joint1 = tk.DoubleVar()
robot_joint2 = tk.DoubleVar()
robot_joint3 = tk.DoubleVar()
robot_joint4 = tk.DoubleVar()
robot_joint5 = tk.DoubleVar()
robot_joint6 = tk.DoubleVar()

p_t1 = tk.Label(window, textvariable=robot_pose1, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t2 = tk.Label(window, textvariable=robot_pose2, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t3 = tk.Label(window, textvariable=robot_pose3, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t4 = tk.Label(window, textvariable=robot_pose4, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t5 = tk.Label(window, textvariable=robot_pose5, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t6 = tk.Label(window, textvariable=robot_pose6, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)
p_t7 = tk.Label(window, textvariable=robot_pose7, bg='green', font=('Arial', 12), width=xyzori_width, height=xyzori_high)

j_t1 = tk.Label(window, textvariable=robot_joint1, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)
j_t2 = tk.Label(window, textvariable=robot_joint2, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)
j_t3 = tk.Label(window, textvariable=robot_joint3, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)
j_t4 = tk.Label(window, textvariable=robot_joint4, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)
j_t5 = tk.Label(window, textvariable=robot_joint5, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)
j_t6 = tk.Label(window, textvariable=robot_joint6, bg='green', font=('Arial', 12), width=joint_width, height=joint_high)


p_t1.grid(column=0,row=1)
p_t2.grid(column=0,row=2)
p_t3.grid(column=0,row=3)
p_t4.grid(column=0,row=4)
p_t5.grid(column=0,row=5)
p_t6.grid(column=0,row=6)
p_t7.grid(column=0,row=7)

j_t1.grid(column=3,row=1)
j_t2.grid(column=3,row=2)
j_t3.grid(column=3,row=3)
j_t4.grid(column=3,row=4)
j_t5.grid(column=3,row=5)
j_t6.grid(column=3,row=6)

def insert_pose():
    robot_pose = []
    robot_pose.append(p1.get())
    robot_pose.append(p2.get())
    robot_pose.append(p3.get())
    robot_pose.append(p4.get())
    robot_pose.append(p5.get())
    robot_pose.append(p6.get())
    robot_pose.append(p7.get())

    result = ur.set_pose_with_posi(robot_pose)

    robot_pose1.set(result[0])
    robot_pose2.set(result[1])
    robot_pose3.set(result[2])
    robot_pose4.set(result[3])
    robot_pose5.set(result[4])
    robot_pose6.set(result[5])
    robot_pose7.set(result[6])

    return result


def insert_joint():
    robot_joint = []
    robot_joint.append(j1.get())
    robot_joint.append(j2.get())
    robot_joint.append(j3.get())
    robot_joint.append(j4.get())
    robot_joint.append(j5.get())
    robot_joint.append(j6.get())

    result = ur.set_pose_with_joint(robot_joint)

    robot_joint1.set(result[7])
    robot_joint2.set(result[8])
    robot_joint3.set(result[9])
    robot_joint4.set(result[10])
    robot_joint5.set(result[11])
    robot_joint6.set(result[12])

    return result

def insert_gripper():
    pass

b1 = tk.Button(window, text='insert pose', width=10, height=2, command=insert_pose)
b1.grid(column=1, row=8)
b2 = tk.Button(window, text='insert joint', width=10, height=2, command=insert_joint)
b2.grid(column=2, row=8)
b3 = tk.Button(window, text='insert gripper', width=10, height=2, command=insert_gripper)
b3.grid(column=4, row=8)





# 第7步，主窗口循环显示
window.mainloop()
