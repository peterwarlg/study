# Install script for directory: /home/wangzitu/ur3e/src/p_robot_learning_demo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/wangzitu/ur3e/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo/action" TYPE FILE FILES "/home/wangzitu/ur3e/src/p_robot_learning_demo/action/UrDemo.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo/msg" TYPE FILE FILES
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoAction.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionGoal.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionResult.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoActionFeedback.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoGoal.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoResult.msg"
    "/home/wangzitu/ur3e/devel/share/p_robot_learning_demo/msg/UrDemoFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo/cmake" TYPE FILE FILES "/home/wangzitu/ur3e/build/p_robot_learning_demo/catkin_generated/installspace/p_robot_learning_demo-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/wangzitu/ur3e/devel/include/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/wangzitu/ur3e/devel/share/roseus/ros/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/wangzitu/ur3e/devel/share/common-lisp/ros/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/wangzitu/ur3e/devel/share/gennodejs/ros/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/wangzitu/ur3e/devel/lib/python2.7/dist-packages/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/wangzitu/ur3e/devel/lib/python2.7/dist-packages/p_robot_learning_demo")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/wangzitu/ur3e/build/p_robot_learning_demo/catkin_generated/installspace/p_robot_learning_demo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo/cmake" TYPE FILE FILES "/home/wangzitu/ur3e/build/p_robot_learning_demo/catkin_generated/installspace/p_robot_learning_demo-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo/cmake" TYPE FILE FILES
    "/home/wangzitu/ur3e/build/p_robot_learning_demo/catkin_generated/installspace/p_robot_learning_demoConfig.cmake"
    "/home/wangzitu/ur3e/build/p_robot_learning_demo/catkin_generated/installspace/p_robot_learning_demoConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/p_robot_learning_demo" TYPE FILE FILES "/home/wangzitu/ur3e/src/p_robot_learning_demo/package.xml")
endif()

