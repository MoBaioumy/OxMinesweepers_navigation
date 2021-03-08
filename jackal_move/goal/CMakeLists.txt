cmake_minimum_required(VERSION 3.0.2)
project(goal)

set(CATKIN_PACKAGE_DEPENDENCIES
  geometry_msgs
  roscpp
  rospy
  std_msgs
  move_base_msgs
  actionlib
)

find_package(catkin REQUIRED COMPONENTS 
  ${CATKIN_PACKAGE_DEPENDENCIES}
)

catkin_package(
  CATKIN_DEPENDS
    ${CATKIN_PACKAGE_DEPENDENCIES}
)

install(PROGRAMS src/set_goal.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(PROGRAMS src/waypoiny_parser.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
