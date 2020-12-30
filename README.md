# OxMinesweepers_navigation
Repository for the navigation team of OxMinesweepers 2020/2021


This a slightly modified version of the ROS talker and listener node that serves as a proof of concept of how the Jackal’s geometry_msgs.
http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29

However, the version of catkin we are using is 
https://catkin-tools.readthedocs.io/en/latest/installing.html

NOTE: This is not a exact representation of how the robot will drive (we need to take into account of  Achermann steering geometry). But as a starting point to software, this should be sufficient.


## Dependancies
jackal_simulator
[Source Code](https://github.com/jackal/jackal_simulator)
`sudo apt install ros-melodic-jackal-simulator ros-melodic-position-controllers`

## Building

**Create Catkin Workspace**
`mkdir -p <your own workspace>/src`
`cd <your own workspace>`
`catkin init`
`cd src`
<--clone this repo here-->

**Build**
`catkin build`
`cd <your own workspace>/src`
`source ../devel/setup.bash`

## Run
**Simulator**
`roslaunch jackal_gazebo jackal_world.launch config:=front_laser`

**Navigation**
C++ Version
1)
`rosrun robot monitor`
You should see the linear and angular speed of the robot printed in terminal

2)
`rosrun robot move`
Under gazebo, you should see the robot moving in a circle.

Python Version
1)
`rosrun robot monitor_py.py`

2)
`rosrun robot move_py.py`

Warning: If you encounter an error that says you dont have permission to run these script

Go to the folder where the python scripts are found

chmod 777 <filename>

