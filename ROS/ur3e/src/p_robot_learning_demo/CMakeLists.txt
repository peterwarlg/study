cmake_minimum_required(VERSION 2.8.3)
project(p_robot_learning_demo)
set(CMAKE_CXX_FLAG “-std=c++11” ${CMAKE_CXX_FLAGS})#此行新增


find_package(catkin REQUIRED COMPONENTS
  genmsg
  cmake_modules
  roscpp
  rospy
  message_generation
  moveit_core
  moveit_msgs
  moveit_ros_planning_interface
  std_msgs
  gazebo_msgs
  ur_msgs
  actionlib
  actionlib_msgs
)



 add_action_files(
   FILES
   UrDemo.action
#   Action2.action
 )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
    actionlib_msgs # std_msgs Or other packages containing msgs 
 )



catkin_package(
  #INCLUDE_DIRS include
  #CATKIN_DEPENDS roscpp message_runtime std_msgs actionlib
#  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)



add_executable(p_robot_go_server src/p_robot_go_server.cpp)
target_link_libraries(p_robot_go_server ${catkin_LIBRARIES})
add_executable(p_robot_go_server_real src/p_robot_go_server_real.cpp)
target_link_libraries(p_robot_go_server_real ${catkin_LIBRARIES})
add_executable(p_robot_go_client src/p_robot_go_client.cpp)
target_link_libraries(p_robot_go_client ${catkin_LIBRARIES})
add_executable(robotiq_grasp src/robotiq_grasp.cpp)
target_link_libraries(robotiq_grasp ${catkin_LIBRARIES})
add_executable(robotiq_server src/robotiq_server.cpp)
target_link_libraries(robotiq_server ${catkin_LIBRARIES})
add_executable(add_object src/add_object.cpp)
target_link_libraries(add_object ${catkin_LIBRARIES})
add_executable(gazebo_set_states_client src/gazebo_set_states_client.cpp)
target_link_libraries(gazebo_set_states_client ${catkin_LIBRARIES})
#add_executable(joint_state_control src/joint_state_control.cpp)
#target_link_libraries(joint_state_control ${catkin_LIBRARIES})

## Rename C++ executable without prefix
## The above recommended prefix causes long target names, the following renames the
## target back to the shorter version for ease of user use
## e.g. "rosrun someones_pkg node" instead of "rosrun someones_pkg someones_pkg_node"
# set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")
# https://blog.csdn.net/u012487272/article/details/12882283
#set_target_properties(robot_planning PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(p_robot_go_server PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(p_robot_go_client PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(robotiq_grasp PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(robotiq_server PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(add_object PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set_target_properties(gazebo_set_states_client PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
#set_target_properties(joint_state_control PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
