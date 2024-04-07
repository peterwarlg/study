较新的gym版本中能找到对应的`gym_robotics`文件夹
如果是conda环境的话，就在`env_name/lib/python3.x(你的python版本)/site_packages/gym`目录下
ur3e_grip_3,ur3e_grip_4是自己加的的两个环境，
ur3e_grip_4先不用管
/ur3e_grip_3是参考/fetch（同级目录fetch文件夹）写的，其中
可以直接移植拷到自己电脑的对应目录下：
1. 将gym_robotics/envs/ur3e_grip_3拷贝到自己的环境中的对应路径
2. 修改robot_env.py,ur_env.py,ur_pick_and_place.py三个文件中的模型的绝对路径
3. 在gym_robotics/envs/__init__.py中增加对应内容（参考此文件夹）
4. 在gym_robotics/__init__.py中增加对应内容
5. 总结：检查所有__init__文件，出现了fetch环境的话，一般是需要添加自己的内容的
6. 使用方法：
   ```python3
    import gym
   e = gym.make('ur3e-v3') #即__init__.py中指定的id
   # 然后像别的gym环境一样使用即可；如reset(),step(),render()
    ```