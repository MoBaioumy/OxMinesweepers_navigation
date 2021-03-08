cmake_minimum_required(VERSION 3.0.2)
project(robot)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES movement
#  CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


add_executable(monitor src/monitor.cpp)
target_link_libraries(monitor ${catkin_LIBRARIES})

add_executable(move src/move.cpp)
target_link_libraries(move ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS src/monitor_py.py src/move_py.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

