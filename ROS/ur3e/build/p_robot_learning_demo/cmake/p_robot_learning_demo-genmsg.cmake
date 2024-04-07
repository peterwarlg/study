# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "p_robot_learning_demo: 7 messages, 0 services")

set(MSG_I_FLAGS "-Ip_robot_learning_demo:/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(p_robot_learning_demo_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" ""
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" ""
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:p_robot_learning_demo/UrDemoResult:std_msgs/Header"
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" "actionlib_msgs/GoalID:p_robot_learning_demo/UrDemoResult:actionlib_msgs/GoalStatus:p_robot_learning_demo/UrDemoActionResult:p_robot_learning_demo/UrDemoActionFeedback:p_robot_learning_demo/UrDemoActionGoal:p_robot_learning_demo/UrDemoFeedback:std_msgs/Header:p_robot_learning_demo/UrDemoGoal"
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" "p_robot_learning_demo/UrDemoGoal:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" "p_robot_learning_demo/UrDemoFeedback:actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:std_msgs/Header"
)

get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_custom_target(_p_robot_learning_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "p_robot_learning_demo" "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_cpp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
)

### Generating Services

### Generating Module File
_generate_module_cpp(p_robot_learning_demo
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(p_robot_learning_demo_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(p_robot_learning_demo_generate_messages p_robot_learning_demo_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_cpp _p_robot_learning_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(p_robot_learning_demo_gencpp)
add_dependencies(p_robot_learning_demo_gencpp p_robot_learning_demo_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS p_robot_learning_demo_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_eus(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
)

### Generating Services

### Generating Module File
_generate_module_eus(p_robot_learning_demo
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(p_robot_learning_demo_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(p_robot_learning_demo_generate_messages p_robot_learning_demo_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_eus _p_robot_learning_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(p_robot_learning_demo_geneus)
add_dependencies(p_robot_learning_demo_geneus p_robot_learning_demo_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS p_robot_learning_demo_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_lisp(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
)

### Generating Services

### Generating Module File
_generate_module_lisp(p_robot_learning_demo
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(p_robot_learning_demo_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(p_robot_learning_demo_generate_messages p_robot_learning_demo_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_lisp _p_robot_learning_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(p_robot_learning_demo_genlisp)
add_dependencies(p_robot_learning_demo_genlisp p_robot_learning_demo_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS p_robot_learning_demo_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_nodejs(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
)

### Generating Services

### Generating Module File
_generate_module_nodejs(p_robot_learning_demo
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(p_robot_learning_demo_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(p_robot_learning_demo_generate_messages p_robot_learning_demo_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_nodejs _p_robot_learning_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(p_robot_learning_demo_gennodejs)
add_dependencies(p_robot_learning_demo_gennodejs p_robot_learning_demo_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS p_robot_learning_demo_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)
_generate_msg_py(p_robot_learning_demo
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
)

### Generating Services

### Generating Module File
_generate_module_py(p_robot_learning_demo
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(p_robot_learning_demo_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(p_robot_learning_demo_generate_messages p_robot_learning_demo_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg" NAME_WE)
add_dependencies(p_robot_learning_demo_generate_messages_py _p_robot_learning_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(p_robot_learning_demo_genpy)
add_dependencies(p_robot_learning_demo_genpy p_robot_learning_demo_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS p_robot_learning_demo_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/p_robot_learning_demo
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(p_robot_learning_demo_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/p_robot_learning_demo
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(p_robot_learning_demo_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/p_robot_learning_demo
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(p_robot_learning_demo_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/p_robot_learning_demo
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(p_robot_learning_demo_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/p_robot_learning_demo
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(p_robot_learning_demo_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
