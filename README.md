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

Other dependancies

`sudo apt install ros-melodic-jackal-viz ros-melodic-jackal-navigation ros-melodic-position-controllers`

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

To simplify the start up and testing process, the shell script `./empty_world.sh` has been provided to launch all the necessary ROS processes.

Simply enter Terminal from where the script is located and type
`./empty_world.sh`

**Navigation**
This allows you to directly control how much you want to move and turn the robot. This implemented mainly for manual control of the robot

`rosrun odom monitor_odom.py`

Allows you to see the current twist of the robot


`rosrun odom set_odom.py`

Allows you to inject a custom twist to the robot.

**Goal Setting**
This allow us to hijack the ROS Navigation Stack and set a custom target for the odometry to reach.

So this will only work if you are already running `roslaunch jackal_navigation odom_navigation_demo.launch`

1)
`rosrun goal set_goal.py`
This allows you to inject a specific x,y,orientation for the jackal to move to at

You can now enter each variable directly

2)
`rosrun goal waypoint_parser.py`
This allows you to put all the destination you want your robot to reach in a list and it will move the robot to each location one by one

To change which parser list you want to run: Please edit the path under `jackal_move/launch/launch/launch_all.launch`

However, right now this function is broken. So the best way is still to go into the python file and edit the address of the objective list manually.

**Test World**

`./nav_test.sh`
`roslaunch launch test_world.launch`
This put jackal in the temporary test world I have made.


**Known Issues**
If you encounter an error that says you dont have permission to run these script or it tells you that `Couldn't find executable named <file_name>`

Go to the folder where the python scripts are found

`chmod 777 <filename>`

Or just change the permission of the entire folder

`chmod -p 777 <foldername>`

