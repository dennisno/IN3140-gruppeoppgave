# Install script for directory: /home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/install")
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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial_msgs/msg" TYPE FILE FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial_msgs/cmake" TYPE FILE FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/build/tutorial_msgs/catkin_generated/installspace/tutorial_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/include/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/share/roseus/ros/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/share/common-lisp/ros/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/share/gennodejs/ros/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/lib/python2.7/dist-packages/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/devel/lib/python2.7/dist-packages/tutorial_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/build/tutorial_msgs/catkin_generated/installspace/tutorial_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial_msgs/cmake" TYPE FILE FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/build/tutorial_msgs/catkin_generated/installspace/tutorial_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial_msgs/cmake" TYPE FILE FILES
    "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/build/tutorial_msgs/catkin_generated/installspace/tutorial_msgsConfig.cmake"
    "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/build/tutorial_msgs/catkin_generated/installspace/tutorial_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial_msgs" TYPE FILE FILES "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/package.xml")
endif()
