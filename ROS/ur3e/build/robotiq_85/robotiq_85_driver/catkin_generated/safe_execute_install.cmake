execute_process(COMMAND "/home/wangzitu/ur3e/build/robotiq_85/robotiq_85_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/wangzitu/ur3e/build/robotiq_85/robotiq_85_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
