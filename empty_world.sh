#!/bin/bash

roslaunch jackal_gazebo empty_world.launch config:=front_laser &
sleep 10
roslaunch jackal_navigation odom_navigation_demo.launch &
sleep 10
roslaunch jackal_viz view_robot.launch config:=navigation &
rqt &
