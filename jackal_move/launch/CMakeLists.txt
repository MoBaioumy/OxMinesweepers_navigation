cmake_minimum_required(VERSION 3.0.2)
project(launch)


set(CATKIN_PACKAGE_DEPENDENCIES
    rospy
    jackal_viz
    jackal_navigation
    position_controllers
    goal
    robot
)

find_package(catkin REQUIRED COMPONENTS ${CATKIN_PACKAGE_DEPENDENCIES})

catkin_package(
  CATKIN_DEPENDS
    ${CATKIN_PACKAGE_DEPENDENCIES}
)


install(DIRECTORY launch worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

