cmake_minimum_required(VERSION 2.8.3)
project(tiburon)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED
tf
rospy
roscpp
geometry_msgs
std_msgs
dynamic_reconfigure
message_generation
genmsg
actionlib_msgs
cv_bridge
#opencv2
sensor_msgs
)
#find_package(OpenCV)


## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend and a run_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependencies might have been
##     pulled in transitively but can be declared for certainty nonetheless:
##     * add a build_depend tag for "message_generation"
##     * add a run_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   sensor_data.msg
   send_arduino.msg
   ins_data.msg
   auvcontrol.msg
 )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   YPR.srv
   depth_srv.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
   geometry_msgs  # Or other packages containing msgs
   actionlib_msgs
 )
generate_dynamic_reconfigure_options(
  cfg/pid.cfg
  cfg/pitchpid.cfg
  cfg/depthpid.cfg
  cfg/yawPitchDepth.cfg
)
###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES tiburon
  CATKIN_DEPENDS roscpp rospy sensor_msgs geometry_msgs tf dynamic_reconfigure  actionlib_msgs
  DEPENDS system_lib
  CATKIN_DEPENDS message_runtime
)
include_directories(${Opencv_INCLUDE_DIRS})
###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(${catkin_INCLUDE_DIRS})

include_directories(vnccpplib/include)
add_library(vn100
    vnccpplib/src/vn100.c
)
add_library(vncp_services
 vnccpplib/src/arch/linux/vncp_services.c
)

## Declare a cpp library
# add_library(tiburon
#   src/${PROJECT_NAME}/tiburon.cpp
# )
add_executable(vn100_node  src/vn100_node.cpp
                           vnccpplib/src/arch/linux/vncp_services.c
                           vnccpplib/src/vn100.c
)

target_link_libraries(vncp_services
pthread
)
target_link_libraries(vn100_node
${catkin_LIBRARIES}
vncp_services
vn100
)
add_executable(thruster_controller src/thruster_controller.cpp)
target_link_libraries(thruster_controller ${catkin_LIBRARIES})

add_executable(rviz src/pub_rviz.cpp)
target_link_libraries(rviz ${catkin_LIBRARIES})

add_executable(thruster_joy_exe src/thruster_control_joy.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(pkg1_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
 target_link_libraries(thruster_joy_exe
   ${catkin_LIBRARIES}
 )


#target_link_libraries(yawPitchDepth_config
#   ${catkin_LIBRARIES}
# )

#add_dependencies(talker shaswat_control_generate_messages_cpp)
## Declare a cpp executable
# add_executable(tiburon_node src/tiburon_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
# add_dependencies(tiburon_node tiburon_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(tiburon_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS tiburon tiburon_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_tiburon.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
