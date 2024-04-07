#!/bin/bash
roslaunch robot_moveit_config ur3_e_moveit_planning_execution.launch sim:=true &
sleep 3
echo "moveit starting success!"
 
roslaunch robot_moveit_config moveit_rviz.launch config:=true &
sleep 2
wait
exit 0
