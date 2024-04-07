#!/usr/bin/env python


import tkinter as tk  # 使用Tkinter前需要先导入
from Robot import ur3e


class Thinker_node(tk.Tk, object):

    def __init__(self):
        self.ur = ur3e()
        super(Thinker_node, self).__init__()  # gripper
        self.color = 'white'
        self.font = '微软雅黑'
        self.font_size = 15
        self.title('robot control')
        self.geometry('1200x300')  # 这里的乘是小x
        self.xyzori_width = 15
        self.xyzori_high = 1
        self.joint_width = 10
        self.joint_high = 1

        self.p = [tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None)]

        self.j = [tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None),
                  tk.Entry(self, show=None)]

        self.g = [tk.Entry(self, show=None)]

        self.robot_pose = [tk.DoubleVar(),
                           tk.DoubleVar(),
                           tk.DoubleVar(),
                           tk.DoubleVar(),
                           tk.DoubleVar(),
                           tk.DoubleVar(),
                           tk.DoubleVar()]

        self.robot_joint = [tk.DoubleVar(),
                            tk.DoubleVar(),
                            tk.DoubleVar(),
                            tk.DoubleVar(),
                            tk.DoubleVar(),
                            tk.DoubleVar()]

        self.gripper_pose = [tk.DoubleVar()]

        self.gripper_text = [
            tk.Label(self, textvariable=self.gripper_pose[0], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high)]

        self.pose_text = [
            tk.Label(self, textvariable=self.robot_pose[0], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[1], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[2], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[3], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[4], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[5], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high),
            tk.Label(self, textvariable=self.robot_pose[6], bg=self.color, font=(self.font, self.font_size),
                     width=self.xyzori_width,
                     height=self.xyzori_high)]

        self.joint_text = [
            tk.Label(self, textvariable=self.robot_joint[0], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high),
            tk.Label(self, textvariable=self.robot_joint[1], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high),
            tk.Label(self, textvariable=self.robot_joint[2], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high),
            tk.Label(self, textvariable=self.robot_joint[3], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high),
            tk.Label(self, textvariable=self.robot_joint[4], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high),
            tk.Label(self, textvariable=self.robot_joint[5], bg=self.color, font=(self.font, self.font_size),
                     width=self.joint_width,
                     height=self.joint_high)]

    def show(self):

        self.gripper_text[0].grid(column=5, row=2)
        self.g[0].grid(column=4, row=2)

        for i in range(7):
            self.p[i].grid(column=1, row=i, pady=8)
            self.pose_text[i].grid(column=0, row=i)
        for i in range(6):
            self.j[i].grid(column=2, row=i, pady=8)
            self.joint_text[i].grid(column=3, row=i)

    def result_to_tk(self, result):
        for i in range(7):
            self.robot_pose[i].set(round(result[i], 3))
        for i in range(6):
            self.robot_joint[i].set(round(result[i + 6], 3))

    def insert_pose(self):
        robot_pose = []
        for i in range(7):
            if not list(self.p[i].get()):
                robot_pose.append(self.ur.robot_pose[0][i])
            else:
                robot_pose.append(float(self.p[i].get().strip("'")) / 10)
        # print('robot_pose', type(robot_pose[0]))
        result = self.ur.set_pose_with_posi(robot_pose[0], robot_pose[1], robot_pose[2])
        # print('result:', result)
        self.result_to_tk(result)
        return result

    def insert_joint(self):
        robot_joint = []
        for i in range(6):
            if not list(self.j[i].get()):
                robot_joint.append(self.ur.robot_pose[1][i])
            else:
                robot_joint.append(float(self.j[i].get().strip("'")))

        result = self.ur.set_pose_with_joint(robot_joint[0], robot_joint[1], robot_joint[2], robot_joint[3],
                                             robot_joint[4], robot_joint[5])
        self.result_to_tk(result)

        return result

    def insert_gripper(self):
        robot_gripper = []
        robot_gripper.append(float(self.g[0].get().strip("'")))
        result = self.ur.gripper_set_pose(robot_gripper[0], control='dis')
        return result

    def initial(self):
        result = self.ur.initial_pose_with_joint(pose='grasp_initial')
        self.result_to_tk(result)

    # def quit(self):
    #     self.quit()

    def reset_cube(self):
        self.ur.env.cube_reset()

if __name__ == '__main__':
    tkk = Thinker_node()
    tkk.ur.initial_pose_with_joint(pose='grasp_initial')
    tkk.show()

    b1 = tk.Button(tkk, text='insert pose', width=10, height=2, command=tkk.insert_pose)
    b1.grid(column=1, row=8)
    b2 = tk.Button(tkk, text='insert joint', width=10, height=2, command=tkk.insert_joint)
    b2.grid(column=2, row=8)
    b3 = tk.Button(tkk, text='insert gripper', width=10, height=2, command=tkk.insert_gripper)
    b3.grid(column=4, row=8)
    b4 = tk.Button(tkk, text='Exit', width=10, height=2, command=tkk.quit)
    b4.grid(column=6, row=8)
    b5 = tk.Button(tkk, text='initial', width=10, height=2, command=tkk.initial)
    b5.grid(column=6, row=7)
    b6 = tk.Button(tkk, text='cube_reset', width=10, height=2, command=tkk.reset_cube)
    b6.grid(column=6, row=6)
    tkk.mainloop()