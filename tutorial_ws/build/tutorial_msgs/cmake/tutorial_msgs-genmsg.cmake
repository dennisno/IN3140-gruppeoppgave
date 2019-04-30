# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "tutorial_msgs: 1 messages, 0 services")

set(MSG_I_FLAGS "-Itutorial_msgs:/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(tutorial_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_custom_target(_tutorial_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tutorial_msgs" "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" "geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(tutorial_msgs
  "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tutorial_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(tutorial_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tutorial_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(tutorial_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(tutorial_msgs_generate_messages tutorial_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_dependencies(tutorial_msgs_generate_messages_cpp _tutorial_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tutorial_msgs_gencpp)
add_dependencies(tutorial_msgs_gencpp tutorial_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tutorial_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(tutorial_msgs
  "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tutorial_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(tutorial_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tutorial_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(tutorial_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(tutorial_msgs_generate_messages tutorial_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_dependencies(tutorial_msgs_generate_messages_eus _tutorial_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tutorial_msgs_geneus)
add_dependencies(tutorial_msgs_geneus tutorial_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tutorial_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(tutorial_msgs
  "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tutorial_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(tutorial_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tutorial_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(tutorial_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(tutorial_msgs_generate_messages tutorial_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_dependencies(tutorial_msgs_generate_messages_lisp _tutorial_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tutorial_msgs_genlisp)
add_dependencies(tutorial_msgs_genlisp tutorial_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tutorial_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(tutorial_msgs
  "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tutorial_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(tutorial_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tutorial_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(tutorial_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(tutorial_msgs_generate_messages tutorial_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_dependencies(tutorial_msgs_generate_messages_nodejs _tutorial_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tutorial_msgs_gennodejs)
add_dependencies(tutorial_msgs_gennodejs tutorial_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tutorial_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(tutorial_msgs
  "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tutorial_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(tutorial_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tutorial_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(tutorial_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(tutorial_msgs_generate_messages tutorial_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/eirikolb/M-drive/Documents/In3140/ROS/3140gruppeoppgave/tutorial_ws/src/tutorial_msgs/msg/RobotPos.msg" NAME_WE)
add_dependencies(tutorial_msgs_generate_messages_py _tutorial_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tutorial_msgs_genpy)
add_dependencies(tutorial_msgs_genpy tutorial_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tutorial_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tutorial_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tutorial_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(tutorial_msgs_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tutorial_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tutorial_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(tutorial_msgs_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tutorial_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tutorial_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(tutorial_msgs_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tutorial_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tutorial_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(tutorial_msgs_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tutorial_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tutorial_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tutorial_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(tutorial_msgs_generate_messages_py geometry_msgs_generate_messages_py)
endif()
